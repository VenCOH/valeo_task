#!/bin/python3

import csv
import random
import sys

def float_variation(value: float, variation: float):
    rn = random.random()
    
    if random.random() < 0.5:
        variation = -variation

    rn *= variation
    
    return value + rn

def generate_csv(filename: str):
    fields = ["Timestamp", "Speed"]
    data = []

    # Timestamp in microseconds
    Timestamp = 100_000_000.0
    time_increment = 200_000.0
    time_variation = 10_000.0
    time_limit = 160_000_000.0
    precision = 6

    # Speed variables (in km/h)
    Speed = 60.0
    speed_increment = 0.56
    speed_variation = 0.1
    speed_limit = 120.0
    speed_limit_reached = False


    while True:
        data.append((round(Timestamp, precision), Speed))

        # Timestamp update
        Timestamp += float_variation(time_increment, time_variation)
        if Timestamp > time_limit:
            break

        # Speed update
        if speed_limit_reached:
            Speed = float_variation(speed_limit, speed_variation)
        else:
            Speed += speed_increment
            if Speed >= speed_limit:
                speed_limit_reached = True

    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(data)

def main():
    # first user argument defines csv filename
    if len(sys.argv) < 2:
        raise RuntimeError("csv filename not specified")

    generate_csv(sys.argv[1])

if __name__=="__main__":
    main()
