import f_cam, sensor, resim

def main():
    f_cam.generate_csv("output/f_cam_out.csv")
    sensor.generate_csv("output/sensor_out.csv")
    resim.generate_csv("output/f_cam_out.csv", "output/sensor_out.csv", "output/resim_out.csv")

if __name__=="__main__":
    main()
