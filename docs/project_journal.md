# Day 1

---

## Summary of Work

> Initialize all related settings and configurations for the projest. Since this is a tedious yet essential process for 
> creating new project, so I document all the steps in detail as below for future reference. The ultimate goal is to 
> make a template based on this project to keep all project unified and save time. Note, this journal will only contain 
> the general steps, for more details, please see the documents in `learning_notes/`.

---

## Project Foundation Setup Steps
1. Create a GitHub repository
2. Set up the virtual environment in PyCharm
3. Initialize Git locally
4. Create the **project structure** and documentation files
5. Configure SSH authentication to link local Git with GitHub
6. Stage, commit, and push the initial commit to GitHub

---

## To-Do List
- [ ] Build a reusable project template based on this when completed

---

# Day 2

---

## Summary of Work

> Break down different functions of a test system into dedicated modules, add them under `src/` and add `__init__.py` 
> files to each module so Python recognizes them as packages. This establishes a clean project structure and allows 
> modules to be imported consistently across the project. Although modern Python can work without `__init__.py` in many 
> cases, including these files improves project organization and follows common Python development practices. Add 
> `config.py`, write `architecture.md` and initialize the `roadmap.md`.

---

## Design Initial System Architecture Steps
1. Create module directory structure under `src/`
2. Add `__init__.py` to each package 
3. Create `config.py`
4. Write initial `architecture.md`
5. Update `roadmap.md`

---

# Day 3

## Summary of Work
> Put hardware, sensors, and communication aside and focus on establishing the initial framework skeleton for the 
> project. Next step will be introducing the communication layer and beginning integrating simulated hardware components
> to complete the framework skeleton.

## Steps
- [x] Modify `main.py` as the application entry point
- [x] Create `src/controller/test_runner.py`
- [x] Implement the `TestRunner` class
- [x] Add the `run()` method
- [x] Connect `main.py` to `TestRunner`
- [x] Verify the basic execution flow

---

# Day 4

## Summary of Work
> Continue from Day 3, complete the framework skeleton by adding the communication, hardware, and sensors modules and 
> integrate them into `test_runner.py`. Focus still only on defining module responsibilities and establishing 
> interactions between components without implementing actual hardware functionality.

## Steps

- [x] Modify `main.py` as the application entry point
- [x] Create `src/communication/communication.py`
- [x] Implement the `Communication` class
- [x] Add `connect()` and `disconnect()` methods
- [x] Create `src/hardware/hardware.py`
- [x] Implement the `Hardware` class
- [x] Add `move()` and `stop()` methods
- [x] Create `src/sensors/sensor.py`
- [x] Implement the `Sensor` class
- [x] Add `read()` method
- [x] Connect `Communication`, `Hardware`, and `Sensor` to `test_runner.py`
- [x] Connect `test_runner.py` to `main.py` 
- [x] Verify the basic execution flow

---

## Day 5

## Summary of Work
> Introduce the first layer of test execution abstraction by separating test execution logic from the TestRunner to 
> allow TestRunner `test_runner.py` to execute different test cases without embedding test-specific logic directly into 
> the controller.

## Steps

- [x] Create TestCase abstraction 
- [x] Implement a simple test case 
- [x] Integrate TestCase with TestRunner 
- [x] Verify test execution flow

--- 

## Day 6

## Summary
> Add a test sequence to make the test case arrangement move flexible instead of hard-coded. The main approach is to 
> evolve the framework from `TestRunner → TestCase` to `TestRunner → TestSequence → TestCase → Result`. And also add 
> test result and basic error handling all together to build the first version of the Test Execution Engine while 
> keeping clear responsibilities and low coupling between the components.

## Steps
- [x] Design and implement TestSequence
- [x] Integrate TestSequence with TestRunner 
- [x] Define and implement Test Result 
- [x] Collect Results in TestSequence 
- [x] Basic Error Handling 
- [x] Integrate Test Execution Flow

