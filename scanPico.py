
# date 15/12/2022
# after lots of editting for unrecognised characters 
import machine
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
 print("no i2c device !")
else:
 print('i2c devices found:', len(devices))

for device in devices:
    print("Decimal address: ", device," | hexa address: ",hex(device))
    
