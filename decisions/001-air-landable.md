# 001 — C-130J Air-Landable Constraint

**Status:** Accepted
**Date:** 2026-04-13

## Context
The vehicle must deploy globally across diverse theaters (Europe, Arctic, desert, jungle, Pacific). Strategic mobility is a hard requirement — the vehicle must be transportable by the most common NATO tactical airlifter.

## Decision
Design to fit inside and roll off a C-130J Super Hercules. This sets hard limits:
- **Max width:** 3.12 m
- **Max height:** 2.74 m
- **Max length:** 12.19 m
- **Max combat weight:** 18,955 kg (~19 tonnes)

## Alternatives Considered
- **Air-droppable:** Would reduce max weight further (~18 tonnes) and require drop-hardened structure. Last significant combat airdrop of vehicles was Iraq 2003. Rejected as operationally unnecessary.
- **C-17 only:** Allows heavier/larger vehicle but limits which airfields and nations can deploy it. Rejected — C-130 compatibility maximizes deployability.

## Consequences
- 19-tonne weight cap drives every downstream decision: armor, powertrain, weapon systems
- Vehicle will be lighter than most IFVs and far lighter than MBTs — protection philosophy must compensate
