from hashlib import md5

import common

if __name__ == "__main__":
    for input_file in common.inputs:
        print(input_file)
        password = ""

        for line in common.read_file(input_file):
            test_value = 1
            while True:
                test = line + str(test_value)
                test_md5 = md5(test.encode("utf-8")).hexdigest()

                if test_md5.startswith("00000"):
                    password += test_md5[5]
                    if len(password) == 8:
                        print(password)
                        break

                test_value += 1
