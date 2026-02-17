class DrivingMode:
    def drive(self):
        pass
class EcoMode(DrivingMode):
    def drive(self):
        print("Driving in ECO mode: Saving fuel, smooth acceleration.")
class SportMode(DrivingMode):
    def drive(self):
        print("Driving in SPORT mode: Fast acceleration, high performance.")
class AutonomousMode(DrivingMode):
    def drive(self):
        print("Driving in AUTONOMOUS mode: Self-driving activated.")
class Vehicle:
    def __init__(self, mode: DrivingMode):
        self.mode = mode

    def set_mode(self, mode: DrivingMode):
        self.mode = mode

    def drive(self):
        self.mode.drive()
vehicle = Vehicle(EcoMode())
vehicle.drive()
vehicle.set_mode(SportMode())
vehicle.drive()
vehicle.set_mode(AutonomousMode())
vehicle.drive()
