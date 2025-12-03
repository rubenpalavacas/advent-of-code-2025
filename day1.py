from dayX import DayBase

class Day1(DayBase):
    def __init__(self):
        super().__init__(day_number=1)
        self.DIAL = 50
        self.NUMBER_OF_ZEROS = 0

    def move_dial(self, direction, quantity):
        if direction == 'R':
            self.NUMBER_OF_ZEROS += self.get_right_movement_zeros(self.DIAL, quantity)
            self.DIAL += quantity

        elif direction == 'L':
            self.NUMBER_OF_ZEROS += self.get_left_movement_zeros(self.DIAL, quantity)
            self.DIAL -= quantity

        self.DIAL = self.DIAL % 100

        ##### PART 1 ZERO COUNTING ######
        # if DIAL == 0:                  #
        #    NUMBER_OF_ZEROS += 1       #
        #################################

    def get_right_movement_zeros(self, dial, quantity):
        return (dial + quantity) // 100

    def get_left_movement_zeros(self, dial, quantity):
        if quantity < dial:
            return 0

        if dial == 0:
            return quantity // 100

        return (quantity - dial) // 100 + 1

    def get_movement(self, line):
        clean = line.strip()
        if len(clean) < 2:
            return None, None

        return clean[0], int(clean[1:])

    def solve(self, part):
        for line in self.data:
            direction, quantity = self.get_movement(line)
            if quantity is not None:
                self.move_dial(direction, quantity)

        self.result = self.NUMBER_OF_ZEROS