from copy import deepcopy
import json
import os
from pathlib import Path
import shutil
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import brain_markdown as brain
import sector_facts as facts
import stock_brain as kb
import test_brain_markdown


class SectorFactsTests(unittest.TestCase):
    def setUp(self):
        test_brain_markdown.MarkdownTests.setUp(self)
        self.compact = self.root / 'compact'
        self.target = self.root / 'main'
        self.target.mkdir()

    def export(self):
        brain.export(self.store, self.output, self.release)
        return facts.export(self.output, self.compact, 'c' * 40)

    def test_actual_markdown_contains_financial_cells_in_main_sector_tree(self):
        manifest = self.export()
        row = manifest['companies'][0]
        self.assertEqual(row['path'], 'sectors/information-technology/facts/0000789019/README.md')
        self.assertEqual(row['classification_method'], 'curated_profile')
        raw = (self.compact / row['path']).read_text()
        meta, body = brain.split_profile(raw)
        self.assertIn('| revenue |', body)
        self.assertIn('Unavailable / blocked', body)
        self.assertIn('negative of reported PaymentsToAcquirePropertyPlantAndEquipment', body)
        self.assertEqual(meta['status'], 'stub')
        self.assertFalse(meta['canonical_reviewed'])
        self.assertIn('/' + 'c' * 40 + '/brain/companies/', meta['full_history_url'])
        sections = kb.sections_from(body, kb.config(ROOT)[1])
        for name in ('financial-performance', 'balance-sheet-and-capital-allocation'):
            self.assertLessEqual(sections[name].count('### '), 3)
        self.assertEqual(facts.verify(self.compact), manifest)

    def test_sic_mapping_is_provisional_and_ambiguous_or_fund_issuers_stay_unclassified(self):
        base = {'issuer_classification': {'sic': '2834', 'sic_description': 'Pharmaceutical preparations'},
                'classification_source': {'url': 'https://data.sec.gov/submissions/CIK0000000001.json'}}
        result = facts.classify(base)
        self.assertEqual(result['sector'], 'health-care')
        self.assertEqual(result['method'], 'project_sic_rule')
        self.assertIn('not licensed or official GICS', result['reason'])
        for code in ('6798', '6770', '7370', None, '9999'):
            value = deepcopy(base)
            value['issuer_classification']['sic'] = code
            self.assertEqual(facts.classify(value)['sector'], 'unclassified')
        base['financial_gap'] = {'reason': 'fund_reporting_review'}
        self.assertEqual(facts.classify(base)['sector'], 'unclassified')
        base.pop('financial_gap')
        base.pop('classification_source')
        self.assertEqual(facts.classify(base)['sector'], 'unclassified')

    def test_main_install_is_repeatable_and_never_overwrites_manual_facts_or_research(self):
        self.export()
        curated = self.target / 'sectors/information-technology/companies/MSFT/README.md'
        curated.parent.mkdir(parents=True)
        curated.write_text('User-owned research stays intact.')
        facts.install(self.compact, self.target)
        facts.install(self.compact, self.target)
        self.assertEqual(curated.read_text(), 'User-owned research stays intact.')
        path = self.target / 'sectors/information-technology/facts/0000789019/README.md'
        path.write_text(path.read_text() + '\nManual note\n')
        with self.assertRaisesRegex(ValueError, 'preserve manual changes'):
            facts.install(self.compact, self.target)
        self.assertIn('Manual note', path.read_text())

    def test_integrity_and_no_research_promotion_are_enforced(self):
        manifest = self.export()
        path = self.compact / manifest['companies'][0]['path']
        original = path.read_text()
        path.write_text(original.replace('canonical_reviewed: false', 'canonical_reviewed: true'))
        m = self.compact / facts.MANIFEST
        manifest['companies'][0].update(sha256=brain.digest(path.read_bytes()), size_bytes=path.stat().st_size)
        m.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'research promotion'):
            facts.verify(self.compact)

    def test_indexes_show_actual_facts_separately_from_curated_counts(self):
        self.export()
        for name in ('config', 'templates'):
            shutil.copytree(ROOT / name, self.target / name)
        facts.install(self.compact, self.target)
        generated = kb.generated(self.target, [])
        index = generated[Path('sectors/information-technology/INDEX.md')]
        self.assertIn('Factual files: **1**', index)
        self.assertIn('Reviewed research: **0**', index)
        self.assertIn('facts/0000789019/README.md', index)
        self.assertIn('actual company Markdown files', generated[Path('INDEX.md')])
        self.assertIn('Unclassified', generated[Path('sectors/README.md')])
        self.assertEqual(json.loads(generated[Path('data/catalog.json')])['companies'], [])

    def test_real_main_publication_is_idempotent_preserves_curated_research_and_rejects_edits(self):
        for name in ('config', 'templates', 'research'):
            shutil.copytree(ROOT / name, self.target / name)
        for path in list((ROOT / 'sectors').glob('*/*.md')) + [d.path for d in kb.documents(ROOT)]:
            dest = self.target / path.relative_to(ROOT)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)
        kb.build(self.target)
        def local(*args, cwd=self.target):
            return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True)
        local('init', '-q', '-b', 'main')
        local('add', '.')
        local('-c', 'user.name=Test', '-c', 'user.email=test@example.test', 'commit', '-qm', 'Curated baseline')
        self.release['source_commit'] = local('rev-parse', 'HEAD').stdout.strip()
        remote = self.root / 'remote.git'
        local('clone', '--bare', str(self.target), str(remote))
        before = {p.relative_to(self.target).as_posix(): p.read_bytes() for p in (self.target / 'sectors').glob('*/companies/*/README.md')}
        self.export()
        real_run = subprocess.run
        def local_remote(args, **kwargs):
            args = [str(remote) if x == 'https://github.com/' + brain.REPO + '.git' else x for x in args]
            return real_run(args, **kwargs)
        with patch.dict(os.environ, {'GH_TOKEN': 'synthetic-test-token'}), patch.object(facts.subprocess, 'run', side_effect=local_remote):
            first = facts.publish(self.compact)
            self.assertEqual(facts.publish(self.compact)['commit'], first['commit'])
            clone = self.root / 'downloaded'
            real_run(['git', 'clone', '-q', str(remote), str(clone)], check=True)
            self.assertEqual(before, {p: (clone / p).read_bytes() for p in before})
            self.assertEqual(len(kb.documents(clone)), 10)
            self.assertEqual(len(kb.export_records(clone)), len(kb.export_records(ROOT)))
            path = clone / 'sectors/information-technology/facts/0000789019/README.md'
            path.write_text(path.read_text() + '\nUser note\n')
            real_run(['git', 'add', '.'], cwd=clone, check=True)
            real_run(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.test', 'commit', '-qm', 'Manual edit'], cwd=clone, check=True)
            real_run(['git', 'push', '-q'], cwd=clone, check=True)
            with self.assertRaisesRegex(ValueError, 'preserve manual changes'):
                facts.publish(self.compact)


if __name__ == '__main__':
    unittest.main()
