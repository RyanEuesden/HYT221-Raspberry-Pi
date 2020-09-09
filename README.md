# HYT221 Raspberry-Pi Initial State Tutorial
This is a guide for setting up a temperature and humidity logger that streams the data to initial state using a HYT-221 temperature and humidity sensor.
## Materials
* Raspberry Pi (incluing power supply and microSD card for software image)
* HYT-221 temperature and humidity sensor ([Datasheet](http://www.ist-ag-japan.com/brand2/pdf/HYT-221.pdf))
* Jump cables
## Method
### Setting Up Raspberry Pi w/ Initial State
* Install software image on to SD and setup RPi ([instructions here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md))
* Create [Initial State](https://www.initialstate.com/) Account 
* Install Initial state on RPi ([instructions here](https://www.initialstate.com/blog/raspberry-pi-data-logger/))
* Enable I2C bus on RPi ([instructions here](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/#:~:text=Method%201%20%E2%80%93%20Using%20%E2%80%9CRaspi%2Dconfig%E2%80%9D%20on%20Command%20Line&text=Highlight%20the%20%E2%80%9CI2C%E2%80%9D%20option%20and,activate%20%E2%80%9C%E2%80%9D.&text=The%20Raspberry%20Pi%20will%20reboot%20and%20the%20interface%20will%20be%20enabled.))
### Wiring the Sensor
The sensor has four pins, SDA, SCL, VCC and GND. These need to be wired to the corresponding GPIO pins on the Raspberry Pi:

<p>
  <kbd><img src="/Images/HYT-221Pins.png" alt="Pinout" width="600" /></kbd>
  <em>HYT-221 Pinout</em>
</p>

<p>
  <kbd><img src="/Images/piwiringdiagram.png" alt="RpiScheme" width="600" /></kbd>
  <em>Pi Wiring Diagram</em>
</p>



### Setting up the Script

To download the python code to your raspberry pi go to the terminal and in your desired destination directory type:
```
sudo git clone https://github.com/RyanCafc/HYT221-Raspberry-Pi.git
```

To edit the Initial State settings change to the HYT221-Raspberry-Pi directory (with `cd HYT221-Raspberry-Pi`) and type:
```
sudo nano temphumid.py
```

Here is where your Initial State access key is added and any user settings that you wish to alter can be changed within the following lines of code:

```Python
# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Humidity Monitor" #Can be changed
BUCKET_NAME = "Humidity Monitor" #Can be changed
BUCKET_KEY = "temphum1"
ACCESS_KEY = "INSERT_ACCESS_TOKEN_HERE"
MINUTES_BETWEEN_READS = 0.1
# ---------------------------------
```
Once the file is edited with your access key press ctrl-O to save and ctrl-x to exit the editor.

To test the code is working type:

```
python temphumid.py
```

and check your Initial State dashboard to confirm receipt of data.

Once this has been confirmed, to run the script automatically on startup type:

```
crontab -e
```
and input the following line at the end of the file:

```
@reboot python /path/to/file/temphumid.py
```
For example if the github repositry was cloned to your user's home directory this would be:
```
@reboot python ~/HYT221-Raspberry-Pi/temphumid.py
```
Save then reboot using `sudo reboot` and the script should start automatically on startup.

