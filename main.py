##############################################################################
########################## ## AUTOMATIC EJB KODE ## ##########################
########################## ##    ©TotalMK 2021   ## ##########################
##############################################################################

## AUTOMATIC EJB KODE BY TOTALMK - HTTP://WWW.YOUTUBE.COM/TOTALMK
## HOOKS UP TO MORTAL KOMBAT 1/2/3 ARCADE MACHINE BLOCK BUTTONS.         
## PUSHING THE MK1/2/3 BUTTON SENDS THE EJB KODE PRESSES TO THE BUTTONS AUTOMATICLY.
## EACH BUTTON PUSH CYCLE IS 90MS BY DEFAULT I BELIEVE IT MUST BE AROUND 1 SECOND TO WORK.
## GREEN LED SHOW PLAYER 1 BLOCK PUSHES, RED LED SHOW PLAYER 2 BLOCK PUSHES.
## BLUE LEDS SHOW THE OUTPUT TO THE ARCADE BLOCK BUTTONS, THE BLINK RATE IS THE DELAY.
## IF BOARD FREEZES OR LEDS DON'T BLINK, CHECK NO LEADS ARE TOUCHING THEN PUSH RESET BUTTON.
## RECOMMEND ONLY CHANGING KODE IN THE 'USER CONFIGURATION:' SECTION.

## RECCOMEND EXECUTING THE KODE AFTER THE "MIDWAY PRESENTS..." SCREEN, IT SEEMS TO BE MORE EFFECTIVE THAT WAY.
## MK3/UMK3 KODE DOES NOT SEEM TO WORK DURING THE MONTAGE OF GAMEPLAY SCREEN RIGHT BEFORE 'THERE IS NO KNOWLEDGE THAT IS NOT POWER'
## BEST TO DO IT ON THE AMAA SCREEN, TITLE SCREEN OR STANDARD GAMEPLAY SCREENS IN DEMO MODE.

##---------------EJB KODES---------------##
##  BUTTON:[BL : P1|P2|P1|P2|P1|P2|P1|P2]##
## MK GAME:[MK1: 05|10|02|01|02|03|04|  ]##
## MK GAME:[MK2: 05|10|02|08|02|        ]##
## MK GAME:[MK3: 05|10|03|01|02|02|03|04]##

# YOU CAN HOOK UP ANY LEDS OR BUTTONS TO ANY GPIO PIN ON THE PICO, EXCEPT VBUS,VSYS,3.3E,3.3O AND ADC.
# BLUE LEDS ARE NOT IN THE KODE BELOW, AS THEY READ THE ACTUAL POWER SIGNAL FROM THE PIN THAT GOES TO THE BL BUTTONS.
# GREEN/RED LEDS SHOW THE VIRTUAL TIMING FROM THE KODE TO THE BL BUTTONS, THE BLUE LEDS SHOW THE ACTUAL TIMING ON THE OUTPUT.

# HOT TIP! GROUND PINS ON THE PICO HAVE A SQUARE PAD WHICH MAKES THEM EASIER TO ID, ALSO THEY ARE DIRECTLY OPPOSITE EACH OTHER.

#                     RASPBERRY PI PICO
#
#                          USB END
#                      [¯¯¯¯[¯¯¯]¯¯¯¯]
#                     -[GP00     VBUS]-
#                     -[GP01     VSYS]-
#         -------------[GRND     GRND]------------
#                     -[GP02     3.3E]-
#                     -[GP03     3.3O]-
#                     -[GP04      ADC]-
#                     -[GP05     GP28]-
#         -------------[GRND     GRND]------------
#                     -[GP06     GP27]-
#                     -[GP07     GP26]-
#                     -[GP08  RUN/RST]-(RESET SWITCH)
#                     -[GP09     GP22]-
#         -------------[GRND     GRND]------------
#                     -[GP10     GP21]-
#         (MK1 BUTTON)-[GP11     GP20]-
#         (MK2 BUTTON)-[GP12     GP19]-
#         (MK3 BUTTON)-[GP13     GP18]-
#         -------------[GRND     GRND]- (GRND FOR P1/P2 BUTTONS)
#          (GREEN LED)-[GP14     GP17]- (PLAYER 2 BLOCK BUTTON)
#            (RED LED)-[GP15     GP16]- (PLAYER 1 BLOCK BUTTON)
#                      [__[_][_][_]__]
#                          |  |  |_SWIO
#                          |  |_-GND-
#                          |_SWCLK

## Import Classes DO NOT CHANGE!

from machine import Pin, Timer, SPI
from time import sleep_ms, sleep

####################################################################

######################## USER CONFIGURATION ########################

# Button Press Delay (in mili seconds) default = 45
# Example MK1 each press is 45ms * 2 = 90ms by default

mk1delay = 45 # MK1 Time Delay Between Button Push Signals
mk2delay = 45 # MK2 Time Delay Between Button Push Signals
mk3delay = 45 # MK3 Time Delay Between Button Push Signals

