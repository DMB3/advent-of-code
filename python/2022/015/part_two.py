import common


def manhattan_distance(one, two):
    (x0, y0), (x1, y1) = one, two

    return abs(x0 - x1) + abs(y0 - y1)


if __name__ == "__main__":
    TARGET_ROW = {
        "inputs/example_input.txt": 10,
        "inputs/real_input.txt": 2000000
    }
    COORDINATE_LIMITS = {
        "inputs/example_input.txt": 20,
        "inputs/real_input.txt": 4000000
    }

    for input_file in common.inputs:
        print(input_file)

        coordinate_limits = COORDINATE_LIMITS[input_file]
        print("Coordinate limits are", coordinate_limits)

        no_beacon_ys = [[] for _ in range(coordinate_limits + 1)]
        for line in common.read_file(input_file):
            sensor_line, beacon_line = line.split(":")

            sensor_line_x, sensor_line_y = sensor_line.split(",")
            beacon_line_x, beacon_line_y = beacon_line.split(",")

            sensor_x = int(sensor_line_x.split("=")[1])
            sensor_y = int(sensor_line_y.split("=")[1])

            beacon_x = int(beacon_line_x.split("=")[1])
            beacon_y = int(beacon_line_y.split("=")[1])

            distance = manhattan_distance((beacon_x, beacon_y), (sensor_x, sensor_y))
            current_y = 0
            while distance > 0:
                left_x = max(0, sensor_x - distance)
                right_x = min(coordinate_limits, sensor_x + distance)

                if sensor_y - current_y >= 0:
                    no_beacon_ys[sensor_y - current_y].append((left_x, right_x))
                if sensor_y + current_y <= coordinate_limits and current_y > 0:
                    no_beacon_ys[sensor_y + current_y].append((left_x, right_x))

                current_y += 1
                distance -= 1

            for potential_y in range(coordinate_limits + 1):
                potential_xs = no_beacon_ys[potential_y]
                if len(potential_xs) == 0:
                    continue
                potential_xs.sort()

                if potential_xs[0][0] != 0:
                    answer_x = 0
                    break

                last_y = potential_xs[0][1]
                for i in range(1, len(potential_xs)):
                    if last_y >= potential_xs[i][0] - 1:
                        last_y = max(last_y, potential_xs[i][1])
                    else:
                        break

                if last_y != coordinate_limits:
                    answer_x = last_y + 1
                    break

        print(answer_x, potential_y)
        frequency = 4000000 * answer_x + potential_y
        print(frequency)
