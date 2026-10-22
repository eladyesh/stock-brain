import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import test from 'node:test';
import {projectCompanyModel, requiredRevenueCagr} from '../site/models.mjs';

function fixture(ticker = 'MSFT') {
  const model = JSON.parse(readFileSync(new URL(`../research/models/${ticker}.json`, import.meta.url)));
  // Fixture gate approval is only for math tests; production approval comes from Python.
  model.readiness = {status: 'illustrative', reasons: [], per_share_ready: true, price_ready: true};
  model.quote = {ticker, status: 'available', currency: 'USD', price: 500, trade_at: '2026-10-22T20:00:00Z', source_url: 'https://example.test/quote'};
  return model;
}

test('company paths connect revenue to profit, cash and diluted EPS without EPS growth shortcuts', () => {
  const model = fixture();
  const output = projectCompanyModel(model);
  const base = output.scenarios.find(s => s.id === 'base');
  assert.equal(base.rows[0].revenue, 331839000000 * 1.18);
  assert.equal(base.rows[0].net_income, base.rows[0].revenue * .38);
  assert.equal(base.rows[0].free_cash_flow, base.rows[0].revenue * .22);
  assert.equal(base.rows[0].eps, base.rows[0].net_income / (7453000000 * .995));
  assert.ok(Math.abs(base.terminal.revenue - 579949657781.76) < .01);
  assert.equal(base.terminal.price, base.terminal.eps * 28);
  assert.notEqual(output.horizon_years, 4);
  assert.equal(base.terminal.annualized_return, (base.terminal.price / 500) ** (1 / output.horizon_years) - 1);
});

test('one-case assumptions are editable without mutating stored paths', () => {
  const model = fixture('MU'), snapshot = JSON.stringify(model);
  const original = projectCompanyModel(model);
  const edited = projectCompanyModel(model, {scenarioId: 'bull', revenueGrowth: .1, netMargin: .2, fcfMargin: .1, shareChange: 0, exitPe: 15});
  assert.equal(JSON.stringify(model), snapshot);
  assert.deepEqual(edited.scenarios[0], original.scenarios[0]);
  assert.deepEqual(edited.scenarios[1], original.scenarios[1]);
  assert.ok(Math.abs(edited.scenarios[2].terminal.revenue - 133188000000 * 1.1 ** 4) < .001);
  assert.equal(edited.scenarios[2].modified_by_user, true);
});

test('unverified shares and nonpositive EPS never produce a P/E price', () => {
  const model = fixture();
  model.readiness.per_share_ready = false;
  model.readiness.price_ready = false;
  const output = projectCompanyModel(model);
  assert.equal(output.range.price, null);
  assert.equal(output.scenarios[1].terminal.eps, null);
  assert.equal(requiredRevenueCagr(model).status, 'unavailable');
  const loss = projectCompanyModel(fixture(), {netMargin: -.1});
  assert.ok(loss.scenarios[1].terminal.eps < 0);
  assert.equal(loss.scenarios[1].terminal.price, null);
});

test('reverse growth reproduces an explicitly chosen price-only return', () => {
  const model = fixture('NVDA');
  const required = requiredRevenueCagr(model, 'base', null, .15);
  assert.equal(required.status, 'illustrative');
  const output = projectCompanyModel(model, {revenueGrowth: required.required_revenue_cagr});
  assert.ok(Math.abs(output.scenarios[1].terminal.annualized_return - .15) < 1e-12);
});

test('bad numeric controls and dates are refused instead of coerced into plausible outputs', () => {
  for (const overrides of [{exitPe: 0}, {netMargin: '0.4'}, {revenueGrowth: -1}, {shareChange: Infinity}, {referencePrice: 0}, {scenarioId: 'missing'}]) {
    assert.equal(projectCompanyModel(fixture(), overrides).status, 'blocked');
  }
  const model = fixture();
  model.quote.trade_at = '2031-01-01';
  assert.equal(projectCompanyModel(model).scenarios[1].terminal.annualized_return, null);
  const currency = fixture();
  currency.quote.currency = 'EUR';
  assert.equal(projectCompanyModel(currency).scenarios[1].terminal.annualized_return, null);
  assert.equal(requiredRevenueCagr(currency).status, 'unavailable');
  model.valuation_date = '2030-02-31';
  assert.equal(projectCompanyModel(model).status, 'blocked');
});

test('missing strict FCF remains missing while explicit forward cash assumptions calculate', () => {
  const model = fixture('NVDA');
  assert.equal(model.base.free_cash_flow, null);
  assert.equal(model.base.supplemental_issuer_fcf.comparable_to_strict_fcf, false);
  const row = projectCompanyModel(model).scenarios[1].rows[0];
  assert.equal(row.free_cash_flow, row.revenue * .42);
  assert.equal(model.base.free_cash_flow, null);
});
