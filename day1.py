DIAL = 50
NUMBER_OF_ZEROS = 0

def move_dial(direction, quantity):
    global DIAL, NUMBER_OF_ZEROS

    if direction == 'R':
        NUMBER_OF_ZEROS += get_right_movement_zeros(DIAL, quantity)
        DIAL += quantity

    elif direction == 'L':
        NUMBER_OF_ZEROS += get_left_movement_zeros(DIAL, quantity)
        DIAL -= quantity

    DIAL = DIAL % 100

    ##### PART 1 ZERO COUNTING ######
    #if DIAL == 0:                  #
    #    NUMBER_OF_ZEROS += 1       #
    #################################

def get_right_movement_zeros(dial, quantity):
    return (dial + quantity) // 100

def get_left_movement_zeros(dial, quantity):
    if quantity < dial:
        return 0

    if dial == 0:
        return quantity // 100

    return (quantity - dial) // 100 + 1

def get_movement(line):
    clean = line.strip()
    if len(clean) < 2:
        return None, None

    return clean[0], int(clean[1:])

def main():
    global DIAL, NUMBER_OF_ZEROS
    try:
        with open("./day1.txt", 'r') as file:
            for line in file:
                direction, quantity = get_movement(line)
                if quantity is not None:
                    move_dial(direction, quantity)

    except FileNotFoundError:
        print("File for day 1 not found")

    print(f"Final counter value is: {NUMBER_OF_ZEROS}")

if __name__ == '__main__':
    main()