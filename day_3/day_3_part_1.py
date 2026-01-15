def calculate_joltage(battery_bank):
    peak_num = 0
    peak_position = 0
    second_peak_num = 0
    for i in range(len(battery_bank) - 1):
        num = int(battery_bank[i])
        if num > peak_num:
            peak_num = num
            peak_position = i
    for i in range(len(battery_bank[peak_position + 1:])):
        num = int(battery_bank[peak_position + 1 + i])
        if num > second_peak_num:
            second_peak_num = num
    joltage = str(peak_num) + str(second_peak_num)
    print(f"Battery bank: {battery_bank}, Peak: {peak_num}, Second Peak: {second_peak_num}, Joltage: {joltage}")

    return int(joltage)
    

def parse_file(input_file):
    total_joltage = 0
    for line in input_file:
        joltage = calculate_joltage(line.strip())
        total_joltage += joltage
    print(f"Total joltage: {total_joltage}")

if __name__ == "__main__":
    input = open("input.txt", "r").readlines()
    parse_file(input)