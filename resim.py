#!/bin/python3

import csv
import sys

def read_csv(filename: str):
    fields = []
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        fields = next(reader)
        data = list(reader)

    return fields, data

# Calculates speed values, and creates output file
# Expects input files in correct format
def generate_csv(f_cam_filename: str, sensor_filename: str, out_filename: str):
    f_cam_fields, f_cam_data = read_csv(f_cam_filename)
    sensor_fields, sensor_data = read_csv(sensor_filename)

    sensor_index = 0

    out_data = []
    for Timestamp, FrameID, Speed, YawRate, Signal1, Signal2 in f_cam_data:
        while float(sensor_data[sensor_index][0]) <= float(Timestamp):
            sensor_index += 1
        
        out_speed = (float(Speed) + float(sensor_data[sensor_index-1][1]))/2

        out_data.append((Timestamp, FrameID, out_speed, YawRate, Signal1, Signal2))
    
    with open(out_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(f_cam_fields)
        writer.writerows(out_data)

def main():
    # arguments: f_cam filename, sensor filename, output filename
    if len(sys.argv) < 4:
        raise RuntimeError("not all filenames were specified")
    
    generate_csv(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__=="__main__":
    main()
