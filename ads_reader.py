import Adafruit_ADS1x15
import time

class ADSReader:
    def __init__(self, address, pin, gain):
        self.address = address
        self.pin = pin
        self.gain = gain
        self.adc = Adafruit_ADS1x15.ADS1115(address=self.address, busnum=1)

    def read_analog_input(self):
        '''
        Use appropriate gain for voltage reading
        2/3 = +/-6.144V
        1 = +/-4.096V
        2 = +/-2.048V
        4 = +/-1.024V
        8 = +/-0.512V
        16 = +/-0.256V
        '''
        # Read analog input from specified pin with given gain
        value = self.adc.read_adc(self.pin, gain=self.gain)

        # Calculate voltage based on range and value
        volt_range = 4.096
        #remember 16-bit capabilities 2^16 = 32767
        analog_voltage = value * (volt_range / 32767)

        # Return voltage value
        return analog_voltage

'''
Use this code in the main.py

from ads_reader import ADSReader

# Create an instance of the ADSReader class
address = 0x48
pin = 0
gain = 1
reader = ADSReader(address, pin, gain)

# Read analog input
analog_voltage = reader.read_analog_input()

# Print the result
print(f"Analog voltage: {analog_voltage:.3f}V")

'''