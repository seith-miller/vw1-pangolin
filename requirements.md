# Pangolin — Design Requirements

## Transport Constraint
- Must be air-landable via C-130J Super Hercules
- **Max width:** 3.12 m (10.25 ft)
- **Max height:** 2.74 m (9 ft)
- **Max length:** 12.19 m (40 ft) — excluding ramp
- **Max combat weight:** 18,955 kg (~19 tonnes)

## Service Life
- Initial operating capability: 2030
- Designed relevance through: 2050

## Operating Environment
- Global deployment: European plains, arctic, desert, jungle, Pacific littoral
- Near-peer contested, sensor-saturated battlefield
- Wide frontages, diverse threat spectrum

## Crew
- See [decision 004](decisions/004-crew-size.md)

## Mobility
- Wheeled (weight and logistics driven)
- Top road speed: 110 km/h
- Tactical range: 900 km on a single tank of fuel
- Gradient: 60%
- Side slope: 40%
- Ground clearance: 410 mm (16 in)
- Fording (unprepared): 76 cm (2.5 ft)
- Fording (prepared): 1.5 m (5 ft)
- Operational doctrine: dispersed flocking — spread out, converge to engage, disengage quickly
- Must refuel and repair quickly in the field

## Strategic Mobility
- C-130J air-landable (see Transport Constraint)

## Protection
- **Passive armor:** 14.5mm all-around protection
- **RPG:** proof against RPG threats (passive + active protection mix)
- **Top attack:** strong defense against drones and loitering munitions (passive + active protection mix)
- **Active protection system:** required — specifics TBD

## Concept
- Disaggregated MBT: a platoon of 3-9 vehicles (TBD) on a common chassis replaces the role of a main battle tank
- Frontline fighting vehicle — closes with and engages the enemy
- Common chassis with interchangeable weapon modules/turrets
- Max weapon module weight: 750 kg (installed, including ammo)

## Weapon Module Variants
1. **Autocannon (30mm)** — direct fire, line-of-sight
2. **Mortar (120mm, NEMO-class)** — semi-automatic indirect fire
3. **Anti-aircraft** — air defense
4. **Loitering munition launcher** — 6-12 near-vertical launch tubes (TBD)

## Out of Scope (separate programs)
- Reconnaissance/sensor drone mothership — packaging doesn't suit this chassis
- Electronic warfare/jamming — different operational profile, operates behind the lines

## Software Tooling (Python)

### Terminal Ballistics Simulation
- Model projectile-armor interactions for composite armor optimization
- **Projectile types:** bullets, APFSDS, HEAT, AP, HE, shrapnel
- **Armor materials library:** steels, aluminums, titaniums, ceramics, composites
- **Optimizer:** evolutionary algorithm to find optimal armor layup (layer order, thickness, material per layer)
- **Fitness criteria:** configurable — minimize weight, maximize protection, or weighted tradeoff

### Visualization
- Animated projectile-armor interaction (penetration, deformation, fragmentation)
- Browser-based web app
- Also embedded in Fusion 360 via web view panel

### Fusion 360 Integration
- Vehicle designed in Fusion 360
- Python API extensions for custom tooling
- Embedded visualization panel
