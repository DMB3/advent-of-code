import common

if __name__ == "__main__":
    for input_file in common.inputs:
        trees = []

        y = 0
        for line in common.read_file(input_file):
            row = []
            for x, size in enumerate(line):
                row.append(common.Tree(trees, x, y, int(size)))
            trees.append(row)
            y += 1

        for y in range(len(trees)):
            for x in range(len(trees[y])):
                trees[y][x].check_visibility()

        result = 0
        for row in trees:
            for tree in row:
                if tree.visible:
                    result += 1

        print(result)
