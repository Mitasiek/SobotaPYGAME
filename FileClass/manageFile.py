import csv

class ManageFile:
    def __init__(self):
        pass
    def SaveWorldToFile(self, file, elementToSave):
        with open(file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            for row in elementToSave:
                writer.writerow(row)
    def LoadWorldFromFile(self, file, elementToUpdate):
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x,row in enumerate(reader):
                for y, tile in enumerate(row):
                    elementToUpdate[x][y] = int(tile)

