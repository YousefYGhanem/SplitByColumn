import os
from os.path import exists

if __name__ == '__main__':
    # reading the data file
    data = open("datafile.csv", 'r')
    next(data)

    while 1:
        # Asking user for the column number
        inp = input("Please enter the Column Number: ")
        if inp.isdigit():
            col_num = int(inp)
        else:
            print("invalid input!")
            continue

        # checking if column number is valid
        if 0 > col_num or col_num > 5:
            print("invalid input!")
            continue
        else:
            # creating a directory if it doesn't exist
            directory = 'column_' + str(col_num)
            if not exists(directory):
                os.mkdir(directory)

            # reading the file line by line
            for line in data.readlines():
                # ignoring empty lines
                if line == "\n":
                    continue
                # splitting the line into an array
                line_split = line.split(',')
                # checking for any empty values and replacing it be 'NA'
                empty = 0
                if '' in line_split:
                    empty = 1
                    line_split[line_split.index('')] = 'NA'

                # for removing \n from the last column
                col = line_split[col_num - 1].strip()

                # file name of the specified column
                filename = directory + '/file_' + str(col) + '.csv'

                # creating the line in new shape
                if empty == 1:
                    new_line = line_split[0]
                    for i in range(1, 5):
                        new_line += ',' + line_split[i]
                else:
                    new_line = line

                # checking for duplicate lines
                flag = 0
                if exists(filename):
                    with open(filename, 'r') as file:
                        if new_line in file:
                            flag = 1
                if flag == 0:
                    # adding line to specified file for column
                    with open(filename, 'a') as file:
                        file.write(new_line)

        break
    # end of program
    print("all done!")
