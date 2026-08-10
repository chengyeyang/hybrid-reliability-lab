# Project Roadmap

> This roadmap outlines the planned development stages for the Hybrid Reliability Lab project.
> It is a living document and will be updated as the project evolves.

---

## Milestone 1 - Project Foundation ✅

**Goal:** Establish a clean development environment and project foundation.

### Tasks

- [x] Create a new GitHub repo for this project
- [x] Configure PyCharm virtual environment 
- [x] Initialize Git repository
- [x] Create project structure
- [x] Create documentation
- [x] Configure SSH authentication to link Git and GitHub

---

## Milestone 2 - System Architecture ✅

**Goal:** Design a scalable software architecture before implementation.

### Tasks
 - [x] Create module directory structure under `src/`
 - [x] Add `__init__.py` to each package
 - [x] Create `config.py`
 - [x] Write initial `architecture.md`
 - [x] Write initial `roadmap.md`

---

## Milestone 3 - Build Test Framework Skeleton ✅

**Goal:** To create an initial framework skeleton for the testing system by establishing the application's entry point 
(`main.py`) and connect it to the test controller (`test_runner.py`) , which orchestrates communication, hardware, and 
sensor modules, before implementing any actual hardware functionality.

### Tasks
- [x] Modify `main.py` as the application entry point

- [x] Create `src/controller/test_runner.py`
- [x] Implement the `TestRunner` class
- [x] Add the `run()` method

- [x] Create `src/communication/communication.py`
- [x] Implement the `Communication` class
- [x] Add `connect()` and `disconnect()` methods

- [x] Create `src/hardware/hardware.py`
- [x] Implement the `Hardware` class
- [x] Add `move()` and `stop()` methods

- [x] Create `src/sensors/sensor.py`
- [x] Implement the `Sensor` class
- [x] Add `read()` method

- [x] Connect `Communication`, `Hardware`, and `Sensor` to `TestRunner`
- [x] Connect `TestRunner` to `main.py` 
- [x] Verify the basic execution flow

---

## Milestone 4 - Test Execution Framework ✅

**Goal:** Build the first layer of the test execution framework by introducing test case abstraction and separating 
test-specific logic from the test controller.

### Tasks
- [x] Create and write test case abstraction `framework/test_case.py`
- [x] Create and implement the logic for `framework/test_sequence.py` to manage the test flow
- [x] Integrate `test_sequence.py` with `test_case.py`
- [x] Integrate `test_runner.py` with `test_sequence.py`
- [x] Create `framework/result.py` and integrate it with test cases
- [x] Implement basic error handling 

---

## Milestone 5 - Communication Layer 🚧

**Goal:** Build the communication interface between Python and hardware.

### Tasks

- [ ] Establish the initial framework skeleton
- [ ] Design communication abstraction
- [ ] Implement virtual communication interface
- [ ] Prepare Serial communication structure
- [ ] Support future Arduino integration

---

## Milestone 6 - Hardware Layer

**Goal:** Implement hardware control modules.

### Tasks

- [ ] Create base hardware class
- [ ] Implement virtual servo motor
- [ ] Implement relay simulation
- [ ] Implement power supply simulation
- [ ] Prepare for real hardware support

---

## Milestone 7 - Sensor Layer

**Goal:** Implement sensor interfaces and simulation.

### Tasks

- [ ] Create base sensor class
- [ ] Implement virtual force sensor
- [ ] Implement temperature sensor simulation
- [ ] Prepare camera interface
- [ ] Support future physical sensors

---

## Milestone 8 - Test Automation Framework

**Goal:** Build the automated testing workflow.

### Tasks

- [ ] Create Test Runner
- [ ] Execute automated test cycles
- [ ] Implement configurable test sequences
- [ ] Handle exceptions and error recovery
- [ ] Display test progress

---

## Milestone 9 - Data Logging

**Goal:** Record test results for later analysis.

### Tasks

- [ ] Save CSV files
- [ ] Save JSON configuration
- [ ] Create logging utilities
- [ ] Record timestamps
- [ ] Organize output directories

---

## Milestone 10 - Data Analysis

**Goal:** Analyze collected testing data.

### Tasks

- [ ] Calculate statistics
- [ ] Detect abnormal values
- [ ] Generate summary results
- [ ] Prepare analysis data

---

## Milestone 11 - Dashboard & Visualization

**Goal:** Visualize testing results.

### Tasks

- [ ] Build Streamlit dashboard
- [ ] Display test status
- [ ] Plot measurement charts
- [ ] Display statistics
- [ ] Improve user interface

---

## Milestone 12 - Documentation & Project Polish

**Goal:** Finalize the project for portfolio presentation.

### Tasks

- [ ] Refactor project structure
- [ ] Improve code readability
- [ ] Complete README
- [ ] Update architecture documentation
- [ ] Add screenshots
- [ ] Prepare portfolio demonstration
- [ ] Final project review

---

# Future Enhancements

Potential features that may be added after the core project is completed.

- Arduino integration
- ESP32 support
- Real force sensor
- Camera inspection
- Database support
- Web API
- Remote monitoring
- Multiple hardware devices
- Continuous Integration (CI)
