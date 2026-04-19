# 006 — Common Chassis, Modular Weapons

**Status:** Accepted
**Date:** 2026-04-13

## Context
The disaggregated MBT concept requires multiple vehicle variants. Building a unique vehicle for each role is prohibitively expensive and complicates logistics.

## Decision
Single common chassis accepts interchangeable weapon modules/turrets. All variants share the same hull, powertrain, suspension, crew station, and base systems.

## Rationale
- One production line, one training pipeline, one spare parts inventory
- Field maintenance simplified — any mechanic trained on the chassis can work on any variant
- Platoon composition can be tailored to mission by swapping modules
- Damaged vehicles can potentially be re-roled by swapping turrets

## Consequences
- Chassis must accommodate the heaviest and largest weapon module within the 19-tonne envelope
- Turret ring / module interface becomes a critical design constraint
- Structural loads vary significantly between variants (120mm recoil vs. loitering munition launch) — chassis must handle the worst case
