import common


def __find_max_with_exclusions(numbers, exclusions):
    search_numbers = numbers.copy()

    while True:
        found = max(search_numbers)
        found_index = search_numbers.index(found)

        if (found, found_index) in exclusions:
            search_numbers[found_index] = -2e10
            continue

        return found, found_index

def largest_joltage(bank, target_length=12):
    generated_code = ""
    integer_bank = [int(b) for b in bank]
    exclusions = []

    while len(generated_code) < target_length:
        maximum_value, index_of_maximum = __find_max_with_exclusions(integer_bank, exclusions)

        generated_length = len(generated_code) + 1

        if generated_length == target_length:
            return int(generated_code + str(maximum_value))

        how_many_needed = target_length - generated_length
        maximum_reach = index_of_maximum + how_many_needed
        if maximum_reach < len(integer_bank):
            generated_code += str(maximum_value)
        else:
            exclusions.append((maximum_value, index_of_maximum))
            continue

        exclusions = []
        integer_bank = integer_bank[(index_of_maximum+1):]

    return int(generated_code)

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        total_output_joltage = 0
        for line in common.read_file(input_file):
            total_output_joltage += largest_joltage(line)

        print(total_output_joltage)
