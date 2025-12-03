import sys

from day1 import Day1
from day2 import Day2
from day3 import Day3


def run_solver(day_num, part):
    SOLVERS = {
        1: Day1,
        2: Day2,
        3: Day3,
    }

    if day_num in SOLVERS:
        SolverClass = SOLVERS[day_num]
        challenge = SolverClass()
        challenge.run(part)
    else:
        print(f"🚫 Error: Challenge for Day {day_num} not implemented.")
        print(f"Available days: {list(SOLVERS.keys())}")

def main():
    if len(sys.argv) < 2:
        print("\nWelcome to the Advent of Code 2025 Solver!")
        day_input = input("Enter the Day number you want to run (e.g., 1 or 2): ")
        part = input("Which part of the problem you want to solve?: ")
        try:
            day_num = int(day_input)
            part = int(part)
            run_solver(day_num, part)
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        try:
            day_num = int(sys.argv[1])
            run_solver(day_num)
        except ValueError:
            print("Invalid command line argument. Please provide a number for the day.")


if __name__ == '__main__':
    main()