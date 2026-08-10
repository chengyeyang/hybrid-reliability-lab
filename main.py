from src.controller.test_runner import TestRunner
from src.framework.test_sequence import TestSequence

from src.framework.test_case import TestCase as TC1
from src.framework.test_case2 import TestCase as TC2


def main():
    test_case = TC1()
    test_case2 = TC2()
    test_sequence = TestSequence()
    test_sequence.add(test_case)
    test_sequence.add(test_case2)
    runner = TestRunner(test_sequence)
    runner.run()


if __name__ == '__main__':
    main()
