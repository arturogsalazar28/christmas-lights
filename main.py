from hardware import RelayBoard
from hardware import close
import csv

with open('/home/pi/christmas-lights/schedule.csv') as song:
    song_array = []

    bitStampArrayRows = csv.reader(song)
    for row in bitStampArrayRows:
        if len(row) != 0 and row[0][0] != '#':
            song_array.append([row[0], float(row[1])])

    firstSong = RelayBoard(song_array, True)
    try:
        firstSong.run_relays()
        close()
    except:
        close()
