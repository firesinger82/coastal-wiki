# ADCIRC Domain Design Process

Date: 2026-04-13

Purpose:
- formalize how ADCIRC model domains should be designed
- replace ad hoc decisions with a defensible process
- define what must be checked before a domain is accepted for meshing and run setup

Core idea:
- the goal is not "standardization first"
- the goal is "formalization first"
- different projects may choose different domains, but they should be chosen through the same decision process

## Problem Statement

The current failure mode is not only technical.

It is process failure:
- domain decisions depend too much on individual memory
- emergency fixes are mixed with actual design choices
- AI suggestions are used tactically, but the decision path is not archived
- each new project reopens the same questions from scratch

So the missing asset is:
- a clear decision process

## Domain Design Questions

Every ADCIRC domain must answer these questions in order:

1. What forcings and boundary data must this domain support?
2. What physical processes must the domain preserve?
3. Where can the offshore boundary be placed without causing obvious numerical damage?
4. Can the resulting mesh survive numerically?
5. Can the resulting setup be validated against observations or accepted references?

If any question is not answered, the domain is not yet ready.

## Five-Gate Process

### Gate 1. Forcing Coverage

Question:
- do the intended data sources actually cover the domain in space, time, and resolution?

Typical sources:
- `NAO99jb`
- `NAO99`
- `FES2022`
- `JMA-MSM`
- `ERA5`
- wave forcing sources if SWAN coupling is intended

Checks:
- horizontal coverage
- coastal coverage quality near the chosen boundary
- time resolution
- update cadence and reproducibility
- datum and variable compatibility

Failure meaning:
- if forcing coverage is weak, the domain may be physically impossible to use even if the mesh is beautiful

### Gate 2. Physics Coverage

Question:
- is the domain large enough to preserve the processes the model is supposed to reproduce?

Typical processes:
- large-scale tide propagation
- shelf resonance
- remote surge propagation
- typhoon wind setup and pressure response
- wave setup if coupled
- harbor-scale trapping only if the larger parent response is already represented elsewhere

Checks:
- is the shelf and offshore fetch large enough?
- is the area too small to support the known regional response?
- are key straits, shelves, and basins truncated too early?
- is parent-child nesting required instead of a small standalone domain?

Failure meaning:
- if physics coverage fails, the model can remain numerically stable and still be physically wrong

### Gate 3. Boundary Bathymetry

Question:
- can the offshore boundary be placed where boundary bathymetry and geometry are numerically safe?

Checks:
- boundary minimum depth
- depth variation along the boundary
- boundary-to-interior slope severity
- proximity to shelf break or coastal complexity
- need for sponge/friction buffering near the boundary
- whether shallow endpoint artifacts exist

Interpretation:
- a boundary that is too shallow or too irregular is a structural risk
- sponge layers can help, but they do not justify a fundamentally bad boundary choice

Failure meaning:
- if this gate fails, the domain geometry itself may need to move

### Gate 4. Numerical Survivability

Question:
- can the model survive with the chosen domain and mesh without exploding?

Checks:
- short-run stability
- ramp behavior
- timestep sensitivity
- friction sensitivity
- sponge behavior
- sensitivity to wet/dry treatment
- boundary-related oscillation or reflection symptoms

Interpretation:
- this is where "model not blowing up" is checked
- but stability is necessary, not sufficient

Failure meaning:
- if the model survives only through extreme patches, the domain design is still suspicious

### Gate 5. Validation

Question:
- can the chosen domain be defended against observations or accepted references?

Checks:
- tide gauges or harmonic stations
- offshore reference fields if available
- comparison against accepted studies or government reports
- constituent-wise metrics
- event-based water-level comparison for surge runs

Interpretation:
- a stable domain without validation is only a candidate

Failure meaning:
- if validation fails, revisit domain size, boundary placement, bathymetry, and forcing assumptions before fine-tuning solver parameters

## Decision Order

The order matters.

Use this sequence:
1. forcing coverage
2. physics coverage
3. boundary bathymetry
4. numerical survivability
5. validation

Do not start with:
- friction tuning
- timestep tweaks
- sponge hacks

unless the earlier gates are already acceptable.

## Allowed Fix Types

When a domain fails, classify the fix.

### Type A. Domain geometry fix

Examples:
- move offshore boundary
- enlarge the basin
- include missing shelf or basin area
- split into parent-child nesting

Meaning:
- structural fix

### Type B. Mesh and bathymetry fix

Examples:
- refine or coarsen resolution zones
- smooth slope
- adjust minimum depth handling
- clean degenerate elements

Meaning:
- representation fix

### Type C. Runtime stabilization fix

Examples:
- change `DT`
- change ramp
- adjust `ESLM`
- adjust friction
- add sponge support

Meaning:
- operational fix

Rule:
- Type C is not allowed to hide a Type A problem

## Minimum Deliverables For Any Domain

Every new domain should leave these artifacts:

1. domain decision record
2. forcing coverage note
3. boundary bathymetry check
4. short-run survivability note
5. validation summary

Without these, the domain is not archived well enough.

## Review Questions

Before a domain is accepted, ask:
- what forcings is this domain explicitly designed for?
- what physical processes is it expected to preserve?
- why is the offshore boundary here and not farther out?
- what evidence says the boundary is deep and smooth enough?
- what evidence says the model survives for the right reasons?
- what evidence says the results are physically believable?

## Working Rule

Use this sentence going forward:
- "A domain is accepted only after it passes the five-gate design process."

Do not use this weaker pattern:
- "The domain looks okay and the run did not crash."
