import neopixel,machine,time

pin=machine.Pin(16,machine.Pin.OUT)
np=neopixel.NeoPixel(pin,10)

def startnp():
    for i in range(10):
        np[i]=(80,80,80)
        np.write()
        time.sleep_ms(60)       
                                                                                     
def endnp():
    for i in range(9,-1,-1):
        np[i]=(0,0,0)
        np.write()
        time.sleep_ms(60)
    
            
