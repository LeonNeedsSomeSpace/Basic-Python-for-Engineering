#Create a program that regulates rotation of a motor by a certain angle
import time #import the library trhat provides time-related tasks
import platform #import the library that is used to access information about the underlying platform

#Import gpiozero only if running on Raspberry Pi
#Windows PC and Mac do not fall under Raspberry Pi
if platform.system() == "Linux" and "arm" in platform.machine():
    from gpiozero import Servo
    from gpiozero.pins.pigpio import GiGPIOFactory
    USING_RASPBERRY_PI = True
else:
    USING_RASPBERRY_PI = False
    print("Not running on Raspberry Pi. Simulation only.")

#Servo control class that works in both real and simulated environments
class ServoController:
    def __init__ (self, pin=15): #pin=15 tells the servo which GPIO pin to use by default
        if USING_RASPBERRY_PI:
            #Use PiGPIOFactory for better pulse accuracy
            factory = PiGPIOFactory()
            self.servo = Servo(pin, pin_factory=factory) #Create a servo object attached to the specified GPIO pin
        else:
            self.servo = None

#Take a parameter 'position' and define the target positions
    #'self' refers to the current instance of the class.
    # 'self.servo' is an attribute of that class
    def move(self, position: str):
        if USING_RASPBERRY_PI: #Check if Raspberry Pi is being used
            if position == "mid":
                self.servo.mid()
            elif position == "min":
                self.servo.min()
            elif position == "max":
                self.servo.max()
            print(f"Moved servo to: {position}")
        else:
            print(f"[VIRTUAL] Move servo to: {position}") #If no Raspberry Pi, carry out simulation

    #Define a method 'run_demo' which is part of that class
    #This enables the motor to rotate to the different positions that are defined above
    def run_demo(self): #Method defined
        try:
            while True:
                for pos in ["mid", "min", "max"]:
                    self.move(pos) #Calling a method named 'move'
                    time.sleep(1) #1 second interval between movements
        except KeyboardInterrupt:
            print("Program stopped.")


#Check whether the python file is being run as the main program
if __name__ == "__main__":
    controller = ServoController(pin=15)
    controller.run_demo()

