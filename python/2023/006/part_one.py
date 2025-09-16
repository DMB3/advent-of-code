import common

if __name__ == "__main__":
    for input_file in common.inputs:
        with open(input_file, "r") as fin:
            time_line = fin.readline()
            distance_line = fin.readline()

        times = [x.strip() for x in time_line[(time_line.find(":") + 1):].strip().split(" ")]
        times = [int(x) for x in times if x]

        distances = [x.strip() for x in distance_line[(distance_line.find(":") + 1):].strip().split(" ")]
        distances = [int(x) for x in distances if x]

        result = 1
        for n in range(len(times)):
            race_duration = times[n]
            race_record = distances[n]

            # print(race_duration, "ms race with a record of", race_record, "mm")
            winners = []
            for wait_time in range(1, race_duration):
                race_time = race_duration - wait_time
                distance_travelled = wait_time * race_time
                if distance_travelled > race_record:
                    winners.append(distance_travelled)

                # print("\tWaiting", wait_time, "speed will be", wait_time, "mm per ms for", race_time,
                #       "ms, travelling", distance_travelled)

            result *= len(winners)

        print(input_file, result)
