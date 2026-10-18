#!/usr/bin/env python3
"""Ask a dated, cited research question in Hebrew or English, without API keys."""
import argparse
import json
from pathlib import Path
import sys
import answering
import research_pipeline as pipeline
import stock_brain as kb


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('question')
    parser.add_argument('--root', type=Path, default=kb.ROOT)
    parser.add_argument('--language', choices=['auto', 'he', 'en'], default='auto')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown')
    parser.add_argument('--monitor-report', type=Path)
    args = parser.parse_args()
    try:
        report = pipeline.read_json(args.monitor_report) if args.monitor_report else None
        result = answering.answer(args.question, args.root, args.language, report)
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == 'json' else answering.markdown(result))
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
