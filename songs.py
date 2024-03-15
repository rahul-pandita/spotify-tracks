import csv

with open("tracks.csv", "r") as tracks:
    reader = csv.reader(tracks)

    with open("songs_list.csv", "w") as songs:
        writer = csv.writer(songs, delimiter=",")

        for line in reader:
            try:
                writer.writerow((line[0], line[1], line[2], line[5]))
            except IndexError:
                continue