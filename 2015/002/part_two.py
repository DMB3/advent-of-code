import common

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            l, w, h = line.split("x")
            l, w, h = int(l), int(w), int(h)

            volume = l * w * h
            perimeters = [2 * w + 2 * l, 2 * w + 2 * h, 2 * l + 2 * h]

            result += volume + min(perimeters)

        print(result)
