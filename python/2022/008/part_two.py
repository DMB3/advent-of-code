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

        highest_scenic_score = 0
        for y in range(len(trees)):
            for x in range(len(trees[y])):
                trees[y][x].check_scenic_score()
                highest_scenic_score = max(highest_scenic_score, trees[y][x].scenic_score)

        print(highest_scenic_score)
