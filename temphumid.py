# HYT221 Inital State Script

import smbus
import time

from ISStreamer.Streamer import Streamer

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Humidity Monitor" 
BUCKET_NAME = "Humidity Monitor" 
BUCKET_KEY = "temphum1"
ACCESS_KEY = "INSERT_ACCESS_TOKEN_HERE"
MINUTES_BETWEEN_READS = 0.1
# ---------------------------------

def gethumid():
	# Get I2C bus
	bus = smbus.SMBus(1)

	# HYT221 address, 0x28(40)
	#		0x80(128)	Send normal mode
	bus.write_byte(0x28, 0x80)

	time.sleep(0.5)

	# HYT221 address, 0x28(40)
	# Read data back from 0x00(00), 4 bytes
	# Humidity MSB, Humidity LSB, Temp MSB, Temp LSB
	data = bus.read_i2c_block_data(0x28, 0x00, 4)

	# Convert the data to 14-bits
	humidity = ((data[0] & 0x3F) * 256 + data[1]) * (100 / 16383.0)

	return humidity

def gettemp():
        # Get I2C bus
        bus = smbus.SMBus(1)

        # HYT221 address, 0x28(40)
        #               0x80(128)       Send normal mode
        bus.write_byte(0x28, 0x80)

        time.sleep(0.5)

        # HYT221 address, 0x28(40)
        # Read data back from 0x00(00), 4 bytes
        # Humidity MSB, Humidity LSB, Temp MSB, Temp LSB
        data = bus.read_i2c_block_data(0x28, 0x00, 4)

        # Convert the data to 14-bits
	
	cTemp = ((data[2] * 256 + (data[3] & 0xFC)) / 4) * (165 / 16383.0) - 40

        return cTemp

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
 
	temp_c = gettemp()
	humidity = gethumid()
        streamer.log(SENSOR_LOCATION_NAME + " Temperature(C)", temp_c)
        streamer.log(SENSOR_LOCATION_NAME + " Humidity (RH)", humidity)
        streamer.flush()
        time.sleep(60 * MINUTES_BETWEEN_READS)
