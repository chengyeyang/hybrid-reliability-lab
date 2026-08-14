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
