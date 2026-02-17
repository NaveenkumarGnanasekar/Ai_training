class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def interpret_data(self, raw_data):
        pass

    def report(self, raw_data):
        interpreted = self.interpret_data(raw_data)
        return {
            "Sensor ID": self.sensor_id,
            "Type": self.__class__.__name__,
            "Value": interpreted
        }
class TemperatureSensor(Sensor):
    def interpret_data(self, raw_data):
        return raw_data * 0.1  
class HumiditySensor(Sensor):
    def interpret_data(self, raw_data):
        return (raw_data / 1023) * 100
class PressureSensor(Sensor):
    def interpret_data(self, raw_data):
        return raw_data + 100 
temp_sensor = TemperatureSensor("T1")
humidity_sensor = HumiditySensor("H1")
pressure_sensor = PressureSensor("P1")
sensors = [temp_sensor, humidity_sensor, pressure_sensor]
raw_values = [250, 500, 30]
for sensor, value in zip(sensors, raw_values):
    report = sensor.report(value)
    print(report)
