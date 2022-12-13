import common


def compare(left, right, indent=0):
    # base_indent = "\t" * indent
    # result_indent = "\t" * (indent + 1)
    # inner_indent = "\t" * (indent + 2)

    # print("%sCompare %s with %s" % (base_indent, left, right))
    for index in range(len(left)):
        if index >= len(right):
            # print("%sRight side ran out of items, so inputs are NOT in the right order" % (result_indent,))
            return False

        left_value, right_value = left[index], right[index]

        if isinstance(left_value, int) and isinstance(right_value, int):
            # print("%sCompare %d vs %d" % (result_indent, left_value, right_value))
            if left_value < right_value:
                # print("%sLeft side is smaller, so inputs are in the right order" % (inner_indent,))
                return True
            elif left_value > right_value:
                # print("%sRight side is smaller, so inputs are NOT in the right order" % (inner_indent,))
                return False
        elif isinstance(left_value, list) and isinstance(right_value, list):
            result = compare(left_value, right_value, indent=indent + 1)
            if result is not None:
                return result
        elif isinstance(left_value, int) and isinstance(right_value, list):
            # print("%sMixed types; convert left and retry comparison" % (result_indent,))
            return compare([left_value], right_value)
        elif isinstance(left_value, list) and isinstance(right_value, int):
            # print("%sMixed types; convert right and retry comparison" % (result_indent,))
            return compare(left_value, [right_value])

    if len(left) < len(right):
        # print("%sLeft side ran out of items, so inputs are in the right order" % (result_indent,))
        return True

    return None


if __name__ == "__main__":
    START_DIVIDER = [[2]]
    END_DIVIDER = [[6]]

    for input_file in common.inputs:
        packets = []
        for line in common.read_file(input_file):
            if line == "":
                continue
            packets.append(eval(line))

        smaller_than_start = 1
        smaller_than_end = 2
        for packet in packets:
            if compare(packet, START_DIVIDER):
                smaller_than_start += 1
                smaller_than_end += 1
            elif compare(packet, END_DIVIDER):
                smaller_than_end += 1

        print(smaller_than_start * smaller_than_end)
