import common

if __name__ == "__main__":
    for input_file in common.inputs:
        filesystem = common.Filesystem()
        space_available = 70000000
        target_space = 30000000

        for line in common.read_file(input_file):
            if line.startswith("$"):
                filesystem.execute(line[1:].strip())
            else:
                one, two = line.split(" ")
                if one == "dir":
                    filesystem.current_directory.add_directory(two)
                else:
                    filesystem.current_directory.add_file(two, int(one))

        currently_unused = space_available - filesystem.root.size
        at_least = target_space - currently_unused

        target_directory = None
        for directory in filesystem.directories_bigger_than(at_least):
            if currently_unused + directory.size >= target_space:
                if target_directory is None or directory.size < target_directory.size:
                    target_directory = directory

        print(target_directory, target_directory.size)
