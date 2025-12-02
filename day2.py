def get_invalid_ids(start, end):
    invalid_ids = []
    for i in range(start, end + 1):
        if check_repetitions_part2(i):
            invalid_ids.append(i)
    return invalid_ids

def check_two_digits(number):
    num = str(number)
    length = len(num)

    if length % 2 != 0:
        return False

    half = length // 2
    first_half = num[:half]
    second_half = num[half:]
    return int(first_half) == int(second_half)

def check_repetitions_part2(number):
    num = str(number)
    length = len(num)
    for i in range(length):
        appearances = num.count(num[:i])
        if appearances >= 2:
            return True
    return False

def main():
    total = 0
    try:
        with open("./day2.txt", 'r') as file:
            for line in file:
               ids = line.split(',')
               for id in ids:
                   if not id.strip():
                       continue
                   start, end = id.split('-')
                   print(start, end)
                   invalid = get_invalid_ids(int(start), int(end))
                   total += sum(invalid)

    except FileNotFoundError:
        print("File for day 1 not found")

    print(f"Final counter value is: {total}")

if __name__ == '__main__':
    main()