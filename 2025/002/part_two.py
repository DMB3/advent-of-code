import common

def is_invalid_id(elf_id):
    so_far = ""
    for character in elf_id:
        so_far += character
        cnt = elf_id.count(so_far)
        if cnt >= 2 and elf_id == (so_far*cnt):
            return True
    return False

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        result = 0
        for line in common.read_file(input_file):
            all_ranges = line.split(",")
            for the_range in all_ranges:
                first_id, last_id = the_range.split("-")
                for elf_id in range(int(first_id), int(last_id) + 1):
                    if is_invalid_id(str(elf_id)):
                        result += elf_id

        print(result)
