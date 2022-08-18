import spidev as SPI
import time

bus = 0
device = 0
spi = SPI.SpiDev(bus,device) # spidev0.0
spi.max_speed_hz = 50000000 # 50MHz
spi.mode = 0b00
spi.lsbfirst = False
while True:
    send_data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]

    spi.writebytes(send_data)

    spi.xfer(send_data)

    time.sleep(0.5)