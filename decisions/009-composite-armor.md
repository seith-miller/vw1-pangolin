# 009 — Composite Armor

**Status:** Accepted
**Date:** 2026-04-13

## Context
For 14.5mm all-around protection on a vehicle with ~28 m² of exterior surface:
- Steel armor: ~125 kg/m² → ~3,500 kg total
- Composite armor: ~20-31 kg/m² → ~560-870 kg total

Steel armor alone would add more weight than the entire rest of the vehicle, pushing it toward 7,500+ kg and stressing off-the-shelf drivetrain components.

## Decision
Use composite armor for all protection. Estimated armor weight: ~800 kg.

## Rationale
- Keeps total vehicle weight in the ~4,800 kg range
- Allows use of off-the-shelf drivetrain components (Dana 70 axles, Allison 3000, Cummins ISB 6.7)
- Aligns with the ballistics simulation and evolutionary optimization tooling — composite layups are the optimization target

## Consequences
- Armor layup must be engineered, not bought — drives simulation and material library priorities
- Higher unit cost than steel armor
- Composite optimization becomes critical to vehicle performance
