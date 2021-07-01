#!/usr/bin/python

# importing csv module
import csv
import sys
import getopt


def main(argv):
    # csv file name
    filename = ''
    delimiter = input('Delimiter: ')
    fileToWrite = "headers.txt"

    try:
        opts, args = getopt.getopt(
            argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:

        print('csv_extract_headers.py -i <inputfile> -o <outputfile>')

        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('csv_extract_headers.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            filename = arg
        elif opt in ("-o", "--ofile"):
            fileToWrite = arg

    # initializing the titles and rows list
    fields = []
    rows = []

    def formatFields(field):
        return "'"+field+"' => '',"

    # Open function to open the file "MyFile1.txt"
    # (same directory) in append mode and

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        next(csvreader)
        # extracting field names through first row
        fields = next(csvreader)

    with open(fileToWrite, 'w+') as txtFile:

        fieldsToWrite = "\n".join(map(formatFields, fields))

        txtFile.writelines(fieldsToWrite)
    print('Finished, data is ready in the file '+fileToWrite)


if __name__ == "__main__":
    main(sys.argv[1:])