--- 

## Day 7

## Summary
> Refine the Test Execution Engine by introducing a `Device` abstraction and improving the error-handling mechanism by
> defining clearer boundaries between test outcomes and execution-level failures. The main approach is to evolve the
> execution flow into `TestRunner → TestSequence → TestCase → Device`, while preserving detailed failure context through
> `Result` and `ExecutionError` before propagating the error. Add automated unit tests with `pytest` to verify the core
> execution flow and document the updated architecture and design decisions.

## Steps

- [x] Introduce Device Abstraction
- [x] Refactor TestCase to Use Device Dependency Injection
- [x] Define Execution Session Lifecycle in TestRunner
- [x] Refine Test-Level and Execution-Level Error Boundaries
- [x] Handle Execution and Cleanup Failures
- [x] Preserve Primary and Cleanup Error Context
- [x] Add Unit Tests for TestCase, TestSequence, and TestRunner
- [x] Update Architecture Documentation
- [x] Update Design Decisions

---

## Day 8

## Summary
> Finalize the Device abstraction by separating the device contract from the real hardware implementation. Define Device 
> as an abstract base class (ABC) and introduce RealDevice as its concrete implementation using Communication, Hardware, 
> and Sensor. Verify that the test framework remains independent of the concrete device implementation while preserving 
> the existing execution behavior. Define the initial VirtualDevice state and behavior requirements in preparation for 
> its implementation.

## Steps
- [x] Review Device responsibilities and abstraction boundary 
- [x] Define the Device contract 
- [x] Introduce Device as an ABC (Abstract Base Class) 
- [x] Separate RealDevice from the Device abstraction 
- [x] Refactor Main to Use RealDevice 
- [x] Verify TestCase independence from concrete Device implementations 
- [x] Review unit Tests for the Device boundary 
- [x] Define initial VirtualDevice state and behavior requirements 
- [x] Run regression tests

---

## Day 9

## Summary
> Implement VirtualDevice as a second concrete implementation of the Device contract. Define its basic connection, 
> movement, measurement, and error behavior to support hardware-independent test execution. Introduce DeviceError to 
> represent device-level operation failures without coupling the Device layer to the framework-level ExecutionError. 
> Add unit tests for VirtualDevice behavior and integrate VirtualDevice with the existing TestRunner, TestSequence, and 
> TestCase without modifying their execution logic. Verify deterministic and repeatable virtual test execution while 
> preserving the existing framework behavior.

## Steps
- [x] Review and finalize VirtualDevice behavior requirements
- [x] Implement VirtualDevice using the existing Device contract
- [x] Add basic connection, movement, and measurement state
- [x] Introduce DeviceError for device-level operation failures
- [x] Implement connect, move, read, stop, and disconnect behavior
- [x] Add unit tests for VirtualDevice behavior
- [x] Verify invalid operations raise DeviceError without unexpected state changes
- [x] Integrate VirtualDevice with the existing test framework
- [x] Verify TestRunner, TestSequence, and TestCase work with VirtualDevice without execution logic changes
- [x] Verify deterministic measurement and test outcome
- [x] Verify repeated virtual executions produce consistent results with independent Result instances
- [x] Run regression tests — 24 tests passed

---

## Day 10

## Summary
> Enhance VirtualDevice with configurable simulated measurement behavior and a controllable connection failure scenario.
> Separate simulated measurement from movement state so sensor behavior can be configured independently from device
> movement. Add VirtualDevice-specific simulation controls without expanding the Device contract, and preserve
> deterministic behavior by explicitly controlling measurement conditions and connection failure state. Extend unit
> tests to verify measurement configuration, invalid input behavior, persistent connection failure, and failure recovery.
> Update existing tests for the intentional default measurement change and verify the complete framework through
> regression testing.

