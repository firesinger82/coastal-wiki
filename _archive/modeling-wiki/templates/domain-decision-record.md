# Domain Decision Record

Date:
Project:
Model:
Domain name:
Status: draft / candidate / accepted / rejected

## 1. Purpose

- What is this domain for?
- Tide only, surge, tide-surge, wave coupling, nesting parent, nesting child, or other?
- What is the intended use case?

## 2. Intended Forcings

- Boundary tide source:
- Wind/pressure source:
- Wave source if any:
- River/source terms if any:
- Why these sources were chosen:

## 3. Gate 1: Forcing Coverage

- Coverage check result: pass / review / fail
- Spatial coverage notes:
- Temporal coverage notes:
- Resolution notes:
- Known forcing limitations:
- Evidence files or links:

## 4. Gate 2: Physics Coverage

- Physics coverage result: pass / review / fail
- Processes the domain must preserve:
- Why the chosen patch size is sufficient:
- What would be lost if the domain were smaller:
- Whether parent-child nesting is required:
- Evidence files or links:

## 5. Gate 3: Boundary Bathymetry

- Boundary bathymetry result: pass / review / fail
- Offshore boundary placement rule:
- Minimum boundary depth:
- Maximum boundary depth:
- Boundary slope concerns:
- Shelf-break or endpoint concerns:
- Sponge-layer need and reason:
- Evidence files or links:

## 6. Gate 4: Numerical Survivability

- Survivability result: pass / review / fail
- Short-run setup used:
- DT:
- Ramp:
- Friction assumptions:
- Sponge assumptions:
- Failure symptoms observed:
- Current survivability judgement:
- Evidence files or links:

## 7. Gate 5: Validation

- Validation result: pass / review / fail
- Validation target:
- Metrics used:
- Main errors:
- Bias pattern:
- Current judgement:
- Evidence files or links:

## 8. Decisions

- Final decision:
- Why this domain was accepted or rejected:
- Alternative domains considered:
- Why those alternatives were rejected:

## 9. Fix Classification

- Type A domain geometry fixes applied:
- Type B mesh/bathymetry fixes applied:
- Type C runtime stabilization fixes applied:
- Which fixes are temporary:
- Which fixes are structural:

## 10. Open Risks

- Remaining uncertainty:
- What could still break:
- What must be checked next:

## 11. Required Artifacts

- Mesh file:
- Boundary review artifact:
- Bathymetry check artifact:
- Short-run artifact:
- Validation artifact:

