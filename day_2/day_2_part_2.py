def parse_file(input_file):
    file = open("input.txt", "r").readlines()
    data = file[0].split(",")
    return data

def is_valid_id(id):
    id_str = str(id)
    n = len(id_str)
    # invalid if the string is a repeated prefix with no gaps (at least 2 repeats)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            chunk = id_str[:size]
            repeats = n // size
            if repeats >= 2 and chunk * repeats == id_str:
                return False
    return True


def check_ids(data):
    invalid_ids = []
    id_range = []
    for id_range_str in data:
        id_range = id_range_str.split("-")
        start = int(id_range[0])
        end = int(id_range[1])
        for id in range(start, end + 1):
                if not is_valid_id(id):
                    invalid_ids.append(id)
    return invalid_ids
        
        

def validate_ids(input):
    data = parse_file(input)
    invalid_ids = check_ids(data)
    print(f"Found {len(invalid_ids)} invalid IDs: {invalid_ids}")
    invalid_sum = sum(invalid_ids)
    print(f"Sum of invalid IDs: {invalid_sum}")


if __name__ == "__main__":
    validate_ids("input.txt")
