import random
import math
import os

import f_cam, sensor, resim

# test with fixed seed
random.seed(42)

test_files = ("test_files/test_f_cam_out.csv", "test_files/test_sensor_out.csv", "test_files/test_resim_out.csv")
for filename in test_files:
    if os.path.isfile(filename):
        os.remove(filename)

# f_cam tests
def test_f_cam_float_variation():
    for _ in range(100):
        value = float(random.randint(1,10000))/10
        deviation = random.random()

        deviated_value = f_cam.float_variation(value, deviation)
        ht = value + deviation
        lt = value - deviation
        assert(deviated_value < ht or math.isclose(deviated_value, ht))
        assert(deviated_value > lt or math.isclose(deviated_value, lt))

def test_f_cam_file_exists():
    f_cam.generate_csv("test_files/test_f_cam_out.csv")
    try:
        file = open("test_files/test_f_cam_out.csv", "r")
        file.close()
    except FileNotFoundError:
        assert(False)

# sensor tests
def test_sensor_float_variation():
    for _ in range(100):
        value = float(random.randint(1,10000))/10
        deviation = random.random()

        deviated_value = sensor.float_variation(value, deviation)
        ht = value + deviation
        lt = value - deviation
        assert(deviated_value < ht or math.isclose(deviated_value, ht))
        assert(deviated_value > lt or math.isclose(deviated_value, lt))

def test_sensor_file_exists():
    sensor.generate_csv("test_files/test_sensor_out.csv")
    try:
        file = open("test_files/test_sensor_out.csv", "r")
        file.close()
    except FileNotFoundError:
        assert(False)

# resim tests
def test_resim_file_exists():
    f_cam.generate_csv("test_files/test_f_cam_out.csv")
    sensor.generate_csv("test_files/test_sensor_out.csv")
    resim.generate_csv("test_files/test_f_cam_out.csv", "test_files/test_sensor_out.csv", "test_files/test_resim_out.csv")
    try:
        file = open("test_files/test_resim_out.csv", "r")
        file.close()
    except FileNotFoundError:
        assert(False)
