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
