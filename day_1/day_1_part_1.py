def turn(pos, delta, size):
    return (pos + delta) % size
    

def unlock(dial_size = 100, pos = 50, zero_count = 0):
    file = open("input.txt", "r").readlines()
    for line in file:
        line = line.strip()
        if line[0] == "R":
            pos = turn(pos, int(line[1:]), dial_size)
            if pos == 0:
                zero_count += 1
            
        elif line[0] == "L":
            pos = turn(pos, -int(line[1:]), dial_size)
            if pos == 0:
                zero_count += 1
    print (zero_count)

unlock()


