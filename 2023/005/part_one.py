import common


def find_value(key, maps, source_key, destination_key):
    the_map = maps[source_key]

    found = False
    index = 0
    mapped_location = None
    for source_start, length in the_map["sources"]:
        if source_start <= key <= source_start + length:
            # print("\tFound match for", source_key, key)
            mapped_location = (source_start + length) - key
            found = True
            break

        index += 1

    if found:
        mapped_value = the_map["destinations"][index][0] + the_map["destinations"][index][1] - mapped_location
    else:
        mapped_value = key

    # print("\t\tMapped value is", mapped_value)
    if the_map["target"] == destination_key:
        return mapped_value

    return find_value(mapped_value, maps, the_map["target"], destination_key)


if __name__ == "__main__":
    for input_file in common.inputs:
        seed_maps = {}
        seeds = []

        current_first, current_second = None, None

        for line in common.read_file(input_file):
            if len(line) == 0:
                continue

            if line.startswith("seeds: "):
                _, seeds = [x.strip() for x in line.split(":")]
                seeds = [int(x.strip()) for x in seeds.split(" ")]
            elif "map:" in line:
                relation, _ = [x.strip() for x in line.split(" ")]
                current_first, current_second = [x.strip() for x in line.split("-to-")]
                current_second = current_second.split(" ")[0].strip()
                seed_maps[current_first] = {
                    "target": current_second,
                    "sources": [],
                    "destinations": []
                }
            else:
                if current_first is None or current_second is None:
                    raise ValueError("Oops! Parsing is bad :(")
                destination_start, source_start, range_length = [int(x.strip()) for x in line.split(" ")]

                seed_maps[current_first]["destinations"].append((destination_start, range_length))
                seed_maps[current_first]["sources"].append((source_start, range_length))

        min_location = 2e10
        for seed in seeds:
            # print("Checking seed", seed)
            value = find_value(seed, seed_maps, "seed", "location")
            # print("\tLocation for seed", seed, "is", value)
            min_location = min(min_location, value)

        print(input_file, min_location)
