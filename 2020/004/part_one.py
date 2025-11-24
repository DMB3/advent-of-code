import common


def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    parts = passport.split(" ")
    for part in parts:
        part = part.strip()
        if len(part) == 0:
            continue

        field, value = part.split(":")
        required_fields.remove(field.strip().lower())

    return len(required_fields) == 0 or required_fields == ["cid"]

if __name__ == "__main__":
    for input_file in common.inputs:
        valid_passports = 0
        current_passport = ""
        for line in common.read_file(input_file):
            if line == "":
                if is_valid_passport(current_passport):
                    valid_passports += 1
                current_passport = ""
            else:
                current_passport += line + " "
        if len(current_passport) > 0:
            if is_valid_passport(current_passport):
                valid_passports += 1

        print(input_file, valid_passports)
