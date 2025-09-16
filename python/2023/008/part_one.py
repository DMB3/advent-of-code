import common

if __name__ == "__main__":
    for input_file in common.inputs:
        movement = None
        nodes = {}

        for line in common.read_file(input_file):
            if movement is None:
                movement = line.strip()
            else:
                if not line:
                    continue

                node, left_right = [x.strip() for x in line.split("=")]
                left, right = [x.strip() for x in left_right.split(",")]
                left, right = left[1:], right[:-1]
                nodes[node] = (left, right)

        current_node = "AAA"
        current_movement_index = 0
        number_of_steps = 0

        while current_node != "ZZZ":
            number_of_steps += 1
            next_move = movement[current_movement_index]

            current_movement_index += 1
            if current_movement_index >= len(movement):
                current_movement_index = 0

            if next_move == "L":
                current_node = nodes[current_node][0]
            elif next_move == "R":
                current_node = nodes[current_node][1]
            else:
                raise ValueError("Unknown next move: %s" % (next_move,))

        print(input_file, number_of_steps)
