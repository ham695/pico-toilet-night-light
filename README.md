# pico-toilet-night-light
 A smart,non-blocking night light for your bathroom, built with Raspberry Pi Pico and MicroPython
## Why I made this?
 At night , the main bathroom light is too bright . It hurts my eyes . So , I made this light . When you walk in the dark , it lights up . After 60 seconds , it turns off by itself .
## Good code (Not a beginner code )
 I did not use ' time.sleep(60) ' . That will freeze the Pico .
 I used ' IRQ_RISING ' (Hardware Interrupt ) and ' time.ticks_diff ' (Non-blocking timer ) .
## What you need (Hardware)
* Raspberry Pi Pico
* PIR Motion Sensor (HC-SR501)
* LDR (Light Sensor)
* WS2812B LED Strip (10 LEDs）
* Battery box (4x AA)
## How to use?
 1.Save 'startnp.py' and 'main.py' to your Pico
 2.Connect the wires .(PIR to pin15 , LDR to pin26 , LED to pin16)
 3.Turn it on . Done !
## picture
<img width="960" height="1440" alt="toilet-night-light Figure2" src="https://github.com/user-attachments/assets/4aa4c133-1892-4450-abbf-919c2c68d53f" />
<img width="835" height="1249" alt="toilet-night-light Figure1" src="https://github.com/user-attachments/assets/f789ad8f-4b7a-4414-8212-83b4978ed4b3" />
## Contact me
 If you have any questions, please open an " Issue" .or email me . (My English is not very good . I used simple words, Thank you for reading!)
