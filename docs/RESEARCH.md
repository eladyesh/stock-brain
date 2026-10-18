# Research guide

## Evidence hierarchy

Prefer the company's filings, financial statements, earnings releases, investor materials, and official product or regulatory documentation. Use secondary sources for context and discovery, and label their origin. A search result snippet is not a substitute for reading the underlying evidence.

Record each source in frontmatter with an ID, title, publisher, URL, publication date when known, and access date. Cite that ID next to the supported claim. Use `null` for an unknown publication date, not an invented date. A source publication date, a financial period, an event date, and an access date are different things.

## Writing rules

- Use English throughout the project and retain the common section order.
- Write self-contained paragraphs: name the company and the subject instead of relying on surrounding context.
- Summarize how a business works and why a relationship matters. Avoid marketing copy.
- Separate reported facts, management guidance, external forecasts, and analyst interpretation.
- For every figure, provide period or timestamp, units, currency, accounting basis, and a source.
- Do not mix fiscal and calendar years, quarterly and annual data, GAAP and non-GAAP metrics, or millions and billions without labeling them.
- Record conflicts and explain the chosen interpretation rather than silently discarding contradictory evidence.
- Use `Not available: <reason>` or `Not applicable: <reason>` when a section cannot be completed. Do not turn missing information into zero.
- Cite claims about competitors, customers, suppliers, and product relationships. Shared tags alone do not prove a commercial relationship.

## Review requirements

A reviewed profile must have a valid listing, an identified sector, research and review dates, a source registry, no remaining TODOs, and evidence citations in the business overview and revenue model. Other sections need citations or an explicit `Not available:` / `Not applicable:` explanation. A source registry is not enough on its own: a reviewer must check that each material claim is supported by the cited document.

The validator implements the mechanical requirements. It does not check source availability over the network, investment correctness, factual completeness, classification accuracy, or whether the author performed a genuine review.

## Freshness and updates

Research is a dated snapshot. Review after earnings, filings, guidance changes, major transactions, product or regulatory events, and material thesis changes. There is no background updater or scheduler in this version.

Prices, multiples, leadership roles, catalysts, and estimates age faster than a business description. Keep their individual dates in the text. The exporter carries profile dates; the future answering layer must apply question-specific freshness rules and refuse to imply that an old price or forecast is current.

Use Git history for the audit trail and the profile's change log for the reason a conclusion changed. Do not overwrite an old figure with a new figure while leaving its old date or citation.
