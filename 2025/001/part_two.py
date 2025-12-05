import common

class Dial(object):
    def __init__(self, initial_value = 50, minimum_value = 0, maximum_value = 99):
        self.value = initial_value
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.zero_count = 0

    def __rotate_left(self):
        self.value -= 1
        if self.value < self.minimum_value:
            self.value = self.maximum_value

        if self.value == 0:
            self.zero_count += 1

    def __rotate_right(self):
        self.value += 1
        if self.value > self.maximum_value:
            self.value = self.minimum_value

        if self.value == 0:
            self.zero_count += 1

    def rotate(self, direction, times):
        if direction == 'L':
            for n in range(times):
                self.__rotate_left()
        elif direction == 'R':
            for n in range(times):
                self.__rotate_right()

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        dial = Dial()

        with open(input_file) as fin:
            for line in fin.readlines():
                direction, amount = line[0], int(line[1:].strip())
                dial.rotate(direction, amount)

        print(dial.zero_count)