## Steps
- [x] Review and refine the VirtualDevice state model
- [x] Separate simulated measurement from movement state
- [x] Add configurable measurement conditions for cold, medium, and hot scenarios
- [x] Add case-insensitive measurement configuration
- [x] Preserve measurement state when an invalid condition raises DeviceError
- [x] Add controllable connection failure simulation
- [x] Keep simulation-specific controls outside the Device contract
- [x] Implement persistent connection failure behavior
- [x] Verify connection recovery after disabling the simulated failure
- [x] Update existing tests for the intentional default measurement behavior change
- [x] Add unit tests for measurement and connection failure behavior
- [x] Run full regression tests — 32 tests passed

--- 

## Day 11

## Summary
> Integrate VirtualDevice with the complete test execution flow and verify end-to-end behavior through TestRunner,
> TestSequence, and TestCase. Refine result ownership by returning execution results through the execution hierarchy
> instead of storing them as persistent TestSequence state, keeping results scoped to each execution. Preserve the
> framework abstraction boundary by configuring VirtualDevice-specific scenarios outside the test framework. Extend
> integration tests to verify PASS and FAIL scenarios, multiple TestCase execution, independent Result instances,
> deterministic repeated execution, and device cleanup. Update existing tests for the new result-return contract and
> verify the complete framework through regression testing.

## Steps
- [x] Review the framework-to-VirtualDevice integration flow
- [x] Keep VirtualDevice scenario configuration outside the test framework
- [x] Return collected results from TestSequence to its caller
- [x] Propagate execution results through TestRunner
- [x] Remove persistent execution-result state from TestSequence
- [x] Simplify redundant ExecutionError handling in TestSequence
- [x] Update existing tests for the new result-return contract
- [x] Verify end-to-end PASS behavior with VirtualDevice
- [x] Verify end-to-end FAIL behavior with VirtualDevice
- [x] Verify multiple TestCase instances execute in a single TestSequence
- [x] Verify independent Result instances across test executions
- [x] Verify deterministic behavior across repeated VirtualDevice executions
- [x] Verify device cleanup after framework execution
- [x] Update architecture and design decision documentation
- [x] Run full regression tests — 34 tests passed

---

## Day 12

## Summary
> Introduce an initial Logger abstraction for recording completed test result data outside the test execution framework.
> Keep logging responsibilities separate from TestRunner, TestSequence, and TestCase by consuming Results returned to the
> caller after execution. Store independent in-memory snapshots of Result data to preserve test outcome, measurement,
> timing, test name, and error information without depending on a persistent output format. Add unit tests to verify
> complete result logging, multiple-result accumulation, independent result snapshots, and error-result preservation.
> Review the execution-to-logging boundary and verify the complete framework through regression testing.

## Steps
- [x] Review the existing Result structure and execution result flow
- [x] Define the responsibility and boundary of the logging layer
- [x] Keep Logger outside the test execution framework
- [x] Define Logger to record completed Results individually
- [x] Implement in-memory storage for logged result data
- [x] Preserve test name, measurement, outcome, timing, and error information
- [x] Store logged data as an independent snapshot of the original Result
- [x] Verify complete Result data is recorded correctly
- [x] Verify multiple Results accumulate as separate records in insertion order
- [x] Verify logged records remain unchanged when the original Result is modified
- [x] Verify ERROR outcome and error information are preserved
- [x] Review whether execution-to-Logger integration testing adds new coverage
- [x] Keep execution and Logger behavior independently tested without redundant integration coverage
- [x] Run full regression tests — 38 tests passed

---

## Day 13

## Summary
> Introduce a TestRecord data model to represent completed test execution data independently from the execution framework.
> Separate mutable execution-time Result objects from immutable data-layer TestRecord objects, and keep TestRecord in an
> independent data layer for future CSV, reporting, analysis, and visualization components. Refactor Logger to convert
> completed Results into TestRecord instances while preserving test identity, timing, measurement, outcome, and error
> information. Add automated tests to verify TestRecord data preservation, unique record identity, immutability, and
> existing Logger behavior, and verify the complete framework through regression testing.

