# find the highest position in the bank that allows 11 positions behind it
def initial_battery(battery_bank):
    peak_num = 0
    peak_position = 0
    for i in range(len(battery_bank) - 12):
        num = int(battery_bank[i])
        if num > peak_num:
            peak_num = num
            peak_position = i
    return (peak_position)

# from the full bank, keep the 12 highest digits in original order
def calculate_joltage(battery_bank):
    digits = [int(ch) for ch in battery_bank if ch.isdigit()]
    top12 = sorted(digits, reverse=True)[:12]
    counts = {}
    for digit in top12:
        counts[digit] = counts.get(digit, 0) + 1

    joltage_digits = []
    for ch in battery_bank:
        if not ch.isdigit():
            continue
        digit = int(ch)
        if counts.get(digit, 0) > 0:
            joltage_digits.append(ch)
            counts[digit] -= 1

    joltage = "".join(joltage_digits)
    print(f"Battery bank: {battery_bank}, Top 12 peaks: {joltage}")
    return joltage
    

def parse_file(input_file):
    total_joltage = 0
    for line in input_file:
        joltage = calculate_joltage(line.strip())
        total_joltage += int(joltage)
    print(f"Total joltage: {total_joltage}")

if __name__ == "__main__":
    input = open("input.txt", "r").readlines()
    parse_file(input)
