import csv

with open("My Spotify Library.csv", "r") as songs_library:
    csv_reader = csv.reader(songs_library)

    with open("tracks.csv", "w") as tracks:
        csv_writer = csv.writer(tracks)

        for line in csv_reader:
            csv_writer.writerow(line)