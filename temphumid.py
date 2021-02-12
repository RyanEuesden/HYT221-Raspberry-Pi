# HYT221 Inital State Script

#import necessary modules
import smbus
import time
import csv
import os.path
from ISStreamer.Streamer import Streamer

# --------- User Settings ---------
BUCKET_NAME = "Humidity Monitor"
BUCKET_KEY = "temp1"
ACCESS_KEY = "inset_access_key_here"
MINUTES_BETWEEN_READS = 0.1
# ---------------------------------

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
		

def get_temperature:()
	 # Get I2C bus
                bus = smbus.SMBus(1)
                address = 0x28
		delay = 50.0 / 1000.0 

                # Initialise
                void = bus.write_byte(address, 0x00)

                time.sleep(delay)

                # HYT221 address, 0x28(40)
                # Read data back from 0x00(00), 4 bytes
                # Humidity MSB, Humidity LSB, Temp MSB, Temp LSB
                data = bus.read_i2c_block_data(address, 0x00, 4)

                # Read data bytes and convert to decimal
                cTemp = ((data[2] * 0x100 + (data[3] & 0xFC)) >> 2) * (165 / 16383.0) - 40
		return cTemp

def get_humidity:()
	 # Get I2C bus
                bus = smbus.SMBus(1)
                address = 0x28
		delay = 50.0 / 1000.0 

                # Initialise
                void = bus.write_byte(address, 0x00)

                time.sleep(delay)

                # HYT221 address, 0x28(40)
                # Read data back from 0x00(00), 4 bytes
                # Humidity MSB, Humidity LSB, Temp MSB, Temp LSB
                data = bus.read_i2c_block_data(address, 0x00, 4)

                # Read data bytes and convert to decimal
                humidity = ((data[0] & 0x3F) * 0x100 + data[1]) * (100 / 16383.0)
		return humidity 
                
def main:()

	while True:
		
		cTemp = get_temperature()
		humidity = get_humidity()
               

		# Send data to initial state server
                streamer.log("Temperature(C)", cTemp)
                streamer.log("Humidity (RH)", humidity)
                streamer.flush()
                time.sleep(60 * MINUTES_BETWEEN_READS)

if __name__ == '__main__':
	main()

