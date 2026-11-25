import machine,time
from startnp import startnp,endnp

snsr_pir=machine.Pin(15,machine.Pin.IN) 
snsr_ldr=machine.ADC(26)


led_on_time=time.ticks_ms()
is_light_on=False

def pir_handler(pin): 
    time.sleep_ms(100)
    global led_on_time
    global is_light_on
    if snsr_ldr.read_u16()>50000 :
        startnp()
        is_light_on=True
        led_on_time=time.ticks_ms()      
        
snsr_pir.irq(trigger=machine.Pin.IRQ_RISING,handler=pir_handler)
 
while True:
    if is_light_on==True:
        if time.ticks_diff(time.ticks_ms(),led_on_time)>60000:
            endnp()
            is_light_on=False
    time.sleep_ms(100)