## Steps
- [x] Review the existing Result and Logger data structures
- [x] Define the responsibility boundary between Result and TestRecord
- [x] Define TestRecord as the data-layer representation of completed test execution data
- [x] Keep TestRecord independent from the execution framework
- [x] Keep TestRecord independent from the Result type
- [x] Define the initial TestRecord schema
- [x] Add unique UUID identity for each TestRecord
- [x] Require completed test data when creating a TestRecord
- [x] Preserve test name, timing, measurement, outcome, and error information
- [x] Keep TestRecord immutable after creation
- [x] Use the existing PASS / FAIL / ERROR outcome representation without adding a separate execution-status field
- [x] Support integer and floating-point measurement values
- [x] Derive TestRecord test scenarios from the defined contract
- [x] Verify TestRecord preserves completed test data
- [x] Verify repeated records receive independent unique identities
- [x] Verify TestRecord data cannot be modified after creation
- [x] Refactor Logger to convert Result objects into TestRecord objects
- [x] Preserve Logger snapshot behavior after the TestRecord refactor
- [x] Preserve multiple-record accumulation and insertion order
- [x] Preserve ERROR outcome and error information through Logger conversion
- [x] Run full regression tests — 41 tests passed

--- 

## Day 14

## Summary
> Introduce CSVExporter to persist completed TestRecord data in a stable CSV representation while keeping CSV persistence
> separate from Logger and the test execution framework. Define explicit serialization rules for record identity, timing,
> duration, measurement, outcome, and error information. Preserve accumulated test history through append-based export,
> write headers only for new or empty files, keep record ordering deterministic, and treat empty record collections as a
> no-op. Add automated tests for single and multiple record export, append behavior, header handling, field serialization,
> empty input, and record ordering, and verify the complete framework through regression testing.

## Steps
- [x] Define the responsibility boundary between Logger and CSVExporter
- [x] Keep CSV persistence separate from the test execution framework
- [x] Introduce CSVExporter for completed TestRecord data
- [x] Define the CSV column schema
- [x] Define explicit TestRecord-to-CSV serialization rules
- [x] Serialize test identifiers as UUID strings
- [x] Serialize timestamps using ISO 8601 format
- [x] Serialize durations as total seconds
- [x] Preserve measurement values in numeric representation
- [x] Serialize missing error values as empty CSV fields
- [x] Export a single TestRecord correctly
- [x] Export multiple TestRecord objects without data loss
- [x] Preserve existing CSV data when exporting additional records
- [x] Write the CSV header only for new or empty files
- [x] Avoid duplicate headers during repeated export
- [x] Treat empty record collections as a no-op
- [x] Preserve input record order during export
- [x] Add automated tests for CSV export behavior
- [x] Refactor repeated CSVExporter test setup while preserving test intent
- [x] Run full regression tests — 48 tests passed

---

# Day 15

## Summary
> Introduce the first reporting layer for completed test data by adding ReportGenerator and TestReport. Keep reporting
> independent from test execution and CSV persistence by generating reports directly from the data-layer TestRecord
> representation. Aggregate test outcomes into execution counts and pass rate, calculate measurement statistics from
> available measurement values, and preserve valid zero measurements while excluding missing values. Include summarized
> failure details for FAIL and ERROR records and reject unsupported outcome values. Separate report calculation from report
> representation so generated report data can be consumed by future visualization and dashboard components. Add automated
> tests for outcome aggregation, empty input, invalid outcomes, measurement statistics, missing measurements, zero-valued
> measurements, and failure details, refactor repeated test setup, and verify the complete framework through regression
> testing.

