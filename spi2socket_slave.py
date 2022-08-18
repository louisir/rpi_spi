import spidev as SPI
import time

bus = 0
device = 0
spi = SPI.SpiDev(bus,device) # spidev0.0
spi.max_speed_hz = 50000000 # 50MHz
spi.mode = 0b00
spi.lsbfirst = False
while True:
    print(spi.readbytes(8))
    time.sleep(0.5)