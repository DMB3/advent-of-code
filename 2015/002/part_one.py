import common

if __name__ == "__main__":
    for input_file in common.inputs:
        result = 0

        for line in common.read_file(input_file):
            l, w, h = line.split("x")
            l, w, h = int(l), int(w), int(h)

            area = 2 * l * w + 2 * w * h + 2 * h * l
            sides = [w * l, w * h, l * h]

            result += area + min(sides)

        print(result)
