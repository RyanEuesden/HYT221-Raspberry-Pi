# HYT221 Inital State Script

#import necessary modules
import smbus
import time
import csv
import os.path

# Check if csv log already exists
file_exists = os.path.isfile('/home/pi/Downloads/HYT221-Raspberry-Pi/temphumidrawlog.csv')

#define csv headers
headers = ['Date', 'Time', 'Temperature', 'Humidity']

# Create csv file processing loop (writes headers only if no file created. If file already exists then new data appended to end of existing file
def processing_loop(csvfile):
        csv_writer = csv.writer(csvfile)
        if not file_exists:
                csv_writer.writerow(headers)


        while True:

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
                cTemp = ((data[2] * 0x100 + (data[3] & 0xFC)) >> 2) * (165 / 16383.0) - 40
		
		# Get date and Time
                Date = time.strftime('%d-%m-%Y')
                Time = time.strftime('%H:%M.%S')

                # Write Data to CSV File
		csv_writer.writerow([Date, Time, cTemp, humidity])
                csvfile.flush()

with open ('temphumidrawlog.csv', 'a+') as csvfile:
        processing_loop(csvfile)
