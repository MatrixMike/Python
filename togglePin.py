import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)

pin.on()

pin.off()
def toggle(p):

   p.value(not p.value())
   
   
while True:

    toggle(pin)

    time.sleep_ms(500)

   
   