from hardware import RelayBoard
import csv

with open('song.csv') as song:
    bitStampArray = []

    bitStampArrayRows = csv.reader(song)
    for row in bitStampArrayRows:
        bitStampArray.append([row[0], float(row[1])])

    
    firstSong = RelayBoard(bitStampArray, True)
    try:
        firstSong.run_relays()
        firstSong.close()
    except:
        firstSong.close()
