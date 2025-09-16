import common

if __name__ == "__main__":
    for input_file in common.inputs:
        filesystem = common.Filesystem()

        for line in common.read_file(input_file):
            if line.startswith("$"):
                filesystem.execute(line[1:].strip())
            else:
                one, two = line.split(" ")
                if one == "dir":
                    filesystem.current_directory.add_directory(two)
                else:
                    filesystem.current_directory.add_file(two, int(one))

        result = 0
        for directory in filesystem.directories_smaller_than(100000):
            result += directory.size

        print(result)
