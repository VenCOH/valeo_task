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
    fields = ["Timestamp", "FrameID", "Speed", "YawRate", "Signal1", "Signal2"]
    data = []

    # Timestamp in microseconds
    Timestamp = 100_000_000.0
    time_increment = 27_700.0
    time_variation = 50.0
    precision = 6

    first_frame = 100
    last_frame = 2000

    # Speed variables (in km/h)
    Speed = 60.0
    speed_increment = 0.08
    speed_variation = 0.05
    speed_limit = 120.0
    speed_limit_reached = False

    # Yaw rate in in deg/s
    YawRate = 0.0

    Signal1 = 0
    Signal2 = 0

    for FrameID in range(first_frame, last_frame + 1):
        # store current data
        data.append((round(Timestamp, precision), FrameID, Speed, YawRate, Signal1, Signal2))

        # Timestamp update
        Timestamp += float_variation(time_increment, time_variation)

        # Speed update
        if speed_limit_reached:
            Speed = float_variation(speed_limit, speed_variation)
        else:
            Speed += speed_increment
            if Speed >= speed_limit:
                speed_limit_reached = True

        # YawRate update
        YawRate = random.random()
        if random.random() < 0.5:
            YawRate = -YawRate

        # Signal1 callculation
        if FrameID == 200:
            Signal1 = random.randint(1,15)
        
        # Signal2 callculation
        if Signal1 < 5:
            Signal2 = 0
        else:
            Signal2 = 80 + random.randint(-10,10)

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
