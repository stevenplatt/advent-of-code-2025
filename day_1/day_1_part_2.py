import math

def turn(pos, delta, size):
    return (pos + delta) % size

def count_crossings(start_pos, delta, size):
    if delta == 0:
        return 0
    if delta > 0:  # right / clockwise
        first = size - start_pos if start_pos != 0 else size
        if delta < first:
            return 0
        return 1 + (delta - first) // size
    else:  # left / counterclockwise
        delta = -delta
        first = start_pos if start_pos != 0 else size
        if delta < first:
            return 0
        return 1 + (delta - first) // size
    

def unlock(dial_size = 100, pos = 50, zero_count = 0):
    file = open("input.txt", "r").readlines()
    for line in file:
        line = line.strip()
        start_pos = pos
        delta = int(line[1:])
        if line[0] == "R":
            zero_count += count_crossings(start_pos, delta, dial_size)
            pos = turn(pos, delta, dial_size)
        elif line[0] == "L":
            zero_count += count_crossings(start_pos, -delta, dial_size)
            pos = turn(pos, -delta, dial_size)

    print (zero_count)

unlock()