## Steps
- [x] Define the responsibility boundary of the reporting layer
- [x] Keep reporting independent from the test execution framework
- [x] Use completed TestRecord data as the reporting input
- [x] Introduce TestReport as the structured report data representation
- [x] Introduce ReportGenerator for report calculation
- [x] Separate report calculation from report representation
- [x] Aggregate total, PASS, FAIL, and ERROR test counts
- [x] Calculate pass rate from completed test records
- [x] Represent pass rate as unavailable when no test records exist
- [x] Calculate measurement count, minimum, maximum, and average
- [x] Exclude missing measurements from measurement statistics
- [x] Preserve zero as a valid measurement value
- [x] Represent unavailable measurement statistics explicitly
- [x] Collect summarized failure details for FAIL and ERROR records
- [x] Exclude PASS records from failure details
- [x] Reject unsupported test outcomes with ValueError
- [x] Add automated tests for report generation behavior
- [x] Refactor repeated report test setup while preserving test intent
- [x] Run full regression tests — 55 tests passed

--- 

# Day 16

## Summary
> Introduce the first visualization layer for structured test report data using Matplotlib. Keep visualization focused on
> presentation by consuming TestReport directly without recalculating report statistics or depending on execution and
> persistence representations. Visualize PASS, FAIL, and ERROR distribution as a pie chart and minimum, average, and
> maximum measurement statistics as a bar chart, with measurement count provided as supplementary context. Represent
> empty test and measurement states explicitly to distinguish unavailable data from visualization failures. Return
> generated Figure and Axes objects to the caller instead of controlling display behavior, allowing future dashboard,
> export, and testing use cases to reuse the same visualization functions. Add automated tests for value-to-label mapping,
> zero-valued categories and measurements, and empty-data behavior, add Matplotlib to project dependencies, and verify the
> complete framework through regression testing.

## Steps
- [x] Define the responsibility boundary of the visualization layer
- [x] Use TestReport as the visualization input
- [x] Keep visualization independent from test execution and CSV persistence
- [x] Add Matplotlib as the visualization dependency
- [x] Introduce the report visualization module
- [x] Implement test result distribution as a pie chart
- [x] Implement measurement summary statistics as a bar chart
- [x] Display measurement count as supplementary visualization context
- [x] Keep report calculation outside the visualization layer
- [x] Return Figure and Axes for caller-controlled presentation
- [x] Represent empty test data explicitly
- [x] Represent empty measurement data explicitly
- [x] Add automated tests for visualization value-to-label mapping
- [x] Verify zero-count outcome category behavior
- [x] Verify zero-valued measurement behavior
- [x] Verify empty test and measurement visualization behavior
- [x] Update project dependency requirements
- [x] Run full regression tests — 61 tests passed

---

# Day 17

## Summary
> Introduce the first interactive Dashboard MVP for completed hardware test data using Streamlit. Present overall test
> summary metrics directly from TestReport, reuse the existing outcome and measurement visualization functions, and
> display summarized failure information without duplicating report or visualization logic. Add individual test history
> using completed TestRecord data and provide basic outcome-based filtering while keeping the overall report summary
> unchanged. Separate temporary dashboard sample data from dashboard presentation logic so the sample input can later be
> replaced by the real execution pipeline during end-to-end integration. Extract and test dashboard-specific pure logic
> for pass-rate formatting and history filtering, represent unavailable and empty presentation states explicitly, resolve
> Streamlit and PyArrow compatibility issues through pinned dependencies, and verify the complete framework through
> regression testing.

