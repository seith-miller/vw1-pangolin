# 004 — Two-Person Crew

**Status:** Accepted
**Date:** 2026-04-13
**Revised:** 2026-04-13

## Context
Modern aircraft operate with a single pilot thanks to consolidated controls, fly-by-wire, and automation. The same principles can apply to ground vehicles. However, ground vehicles deploy for days/weeks vs. aircraft sorties of 2-6 hours.

Earlier iteration considered 3 crew for watch rotation, but the vehicle was sized down for urban agility. Three crew doesn't package well in the compact form factor.

## Decision
Two-person crew. Both stations identical — either can drive, fight, and command. Vehicle must be fully operable by a single person.

## Research Considered
- 24 hours without sleep: ~25-30% performance decline
- 48 hours sustained ops: significant degradation in surveillance and driving (1971 Army study)
- Crew fatigue is the primary argument for more crew (watch rotation)

## Rationale
- Compact vehicle footprint drives crew count down
- Two identical stations provide redundancy — either crew member can take over any role
- Single-operator capability enables degraded operations and future autonomy path
- Sustained operations handled by crew rotation at the unit level
- AI/autonomy assists crew but does not replace them

## Consequences
- Both stations need full drive-by-wire, weapons, and C2 interfaces
- HMI must be designed so one person can manage all systems under load
- Higher dependency on unit-level rotation planning
- Simplified training — both crew members train on the same station
