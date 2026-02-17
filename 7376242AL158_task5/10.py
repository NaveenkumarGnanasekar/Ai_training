class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        print(f"Device {self.device_id} is now ON")

    def turn_off(self):
        self.status = "OFF"
        print(f"Device {self.device_id} is now OFF")

class Light(SmartDevice):
    def turn_on(self):
        self.status = "ON"
        print(f"Light {self.device_id} is shining brightly 💡")

    def turn_off(self):
        self.status = "OFF"
        print(f"Light {self.device_id} is turned off")

class Fan(SmartDevice):
    def turn_on(self):
        self.status = "ON"
        print(f"Fan {self.device_id} is spinning 🌪️")

    def turn_off(self):
        self.status = "OFF"
        print(f"Fan {self.device_id} is stopped")
light1 = Light("L1")
fan1 = Fan("F1")
light1.turn_on()
fan1.turn_on()
light1.turn_off()
fan1.turn_off()
