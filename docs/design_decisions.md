# Design Decisions

## 2026-08-06

### Decision 1: Add a dedicated category for single-board controllers

Reason:

To better categorize modules since those single-board controller, such as Arduino, Raspberry Pi, or ESP32, do not 
actually perform as a hardware component nor sensor.

---

## 2026-08-14

### Decision 2: Introduce a Device Abstraction

Reason: 

To provide a unified interface over the lower-level hardware components, allowing the test framework to focus on invoking 
higher-level device operations without depending on implementation details.

### Decision 3: Inject Device Dependencies into Test Cases

Reason: 

To decouple test cases from the construction and implementation of `Device`. This allows the `Device` implementation or 
its dependencies to change without requiring corresponding changes to the test cases.

### Decision 4: Let TestRunner Own the Execution Session Lifecycle

Reason: 

At the current scale of the framework, introducing a dedicated lifecycle manager would add unnecessary complexity. 
`TestRunner` therefore owns the session-level lifecycle, including connecting before test execution and disconnecting 
after execution.

### Decision 5: Separate Test Outcomes from Execution-Level Failures

Reason: 

A valid test outcome may still exist when an execution-level failure occurs. Keeping `Result` and `ExecutionError` 
separate preserves both the test outcome and the execution failure information for better diagnosis.

### Decision 6: Preserve the Primary Error When Cleanup Also Fails

Reason: 

When both primary execution and cleanup fail, the primary error is preserved while the cleanup error is retained as 
additional context. This provides more complete diagnostic information without losing the original cause of the failure.

### Decision 7: Stop the Test Sequence on Execution-Level Failure

Reason: 

An execution-level failure may leave the system in an invalid or unknown state. Continuing to execute the remaining test 
cases could therefore produce unreliable results. The test sequence stops and propagates the failure instead.