## Steps
- [x] Define the responsibility boundary of the dashboard layer
- [x] Identify TestReport and TestRecord responsibilities within the dashboard
- [x] Define the minimum Dashboard MVP information layout
- [x] Research Python dashboard technology options
- [x] Select Streamlit for the Dashboard MVP
- [x] Add Streamlit dashboard dependencies
- [x] Create the dashboard module and Streamlit entry point
- [x] Display overall test summary metrics
- [x] Represent unavailable pass rate as user-facing N/A
- [x] Reuse the existing outcome visualization
- [x] Reuse the existing measurement visualization
- [x] Display summarized failure information
- [x] Represent the no-failure state explicitly
- [x] Display individual test history from TestRecord data
- [x] Add outcome-based test history filtering
- [x] Keep history filtering independent from overall report statistics
- [x] Represent empty history and empty filtered-result states explicitly
- [x] Separate temporary dashboard sample data from presentation logic
- [x] Extract dashboard helper logic for filtering and pass-rate formatting
- [x] Add automated tests for dashboard helper behavior
- [x] Preserve zero pass rate separately from unavailable pass rate
- [x] Resolve Streamlit and PyArrow compatibility issues
- [x] Pin compatible dashboard dependency versions
- [x] Run full regression tests — 69 tests passed

---

# Day 18

## Summary
> Integrate the existing execution, logging, persistence, reporting, and dashboard components into the first complete
> end-to-end hardware test data flow. Use the existing `main.py` entry point as the MVP orchestration owner, execute
> deterministic tests through `VirtualDevice`, convert completed execution results into immutable `TestRecord` data, and
> persist records through `CSVExporter`. Add `CSVReader` to restore persisted CSV history into typed `TestRecord` objects
> and replace the dashboard's runtime sample-data dependency with persisted test history. Generate dashboard report
> statistics through the existing `ReportGenerator`, preserve explicit missing and empty presentation states, and keep
> the Streamlit dashboard independent from the test execution lifecycle. Verify PASS and FAIL outcome consistency across
> execution results, records, CSV persistence, reporting, and dashboard presentation. Identify the existing ERROR path as
> an execution-level `ExecutionError` propagation path that does not yet reach persistence or reporting, leaving failure
> integration behavior for the reliability-focused follow-up work. Add CSV round-trip and end-to-end integration tests
> and verify the complete framework through regression testing with 75 passing tests.

## Steps
- [x] Review the existing execution-to-dashboard component boundaries
- [x] Define `main.py` as the top-level MVP orchestration owner
- [x] Keep orchestration separate from component-specific responsibilities
- [x] Replace the main execution path with `VirtualDevice`
- [x] Collect completed results returned by `TestRunner`
- [x] Convert completed results into `TestRecord` data through `Logger`
- [x] Persist completed records to the `output` directory through `CSVExporter`
- [x] Generate a `TestReport` from completed execution records
- [x] Identify persisted CSV data as the runtime boundary between execution and dashboard processes
- [x] Add `CSVReader` for restoring persisted test records
- [x] Restore UUID, datetime, duration, measurement, outcome, and error field types from CSV
- [x] Preserve unavailable measurements separately from valid zero measurements during CSV restoration
- [x] Add CSV export/read round-trip tests
- [x] Verify normal, unavailable, zero, and multiple-record CSV restoration
- [x] Replace the dashboard runtime sample-data dependency with persisted CSV history
- [x] Generate the dashboard `TestReport` from restored historical `TestRecord` data
- [x] Handle missing persisted dashboard data without crashing
- [x] Preserve existing dashboard empty and unavailable presentation states
- [x] Verify PASS outcome consistency across execution, logging, persistence, reporting, and dashboard presentation
- [x] Verify FAIL outcome consistency across execution, logging, persistence, reporting, and dashboard presentation
- [x] Identify execution-level ERROR propagation behavior for follow-up reliability work
- [x] Add end-to-end PASS integration coverage
- [x] Add end-to-end FAIL integration coverage
- [x] Keep dashboard sample data available only for deterministic dashboard tests
- [x] Run full regression tests — 75 tests passed

---

# Day 19

