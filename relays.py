import RPi.GPIO as GPIO
import sys

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
def main(bit_stamp):
    try:
        # Setup GPIO for the relays
        GPIO.cleanup()
    except:
        pass

    try:
        GPIO.setmode(GPIO.BCM)
    except:
        pass

    try:    # Setup all the relays to off
        for relay in relays:
            GPIO.setup(relay, GPIO.OUT)
            GPIO.output(relay, 1)
    except:
        pass


    for relayNumber in range(8):
        if int(bit_stamp[0], 2) & (int('10000000', 2) >> relayNumber):
            GPIO.output(relays[relayNumber], 0)
        else:
            GPIO.output(relays[relayNumber], 1)


if len(sys.argv) != 2:
    print("Usage: python3 relays.py <bitstamp>")
    sys.exit(1)
light_bit_stamp = sys.argv[1]
main(light_bit_stamp)
