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

---

## 2026-08-15

### Decision 8: Separate the Device Contract from the Real Device Implementation

Reason:

The original Device abstraction also contained dependencies on Communication, Hardware, and Sensor, which tied the 
abstraction to the real hardware implementation. Separating Device from RealDevice allows Device to define only the 
common contract, while RealDevice implements that contract using the real hardware components.

### Decision 9: Use an Abstract Base Class to Define the Device Contract

Reason:

An abstract base class explicitly defines the operations required by the framework and prevents incomplete concrete 
device implementations from being instantiated. Each concrete device implementation must provide connect(), move(), 
read(), stop(), and disconnect().

### Decision 10: Keep the Device Contract Limited to Current Requirements

Reason:

The framework cannot predict the capabilities required by every future hardware device. The initial Device contract 
therefore defines only the operations required by the current project instead of attempting to create a universal 
hardware interface. The contract can evolve when new requirements are introduced.

--- 

## 2026-08-17

### Decision 11: VirtualDevice Implements the Existing Device Contract

Reason:

VirtualDevice should be interchangeable with RealDevice from the test framework's perspective. Reusing the existing
Device contract allows TestRunner, TestSequence, and TestCase to work with VirtualDevice without introducing
virtual-specific execution logic. This keeps the framework independent from concrete device implementations and
allows virtual tests to run without Communication, Hardware, or Sensor dependencies.

### Decision 12: Use DeviceError for Device-Level Operation Failures

Reason:

Invalid device operations should be represented at the Device abstraction layer instead of coupling concrete device
implementations to the framework-level ExecutionError. Both RealDevice and VirtualDevice may encounter device-level
operation failures, so DeviceError provides a shared abstraction for these failures. More specific device error types
can be introduced later if different handling behavior becomes necessary.

---

## 2026-08-18

### Decision 13: Separate Simulated Measurement from Movement State

Reason:

VirtualDevice measurement should represent the simulated sensor or environmental condition rather than the device's
movement state. Moving or stopping the device should therefore not directly change the measurement. This keeps
different device states independent and allows test scenarios to control simulated measurements explicitly through
VirtualDevice without coupling sensor behavior to movement behavior.

### Decision 14: Keep Simulation Controls Outside the Device Contract

Reason:

Simulation controls such as `set_measurement()` and `set_connection_failure()` are specific to VirtualDevice and are
not operations that every Device implementation should provide. Keeping these controls outside the Device contract
allows tests to configure deterministic virtual scenarios without requiring RealDevice or the test framework to
implement or depend on simulation-specific behavior.

---

## 2026-08-19

### Decision 15: Return Execution Results Through the Execution Hierarchy

Reason:

Execution results should be returned through the same hierarchy that manages test execution rather than stored as
persistent state in TestSequence. TestCase returns an individual Result, TestSequence collects and returns the Results
from the current execution, and TestRunner returns them to its caller. This keeps execution results scoped to a single
run, avoids accumulating results across repeated executions, and allows callers to obtain results without depending on
TestSequence's internal state.

### Decision 16: Configure VirtualDevice Scenarios Outside the Test Framework

Reason:

VirtualDevice scenarios should be configured before framework execution by setup or composition code rather than by
TestRunner, TestSequence, or TestCase. This prevents the test framework from depending on VirtualDevice-specific
controls such as `set_measurement()` and keeps framework components dependent only on the Device contract. As a result,
different simulated scenarios can be configured without introducing simulation-specific behavior into the execution
framework.

--- 

## 2026-08-20

### Decision 17: Keep Logging Outside the Test Execution Framework

Reason:

Test results should be logged outside the test execution framework using the results returned by TestRunner rather than
by TestRunner, TestSequence, or TestCase. This keeps logging responsibilities separate from test execution and prevents
framework components from depending on logging-specific behavior. As a result, completed test results can be consumed by
the Logger or future data-processing components without expanding the responsibilities of the execution framework.

---

## 2026-08-22

### Decision 18: Represent Completed Test Data with Immutable TestRecord Objects

Reason:

Completed test execution data should be represented by immutable TestRecord objects rather than by mutable execution-time
Result objects. Result remains responsible for carrying test outcome data through the execution flow, while TestRecord
represents the completed state of one test execution after that data crosses into the data layer. Keeping TestRecord
immutable preserves the recorded execution state and prevents downstream processing from modifying historical test data.


### Decision 19: Keep TestRecord in an Independent Data Layer

Reason:

TestRecord should belong to an independent data layer rather than the test execution framework or Logger implementation.
This keeps the standardized test record representation separate from both execution behavior and logging behavior. As a
result, future components such as CSV export, reporting, analysis, and visualization can consume TestRecord objects without
depending on TestCase, TestSequence, TestRunner, or Logger-specific implementation details.


### Decision 20: Keep TestRecord Independent from Result

Reason:

TestRecord should receive completed test data values rather than depend directly on the Result type. Conversion from Result
to TestRecord is performed at the logging and data boundary, allowing Result to remain an execution-layer representation
while TestRecord remains a data-layer representation. This reduces coupling between the execution and data layers and
allows TestRecord to be created or consumed independently from the test execution framework.

