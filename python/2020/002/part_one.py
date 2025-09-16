import common

if __name__ == "__main__":
    for input_file in common.inputs:
        valid_passwords = 0

        for line in common.read_file(input_file):
            policy, password = line.split(":")

            min_max, character = policy.split(" ")
            mini, maxi = min_max.split("-")

            count = password.strip().count(character.strip())
            if int(mini) <= count <= int(maxi):
                valid_passwords += 1

        print(valid_passwords)
