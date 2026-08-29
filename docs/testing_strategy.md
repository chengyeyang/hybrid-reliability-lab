# Testing Strategy

## Objective

The testing strategy verifies the hardware test platform at unit, integration, and end-to-end levels. The goal is to
validate individual component behavior while also confirming that execution results and failure evidence remain correct
across the complete test data pipeline.

The test suite is designed around deterministic behavior so that normal execution, test failures, device failures, and
cleanup failures can be reproduced consistently without requiring physical hardware.

## Test Levels

### Unit Tests

Unit tests validate individual components and their local behavior in isolation.

Current unit-level coverage includes:

- Test execution result and test-record data models
- Test-case outcome evaluation
- Test-sequence result collection and stopping behavior
- TestRunner connection and cleanup lifecycle
- VirtualDevice state transitions and deterministic failure scenarios
- Result-to-TestRecord logging
- CSV serialization and restoration
- Report calculation
- Visualization behavior
- Dashboard helper functions

### Integration Tests

Integration tests verify interactions between multiple components and confirm that architectural boundaries behave as
expected.

Important integration scenarios include:

- TestRunner, TestSequence, TestCase, and VirtualDevice execution
- Multiple test cases executed in sequence
- Result propagation through the execution hierarchy
- VirtualDevice failure behavior through the test framework
- Persistence and restoration of completed test records
- Reporting from restored test data

### End-to-End Tests

End-to-end tests validate the complete application data flow from test execution through reporting.

The tested pipeline includes:

```text
VirtualDevice
    ↓
TestCase
    ↓
TestSequence
    ↓
TestRunner
    ↓
Result
    ↓
Logger
    ↓
TestRecord
    ↓
CSVExporter
    ↓
CSVReader
    ↓
ReportGenerator
    ↓
TestReport
```

End-to-end coverage includes normal test execution and reliability failure scenarios where completed execution evidence
must remain available after a failure.

## Reliability Testing

Reliability behavior is tested explicitly because device and cleanup failures can affect both test evidence and the safety
of continued sequence execution.

The test suite verifies the following behaviors:

| Scenario | Expected Behavior |
| --- | --- |
| Normal PASS / FAIL | Preserve the completed result and continue the sequence |
| Device operation failure | Preserve an `ERROR` result and stop the remaining sequence |
| Cleanup failure after PASS / FAIL | Preserve the original outcome, record `cleanup_error`, and stop the sequence |
| Execution failure plus cleanup failure | Preserve the primary execution error and secondary cleanup error |
| Connection / startup failure | Propagate the failure without creating a completed `Result` or `TestRecord` |

`VirtualDevice` provides deterministic failure controls so these scenarios can be reproduced without depending on random
or physical hardware failures.

## Data Integrity Testing

Persistence tests verify that completed test records retain their meaning after serialization and restoration.

The test suite verifies that:

- UUID record identifiers are restored correctly
- Timestamps and durations are restored to their expected types
- Numeric measurements remain numeric after CSV restoration
- Missing measurements remain `None`
- Valid zero measurements are preserved as valid values
- Primary error and cleanup-error information remain separate
- Record order is preserved during export and restoration

## Test Execution

Run the complete automated test suite from the project root:

```bash
python -m pytest
```

Using `python -m pytest` ensures that pytest runs with the Python interpreter from the currently active environment.

The current MVP test suite contains 83 passing automated tests covering unit, integration, and end-to-end behavior.
