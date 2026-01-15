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

# from the full bank, keep the lexicographically largest 12-digit subsequence
def calculate_joltage(battery_bank):
    digits = [ch for ch in battery_bank if ch.isdigit()]
    target_len = 12
    stack = []
    total = len(digits)

    for idx, ch in enumerate(digits):
        remaining = total - idx
        while (
            stack
            and stack[-1] < ch
            and (len(stack) - 1 + remaining) >= target_len
        ):
            stack.pop()
        if len(stack) < target_len:
            stack.append(ch)

    joltage = "".join(stack)
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