## Summary
> Extend the hardware test framework with deterministic reliability failure simulation and complete the previously
> incomplete ERROR-result data path. Define failure semantics that distinguish startup failures from completed test
> execution errors, stop the remaining test sequence when an individual test encounters an execution-level failure, and
> preserve all completed results including the failed test's ERROR result. Add separate cleanup-error information so
> cleanup failures do not overwrite an already determined PASS or FAIL outcome or replace a primary execution error.
> Extend Result, TestRecord, Logger, CSV export, and CSV restoration to preserve cleanup failure information across the
> data pipeline. Add deterministic movement, read, and stop failure controls to VirtualDevice while keeping simulation
> controls outside the Device contract. Add focused tests for operation failure, cleanup failure, combined primary and
> secondary failures, sequence fail-fast behavior, and an end-to-end ERROR flow through execution, logging, persistence,
> restoration, and reporting. Verify existing PASS and FAIL behavior through full regression testing with 83 passing
> tests.

## Steps
- [x] Review the existing failure and ExecutionError flow
- [x] Distinguish configuration, startup, test execution, and cleanup failures
- [x] Define startup failures as execution-level failures that do not produce TestRecord data
- [x] Define individual test execution errors as completed ERROR results
- [x] Stop the remaining sequence after an individual test execution error
- [x] Preserve completed PASS and FAIL results before an execution error
- [x] Preserve the failed test's ERROR result when stopping the sequence
- [x] Update TestSequence to consume ExecutionError and return completed execution evidence
- [x] Preserve existing PASS or FAIL outcomes when cleanup fails
- [x] Preserve primary execution errors separately from secondary cleanup errors
- [x] Add cleanup_error to Result and TestRecord
- [x] Propagate cleanup-error data through Logger
- [x] Extend CSV persistence with cleanup-error data
- [x] Restore persisted cleanup-error data through CSVReader
- [x] Add deterministic movement failure simulation to VirtualDevice
- [x] Add deterministic read failure simulation to VirtualDevice
- [x] Add deterministic stop failure simulation to VirtualDevice
- [x] Keep reliability simulation controls outside the Device contract
- [x] Verify failed simulated operations do not incorrectly apply successful state transitions
- [x] Add focused VirtualDevice failure-simulation tests
- [x] Add TestCase execution-error handling coverage
- [x] Verify PASS outcome preservation when cleanup fails
- [x] Verify primary and cleanup errors are both preserved when both stages fail
- [x] Add TestSequence fail-fast and result-preservation coverage
- [x] Add end-to-end ERROR integration coverage
- [x] Verify ERROR data through Logger, CSV export, CSV restoration, and ReportGenerator
- [x] Verify existing PASS and FAIL behavior remains unchanged
- [x] Run full regression tests — 83 tests passed

# Day 20

## Summary
> Improve engineering documentation and repository quality for external review. Expand the README to explain the project
> purpose, key capabilities, architecture, execution flow, data pipeline, reliability behavior, device abstraction,
> installation, usage, example output, project structure, and major engineering decisions. Align architecture and design
> documentation with the latest reliability semantics, clarify the RealDevice integration boundary, and add a formal
> testing strategy covering unit, integration, end-to-end, reliability, and data-integrity testing. Remove unused scaffold
> code and tracked runtime artifacts, update ignore rules for generated output and local environments, and validate the
> documented setup through a clean Python 3.11 environment. Complete regression testing with 83 passing automated tests,
> verify the end-to-end application workflow, and confirm the Streamlit dashboard starts successfully from persisted CSV
> test history.

