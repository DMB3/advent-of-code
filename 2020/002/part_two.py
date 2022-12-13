import common

if __name__ == "__main__":
    for input_file in common.inputs:
        valid_passwords = 0

        for line in common.read_file(input_file):
            policy, password = line.split(":")

            positions, character = policy.split(" ")
            p_one, p_two = positions.split("-")

            if (password[int(p_one)] == character) ^ (password[int(p_two)] == character):
                valid_passwords += 1

        print(valid_passwords)