# GPIO Buttons (Set Your Buttons Here)

mk1_button = Pin(11, Pin.IN, Pin.PULL_UP) #MK1 BUTTON
mk2_button = Pin(12, Pin.IN, Pin.PULL_UP) #MK2 BUTTON
mk3_button = Pin(13, Pin.IN, Pin.PULL_UP) #MK3 BUTTON

# GPIO Outputs (Set Your BL Outputs Here)

ejbp1bl = Pin(16, Pin.OUT, Pin.PULL_UP) #P1 BLOCK BUTTON
ejbp2bl = Pin(17, Pin.OUT, Pin.PULL_UP) #P2 BLOCK BUTTON
ejbp1bl.value(1)
ejbp2bl.value(1)

# GPIO LEDs (Set Your LEDs Here)

greled = Pin(14, Pin.OUT) #GREEN LED (P1)
redled = Pin(15, Pin.OUT) #RED LED (P2)
greled.value(0)
redled.value(0)

######################## END CONFIGURATION #########################

####################################################################
##DO NOT CHANGE ANYTHING BELOW UNLESS YOU KNOW WHAT YOU ARE DOING!!#

# P1 BL Counter DO NOT CHANGE!

DEFAULT_COUNTER_VALUE = 0
COUNTER_CHANGE = 1
p1bl_value = DEFAULT_COUNTER_VALUE

# P2 BL Counter DO NOT CHANGE!

DEFAULT_COUNTER_VALUE = 0
COUNTER_CHANGE = 1
p2bl_value = DEFAULT_COUNTER_VALUE

while True:

    if mk1_button.value()==0: # MK1 EJB KODE:
        print('')
        print('-----------MK1 EJB KODE-----------')
        for i in range(5):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk1delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk1delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(10):
            ejbp2bl.value(0)
            redled.on()
            sleep_ms(mk1delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk1delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK1 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(2):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk1delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk1delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(1):
            ejbp2bl.value(0)
            redled.on()
            sleep_ms(mk1delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk1delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK1 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(2):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk1delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk1delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(3):
            ejbp2bl.value(0)
            redled.on()
            sleep_ms(mk1delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk1delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK1 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(4):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk1delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk1delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK1 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        print('----------AUTOMATIC EJB-----------')
        print('---------KODE BY TOTALMK----------')
        print('--------YOUTUBE.COM/TOTALMK-------')
            
    if mk2_button.value()==0: # MK2 EJB KODE:
        print('')
        print('-----------MK2 EJB KODE-----------')
        for i in range(5):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk2delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk2delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK2 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(10):
            ejbp2bl.value(0)            
            redled.on()
            sleep_ms(mk2delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk2delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK2 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(2):
            ejbp1bl.value(0)            
            greled.on()
            sleep_ms(mk2delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk2delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK2 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(8):
            ejbp2bl.value(0)            
            redled.on()
            sleep_ms(mk2delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk2delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK2 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(2):
            ejbp1bl.value(0)           
            greled.on()
            sleep_ms(mk2delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk2delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK2 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        print('----------AUTOMATIC EJB-----------')
        print('---------KODE BY TOTALMK----------')
        print('--------YOUTUBE.COM/TOTALMK-------')

    if mk3_button.value()==0: # MK3/UMK3 EJB KODE:
        print('')
        print('-----------MK3 EJB KODE-----------')
        for i in range(5):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk3delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk3delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(10):
            ejbp2bl.value(0)
            redled.on()
            sleep_ms(mk3delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk3delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(3):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk3delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk3delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(1):
            ejbp2bl.value(0)
            redled.on()
            sleep_ms(mk3delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk3delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(2):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk3delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk3delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(2):
            ejbp2bl.value(0)
            redled.on()
            sleep_ms(mk3delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk3delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        for i in range(3):
            ejbp1bl.value(0)
            greled.on()
            sleep_ms(mk3delay)
            ejbp1bl.value(1)
            greled.off()
            sleep_ms(mk3delay)
            p1bl_value = p1bl_value + COUNTER_CHANGE
        print('> P1 MK3 BL Button Pushed {} Times.'.format(p1bl_value))
        p1bl_value = DEFAULT_COUNTER_VALUE
        for i in range(4):
            ejbp2bl.value(0)
            redled.on()
            sleep_ms(mk3delay)
            ejbp2bl.value(1)
            redled.off()
            sleep_ms(mk3delay)
            p2bl_value = p2bl_value + COUNTER_CHANGE
        print('> P2 MK3 BL Button Pushed {} Times.'.format(p2bl_value))
        p2bl_value = DEFAULT_COUNTER_VALUE
        print('----------AUTOMATIC EJB-----------')
        print('---------KODE BY TOTALMK----------')
        print('--------YOUTUBE.COM/TOTALMK-------')

##############################################################################
######################## ## END AUTOMATIC EJB KODE ## ########################
######################## ##      ©TotalMK 2021     ## ########################
##############################################################################
#################################Version 1.0##################################
