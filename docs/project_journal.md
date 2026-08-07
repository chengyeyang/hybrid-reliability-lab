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
- [ ] Modify `main.py` as the application entry point
- [ ] Create `src/controller/test_runner.py`
- [ ] Implement the `TestRunner` class
- [ ] Add the `run()` method
- [ ] Connect `main.py` to `TestRunner`
- [ ] Verify the basic execution flow


