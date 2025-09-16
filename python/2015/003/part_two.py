import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)

        for line in common.read_file(input_file):
            santa_x, santa_y = (0, 0)
            robot_x, robot_y = (0, 0)

            seen = {(santa_x, santa_y)}
            santa_turn = True
            for instruction in line:
                if instruction == "^":
                    if santa_turn:
                        santa_y += 1
                    else:
                        robot_y += 1
                elif instruction == "v":
                    if santa_turn:
                        santa_y -= 1
                    else:
                        robot_y -= 1
                elif instruction == "<":
                    if santa_turn:
                        santa_x -= 1
                    else:
                        robot_x -= 1
                elif instruction == ">":
                    if santa_turn:
                        santa_x += 1
                    else:
                        robot_x += 1

                seen.add((santa_x, santa_y))
                seen.add((robot_x, robot_y))
                santa_turn = not santa_turn

            print(len(seen))
