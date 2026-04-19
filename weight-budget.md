# Weight Budget

Source of record: [weight-budget.csv](weight-budget.csv)

Open in any spreadsheet tool (Excel, Numbers, Google Sheets) for editing. Commits diff cleanly as text.

## Schema

| Column | Values |
|--------|--------|
| system | Drivetrain, Rolling, Structure, Protection, Weapons, Crew, Consumables, Electronics, Electrical, Environmental, Safety, Ancillary |
| component | Specific item |
| weight_kg | Number |
| confidence | `estimate`, `spec`, `measured` |
| source | Where the number came from |
| notes | Free text |

## Current Totals

Last rolled up 2026-04-13 — will be automated later.

| System | kg |
|--------|-----|
| Drivetrain | 1,301 |
| Rolling | 510 |
| Structure | 400 |
| Protection | 1,130 |
| Weapons | 750 |
| Crew | 200 |
| Consumables | 150 |
| Electronics | 150 |
| Electrical | 100 |
| Environmental | 80 |
| Safety | 20 |
| Ancillary | 50 |
| **Total** | **~4,841 kg** |

Well under C-130 max of 19,000 kg. Within off-the-shelf drivetrain ratings.