## Steps
- [x] Review the repository from an external-reviewer perspective
- [x] Expand README project overview and key features
- [x] Add architecture and execution-flow documentation to README
- [x] Document the Result-to-TestRecord data pipeline and CSV persistence boundary
- [x] Document reliability and failure-handling semantics
- [x] Explain Device abstraction and VirtualDevice responsibilities
- [x] Add installation and dependency setup instructions
- [x] Document how to run the application, automated tests, and Streamlit dashboard
- [x] Add example test output based on actual generated CSV data
- [x] Add README engineering-decision summaries and documentation links
- [x] Document the current project structure
- [x] Clarify RealDevice as an integration boundary rather than completed physical-hardware I/O
- [x] Update architecture documentation for execution and cleanup failure semantics
- [x] Update design decisions for cleanup-error persistence and sequence-stop behavior
- [x] Add a testing strategy for unit, integration, end-to-end, reliability, and data-integrity coverage
- [x] Verify dependencies in a clean Python 3.11 virtual environment
- [x] Keep the explicit Streamlit-compatible PyArrow dependency after clean-environment verification
- [x] Prefer `python -m pytest` to ensure pytest uses the active Python environment
- [x] Remove unused `analysis` and `utils/config.py` scaffolding
- [x] Remove tracked generated CSV backup data
- [x] Ignore generated `output/`, Python caches, pytest cache, IDE files, and local virtual environments
- [x] Check documentation for stale dates and formatting issues
- [x] Run the complete automated test suite successfully with 83 passing tests
- [x] Verify `python main.py` completes successfully
- [x] Verify the Streamlit dashboard starts successfully from persisted test data

---

# Day 21

## Summary
> Finalize the Hardware Test Automation V1 MVP for portfolio and interview presentation. Revalidate the complete
> end-to-end workflow using Python 3.11, confirm CSV persistence and Streamlit dashboard operation, and complete the final
> automated regression suite with 83 passing tests. Review repository cleanliness and README accuracy from an external
> reviewer perspective, including alignment between documented architecture terminology and the implemented data models.
> Prepare concise explanations of the system architecture, Device abstraction, VirtualDevice simulation, deterministic
> failure handling, FAIL versus ERROR semantics, failure-evidence preservation, execution-to-data boundaries, CSV
> restoration, and the future real-hardware integration path. Develop a portfolio elevator pitch, resume-ready project
> bullets, and an interview story centered on failure propagation, diagnosability, and reliable sequence termination.
> Complete final repository validation and prepare the project for its first V1 MVP milestone release.

## Steps
- [x] Run the final end-to-end application workflow successfully
- [x] Verify generated CSV test data and persistence behavior
- [x] Launch and verify the Streamlit dashboard
- [x] Run the complete automated regression suite with 83 passing tests
- [x] Confirm the final Python 3.11 development environment
- [x] Verify the Git working tree and tracked-file inventory
- [x] Confirm generated runtime output is not tracked by Git
- [x] Run final whitespace and diff validation
- [x] Review the README from a first-time external-reviewer perspective
- [x] Verify README setup, application, test, and dashboard commands
- [x] Verify README claims accurately represent the implemented V1 scope
- [x] Align README architecture terminology with `OneTestRecord` and `OneTestReport`
- [x] Review the high-level execution, persistence, reporting, and presentation architecture
- [x] Prepare a concise architecture walkthrough
- [x] Explain the purpose of the `Device` abstraction
- [x] Explain why `VirtualDevice` enables hardware-independent development
- [x] Explain deterministic failure simulation and its testing value
- [x] Explain the difference between `FAIL` and `ERROR`
- [x] Explain why execution-level errors stop the remaining test sequence
- [x] Explain why failure evidence is preserved before sequence termination
- [x] Explain why primary execution errors and cleanup errors are preserved separately
- [x] Explain the separation between `Result` and `OneTestRecord`
- [x] Explain why persisted CSV data is restored into typed application models before reporting
- [x] Describe the future real-hardware integration path through `RealDevice`
- [x] Clarify that real-hardware integration should primarily extend the device side of the abstraction boundary
- [x] Prepare a concise project elevator pitch
- [x] Prepare resume-ready project bullet candidates
- [x] Prepare an interview story centered on failure propagation and diagnosability
- [x] Perform the final repository validation
- [ ] Commit the final Day 21 changes
- [ ] Create the V1 MVP milestone release / tag
- [ ] Close the Day 21 GitHub issue
