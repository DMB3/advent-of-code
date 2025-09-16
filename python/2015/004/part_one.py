import common
import hashlib

if __name__ == "__main__":
    for input_file in common.inputs:
        for line in common.read_file(input_file):
            to_add = 0
            while True:
                md5 = hashlib.md5(("%s%d" % (line, to_add)).encode())
                digested = md5.hexdigest()
                if digested.startswith("00000"):
                    print(line, to_add, digested)
                    break
                to_add += 1
