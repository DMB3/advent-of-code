import common


def manhattan_distance(one, two):
    (x0, y0), (x1, y1) = one, two

    return abs(x0 - x1) + abs(y0 - y1)


if __name__ == "__main__":
    TARGET_ROW = {
        "inputs/example_input.txt": 10,
        "inputs/real_input.txt": 2000000
    }
    for input_file in common.inputs:
        print(input_file)

        target_row = TARGET_ROW[input_file]
        print("Target row is", target_row)

        # these sets will contain both the beacons and all the (in distance) xs at target row
        beacons_at_target_row = set()
        covered_xs_at_target_row = set()

        for line in common.read_file(input_file):
            sensor_line, beacon_line = line.split(":")

            sensor_line_x, sensor_line_y = sensor_line.split(",")
            beacon_line_x, beacon_line_y = beacon_line.split(",")

            sensor_x = int(sensor_line_x.split("=")[1])
            sensor_y = int(sensor_line_y.split("=")[1])

            beacon_x = int(beacon_line_x.split("=")[1])
            beacon_y = int(beacon_line_y.split("=")[1])

            if beacon_y == target_row:
                beacons_at_target_row.add(beacon_x)

            distance = manhattan_distance((beacon_x, beacon_y), (sensor_x, sensor_y))
            distance -= abs(target_row - sensor_y)

            for x in range(sensor_x - distance, sensor_x + distance + 1):
                covered_xs_at_target_row.add(x)

        set_intersection = covered_xs_at_target_row - beacons_at_target_row
        print(len(set_intersection))
