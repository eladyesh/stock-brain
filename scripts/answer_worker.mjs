// One bounded, read-only request. The same evidence engine runs in the browser.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {ask} from '../site/engine.mjs';

try {
  const request = JSON.parse(fs.readFileSync(0, 'utf8'));
  if(typeof request.question !== 'string' || !request.question.trim() || request.question.length > 4000)throw Error('invalid_question');
  const raw = fs.readFileSync(process.argv[2]);
  const snapshot = JSON.parse(raw).files['desk.json'];
  const result = ask(request.question, snapshot);
  // Do not echo the full financial histories or question in the response/logs.
  result.companies = result.companies.map(({ticker,name,as_of})=>({ticker,name,as_of}));
  process.stdout.write(JSON.stringify({...result, built_at:snapshot.built_at,
    generation:crypto.createHash('sha256').update(raw).digest('hex'), engine:'evidence-v2'}));
} catch {
  process.stderr.write('Answer worker failed\n');
  process.exitCode = 1;
}
