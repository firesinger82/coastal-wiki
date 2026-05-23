# Experiment Protocol

The goal is to produce comparable experiments, not heroic one-off runs.

## Rule 1

Each experiment should answer one specific question.

Bad:
- "make the model better"

Good:
- "does lowering the timestep stabilize the refined coastal boundary segment?"

## Rule 2

Change one primary variable at a time unless the run is explicitly exploratory.

## Rule 3

Always write down the baseline before modifying it.

## Minimum Viable Experiment

Every experiment must define:
- objective
- baseline configuration
- one primary intervention
- success metric
- failure signature
- next decision if the run fails

## Experiment Types

- `diagnostic`: isolate one suspected cause
- `sensitivity`: vary one parameter or one small set
- `stability`: test whether a run remains well-behaved
- `validation`: compare against data or reference behavior
- `performance`: reduce runtime or memory cost

## Before Running

1. Write the experiment card first.
2. Define what counts as success or failure.
3. Save the relevant config names and input paths.
4. Decide what plot, metric, or log will judge the result.

## After Running

1. Record what happened, even if the run failed immediately.
2. Save the first useful diagnostic artifact.
3. State whether the result changes your next decision.
4. Promote only if the lesson looks reusable.
