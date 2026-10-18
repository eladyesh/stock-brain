# Research desk and numerical question contract

The hosted desk is [Stock Brain](https://stock-brain-desk.neatibex64.chatgpt.site). It is owner-private; the GitHub repository and its source data remain public.

## Three distinct data layers

1. **Reviewed narrative lookup:** immutable claim text with packet/profile review bindings, Hebrew translation hashes, source links and a research cutoff. Reviews include AI checks, not independent human sign-off. The JavaScript engine is a bounded lookup engine, not a language model.
2. **Normalized SEC history:** five annual and twelve standalone quarterly periods per issuer, separately sourced and validated. Missing values, revisions, fiscal-label conflicts, definition changes and share-basis limitations remain visible. History does not automatically approve or rewrite narrative claims.
3. **Market snapshots and scenarios:** Yahoo Finance's public chart endpoint supplies a dated last regular-session trade and reported split events. It is an optional public interface without a real-time/exchange SLA. Failures preserve the old value and are logged. The scenario calculator uses an explicit user-supplied positive EPS base, EPS growth, terminal P/E, horizon and reference price.

The calculator computes EPS × (1 + growth)^years × exit P/E and price-only annualized change. It excludes dividends, tax, fees and FX. Example growth/multiple inputs are generic illustrations, not company forecasts. Negative EPS is unsupported by this P/E calculator. Reported EPS is shown as a source reference, not silently promoted into a split-comparable valuation input.

## Exact numerical answers

scripts/query_contract.py makes numeric evidence eligibility a prerequisite to ranking. The gate checks metric, period type, fiscal identity, accounting basis and guidance versus reported results. It rejects unsupported segment exclusions, constant-currency/inflation adjustments, per-employee ratios and unknown metrics. Every requested company and metric must be supported; the engine cannot silently answer a smaller comparison.

An explicit fiscal Q2 FY2027 is not interchangeable with calendar Q2 2027. Annual values never fill a missing quarter. Financial periods come from source-backed claims/locators and exact duration boundaries, not month-to-quarter guesses. Unqualified years cannot silently cross a calendar/fiscal boundary. A missing answer in reviewed narrative does not mean a metric is absent from the separate history tab.

site/engine.mjs implements the portable gate with precomputed metric identities exported by Python. Seventy-seven browser-engine/DOM tests cover the fifty frozen bilingual acceptance cases, new numerical rejection/positive cases, citation coverage, scenario math and all principal UI interactions. These are reproducible integrity checks, not general natural-language or factual-truth guarantees.

## Build and run

Python 3.11+, Node.js 20+ and the Python dependencies are required. JavaScript dependencies are development-only; the delivered desk runs without third-party JavaScript packages or API keys.

    python -m pip install -r requirements.txt
    npm ci --ignore-scripts
    npm run build
    npm test
    python -m http.server --directory dist 8766

The build validates research review bindings before exporting. data/desk.json and dist/ are generated outputs. The published package contains a fallback snapshot and fetches a newer snapshot from the public automation/research-data branch. If the remote read fails, it labels the saved copy with its date. Opening the page is not the unattended updater.

CSS supports mobile widths and right-to-left Hebrew. Source URLs are rendered as safe HTTPS links using DOM text nodes. Tests exercise actual data and DOM interactions. Browser screenshot QA was unavailable in this environment; no screenshot verification is claimed.

## Remaining substantive research work

- Read and resolve the durable disclosure backlog, starting with financial results and material events. See P0_REVIEW.md for the first source-review pass.
- Resolve the 109 stored normalization QA flags before treating all history as comparable model inputs: share splits, AVAV revisions, RTX presentation differences, Oracle fiscal identity, debt and missing concepts.
- Deepen company-specific moat, unit economics, management incentives, customer concentration and measurable thesis-breaker analysis. Existing source-backed narrative is useful but not a complete investment memo.
- Add independently written holdout questions and review answers with a human before expanding coverage or replacing the bounded engine.
- Add consensus or forward valuation only when a permitted, dated source is connected. The current sensitivity tool does not supply these.

