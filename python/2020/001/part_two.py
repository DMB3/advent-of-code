import common

if __name__ == "__main__":
    for input_file in common.inputs:
        entries = []

        for line in common.read_file(input_file):
            line_value = int(line)
            entries.append(line_value)

        done = False
        for n_1 in range(len(entries)):
            if done:
                break

            entry_1 = entries[n_1]

            for n_2 in range(n_1, len(entries)):
                if done:
                    break

                entry_2 = entries[n_2]

                for n_3 in range(n_2, len(entries)):
                    entry_3 = entries[n_3]

                    if entry_1 + entry_2 + entry_3 == 2020:
                        print(entry_1 * entry_2 * entry_3)
                        done = True
                        break
