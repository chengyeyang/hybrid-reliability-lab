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

## Milestone 3 - Build Test Framework Skeleton 🚧

**Goal:** To create an initial framework skeleton for the testing system by establishing the application's entry point 
(`main.py`) and connect it to the test controller before implementing any actual hardware functionality.

### Tasks
- [ ] Modify `main.py` as the application entry point

- [ ] Create `src/controller/test_runner.py`
- [ ] Implement the `TestRunner` class
- [ ] Add the `run()` method

- [ ] Create `src/communication/communication.py`
- [ ] Implement the `Communication` class
- [ ] Add `connect()` and `disconnect()` methods

- [ ] Create `src/hardware/hardware.py`
- [ ] Implement the `Hardware` class
- [ ] Add `move()` and `stop()` methods

- [ ] Create `src/sensors/sensor.py`
- [ ] Implement the `Sensor` class
- [ ] Add `read()` method

- [ ] Connect `Communication`, `Hardware`, and `Sensor` to `TestRunner`
- [ ] Connect `TestRunner` to `main.py` 
- [ ] Verify the basic execution flow

---

## Milestone 4 - Communication Layer 

**Goal:** Build the communication interface between Python and hardware.

### Tasks

- [ ] Establish the initial framework skeleton
- [ ] Design communication abstraction
- [ ] Implement virtual communication interface
- [ ] Prepare Serial communication structure
- [ ] Support future Arduino integration

---

## Milestone 5 - Hardware Layer

**Goal:** Implement hardware control modules.

### Tasks

- [ ] Create base hardware class
- [ ] Implement virtual servo motor
- [ ] Implement relay simulation
- [ ] Implement power supply simulation
- [ ] Prepare for real hardware support

---

## Milestone 6 - Sensor Layer

**Goal:** Implement sensor interfaces and simulation.

### Tasks

- [ ] Create base sensor class
- [ ] Implement virtual force sensor
- [ ] Implement temperature sensor simulation
- [ ] Prepare camera interface
- [ ] Support future physical sensors

---

## Milestone 7 - Test Automation Framework

**Goal:** Build the automated testing workflow.

### Tasks

- [ ] Create Test Runner
- [ ] Execute automated test cycles
- [ ] Implement configurable test sequences
- [ ] Handle exceptions and error recovery
- [ ] Display test progress

---

## Milestone 8 - Data Logging

**Goal:** Record test results for later analysis.

### Tasks

- [ ] Save CSV files
- [ ] Save JSON configuration
- [ ] Create logging utilities
- [ ] Record timestamps
- [ ] Organize output directories

---

## Milestone 9 - Data Analysis

**Goal:** Analyze collected testing data.

### Tasks

- [ ] Calculate statistics
- [ ] Detect abnormal values
- [ ] Generate summary results
- [ ] Prepare analysis data

---

## Milestone 10 - Dashboard & Visualization

**Goal:** Visualize testing results.

### Tasks

- [ ] Build Streamlit dashboard
- [ ] Display test status
- [ ] Plot measurement charts
- [ ] Display statistics
- [ ] Improve user interface

---

## Milestone 11 - Documentation & Project Polish

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
