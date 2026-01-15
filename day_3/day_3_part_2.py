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

# not working correctly yet
# from the peak position (inclusive), loop and remove the lowest digit each time, until 12 digits are left in the joltage
def calculate_joltage(battery_bank, peak_position):
    joltage = battery_bank[peak_position:]
    while len(joltage) > 12:
        

    print (f"Battery bank: {battery_bank}, Top 12 peaks: {joltage}")
    return (joltage)
    

def parse_file(input_file):
    total_joltage = 0
    for line in input_file:
        joltage = calculate_joltage(line.strip())
        total_joltage += joltage
    print(f"Total joltage: {total_joltage}")

if __name__ == "__main__":
    input = open("input.txt", "r").readlines()
    parse_file(input)