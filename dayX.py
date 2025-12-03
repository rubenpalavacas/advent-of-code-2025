import os

class DayBase:
    def __init__(self, day_number, file_name=None):
        self.day_number = day_number
        if file_name is None:
            self.file_path = f"./day{day_number}.txt"
        else:
            self.file_path = file_name
        self.data = []
        self.result = None

    def _read_data(self):
        if not os.path.exists(self.file_path):
            print(f"File for day {self.day_number} not found at {self.file_path}")
            return False

        try:
            with open(self.file_path, 'r') as file:
                self.data = [line.strip() for line in file.readlines()]
            return True
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return False

    def solve(self, part):
        raise NotImplementedError("Subclasses must implement the solve() method.")

    def run(self, part):
        print(f"--- Day {self.day_number} ---")
        if self._read_data():
            print(f"Solving for part: {part}")
            self.solve(part)
            if self.result is not None:
                print(f"Solution value is: {self.result}")
            else:
                print("Solve method completed, but no result was stored in self.result.")
        print("-" * (11 + len(str(self.day_number)) * 2))