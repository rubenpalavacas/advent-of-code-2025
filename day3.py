from dayX import DayBase

class Day3(DayBase):
    def __init__(self):
        super().__init__(day_number=3)

    def get_joltage_part1(self, bank):
        joltage = 0
        d1 = "0"
        for index, digit in enumerate(bank[:-1], start=0):
            if digit > d1:
                d1 = digit
            digits = d1 + bank[index + 1]
            if int(digits) > joltage:
                joltage = int(digits)

        return int(joltage)

    def get_joltage_part2(self, bank):
        digits = bank[0]
        for index, digit in enumerate(bank[1:],start=1):
            remain = len(bank) - index
            skip_outer = False
            for index2, saved_digit in enumerate(digits, start=0):
                must_remain = 12 - (index2 + 1)
                if remain > must_remain and int(digit) > int(saved_digit):
                    digits = digits[:index2] + digit
                    skip_outer = True
                    break

            if not skip_outer and len(digits) != 12:
                digits = digits + digit

        return int(digits)

    def solve(self, part):
        total = 0
        for bank in self.data:
            if part == 1:
                total += self.get_joltage_part1(bank)
            elif part == 2:
                total += self.get_joltage_part2(bank)

        self.result = total