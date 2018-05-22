
"""
Lidar
"""
import sys
import time
import numpy as np


class RPLidar():
    def __init__(self, port='/dev/ttyUSB0'):
        from rplidar import RPLidar
        self.port = port
        self.frame = np.zeros(shape=365)
        self.lidar = RPLidar(self.port)
        self.lidar.clear_input()
        time.sleep(1)
        self.on = True
       # self.lidar.stop()
       # self.lidar.disconnect()

    def update(self):
        self.measurements = self.lidar.iter_measurments(500)
        for new_scan, quality, angle, distance in self.measurements:
            #angle = int(angle)
            distance =int(distance)
            #self.frame[angle] = 2*distance/3 + self.frame[angle]/3
            #self.frame[10]=self.frame[angle]
            #self.frame = self.frame/10
            #self.frame[distance]=np.mean(distance)
            self.frame=distance

            #self.frame=np.mean(self.frame)
            if not self.on:
                break

    def run_threaded(self):
        return self.frame

    def shutdown(self):
        # indicate that the thread should be stopped
        self.on = False
        time.sleep(.5)
        print('stopping Lidar')
        self.lidar.stop()
        self.lidar.stop_motor()
        self.lidar.disconnect()

        # time.sleep(.5)


class stop_vehicle():

    def __init__(self):

        self.on=True

    def run(self,mode,angle,throttle,rp):
        import donkeycar as dk
        V = dk.vehicle.Vehicle()
        print(rp)
        self.angle = angle
        self.throttle = throttle

        if mode == 'local_angle' and rp>= 100 and rp<=300:
            print('Too close!')
            #self.on=False
            #self.throttle = 350
            V.shutdown()

            #time.sleep(5000)
        else:
            self.throttle = self.throttle

        return self.angle, self.throttle


    '''def run_threaded(self):
        #print(mode)
        return self.on

    def shutdown(self):
        # indicate that the thread should be stopped
        self.on = False
        time.sleep(.5)
        #print('Too close!')'''
