import csv

# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

def GetColumnMappings(spamReader):
    columnNames = {}
    index = 0
    for row in spamReader: #Parse the column names from the first row of the file.
        for columnName in row :
            columnNames[columnName] = index
            index = index + 1
        return columnNames

def GetPositions(csvPortolio):
    positions = OrderedDict()
    with open(csvPortolio, newline='') as csvfile:
        spamReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        columnLookup = GetColumnMappings(spamReader)
        for row in spamReader:
            if (len(row) > columnLookup['Current Value']) and (row[columnLookup['Symbol']] != 'Pending Activity'):
                #lookup = positions[row[columnNumber['Symbol']]]

                if row[columnLookup['Symbol']] in positions:
                    old = positions[row[columnLookup['Symbol']]]
                else:
                    old = 0

                new = row[columnLookup['Current Value']]
                oldDollars = old #int(round(float(old.strip('$'))))
                newDollars = int(round(float(new.strip('$'))))
                positions[row[columnLookup['Symbol']]] = oldDollars + newDollars

    return positions

