from src.controller.test_runner import TestRunner
from src.framework.test_case import TestCase


def main():
    test_case = TestCase()
    runner = TestRunner(test_case)
    runner.run()


if __name__ == '__main__':
    main()
