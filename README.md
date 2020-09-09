# HYT221 Raspberry-Pi Initial State Tutorial
This is a guide for setting up a temperature and humidity logger that streams the data to initial state using a HYT-221 temperature and humidity sensor.
## Materials
* Raspberry Pi (incluing power supply and microSD card for software image)
* HYT-221 temperature and humidity sensor ([Datasheet](http://www.ist-ag-japan.com/brand2/pdf/HYT-221.pdf))
* Jump cables
## Method
### Setting Up Raspberry Pi w/ Initial State
* Install software image on to SD and setup RPi ([instructions here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md))
* Install Initial state on RPi ([instructions here](https://www.initialstate.com/blog/raspberry-pi-data-logger/))
* Enable I2C bus on RPi ([instructions here](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/#:~:text=Method%201%20%E2%80%93%20Using%20%E2%80%9CRaspi%2Dconfig%E2%80%9D%20on%20Command%20Line&text=Highlight%20the%20%E2%80%9CI2C%E2%80%9D%20option%20and,activate%20%E2%80%9C%E2%80%9D.&text=The%20Raspberry%20Pi%20will%20reboot%20and%20the%20interface%20will%20be%20enabled.))
### Wiring the Sensor
The sensor has four pins, SDA, SCL, VCC and GND. These need to be wired to the corresponding GPIO pins on the Raspberry Pi
<img src="/Images/HYT-221Pins.png" alt="drawing" width="400"/>
<img src="/Images/piwiringdiagramhyt.png" alt="drawing" width="400"/>
