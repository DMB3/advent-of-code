import re

import common


def valid_byr(value):
    try:
        return 1920 <= int(value) <= 2002
    except ValueError:
        return False


def valid_iyr(value):
    try:
        return 2010 <= int(value) <= 2020
    except ValueError:
        return False


def valid_eyr(value):
    try:
        return 2020 <= int(value) <= 2030
    except ValueError:
        return False


def valid_hgt(value):
    try:
        if value.endswith('cm'):
            return 150 <= int(value[:-2]) <= 193
        elif value.endswith('in'):
            return 59 <= int(value[:-2]) <= 76
    except ValueError:
        return False

    return False


def valid_hcl(value):
    try:
        return re.match(r'^#[0-9a-f]{6}$', value)
    except ValueError:
        return False


def valid_ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid_pid(value):
    try:
        return len(value) == 9 and int(value) >= 0
    except ValueError:
        return False

def valid_cid(_):
    return True

def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    validations = {
        "byr": valid_byr,
        "iyr": valid_iyr,
        "eyr": valid_eyr,
        "hgt": valid_hgt,
        "hcl": valid_hcl,
        "ecl": valid_ecl,
        "pid": valid_pid,
        "cid": valid_cid,
    }

    parts = passport.split(" ")
    for part in parts:
        part = part.strip()
        if len(part) == 0:
            continue

        field, value = part.split(":")
        if field in validations and validations[field](value):
            required_fields.remove(field.strip().lower())

    if len(required_fields) == 0 or required_fields == ["cid"]:
        return True

    return False


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
