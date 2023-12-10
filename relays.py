import RPi.GPIO as GPIO
from time import sleep

# Pin Setup
# Pin number   WiringPi Pin   BCM Pin  Relay
#       3           8           2       1
#       5           9           3       2
#       7           7           4       3
#       8           15          14      4
#       10          16          15      5
#       12          1           18      6
#       11          0           17      7
#       13          2           27      8

relays = [2, 3, 4, 14, 15, 18, 17, 27]


# Main function for the program
def main(bit_stamp_array):

    GPIO.setwarnings(False)

    try:
        GPIO.cleanup()
    except:
        pass

    # Setup GPIO for the relays
    GPIO.setmode(GPIO.BCM)

    # Setup all the relays to off
    for relay in relays:
        GPIO.setup(relay, GPIO.OUT)
        GPIO.output(relay, 1)

    # Based on the bitStampArray, switch the relays on and off starting with 1
    for bitStamp in bit_stamp_array:
        for relayNumber in range(8):
            if int(bitStamp[0], 2) & (int('10000000', 2) >> relayNumber):
                GPIO.output(relays[relayNumber], 0)
            else:
                GPIO.output(relays[relayNumber], 1)




import sys
if len(sys.argv) != 2:
    print("Usage: python3 relays.py <bitstamp>")
    sys.exit(1)
bit_stamp_array = [sys.argv[1]]
main(bit_stamp_array)
