import csv
import random
import math

char_name_list = []
temp_counter1 = 0
temp_counter2 = 0
numlist_t1 = []
numlist_t2 = []
num_temp = 0
input_varSTR1 = " "
input_varSTR2 = " "
input_varSTR3 = ' '
input_varINT = 0
characterdict = {}
spldict = {}
atklog = []
splperc = []
atkpreexisting = []
splpreexisting = []


with open('character_name_list.csv', 'r', newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:

        char_name_list.append([row['name'], row['char']])

date = input('Insert date in dd/mm/yyyy format')


def write_to_csv(filename):
    with open(f'{filename}.csv', 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(filename.header)
        csvwriter.writerows(filename.data)


def new_character_csv_files(character):

    tempheader = ['order', 'date', 'atkname', 'dmg_output']

    with open(f'{character}_atklog.csv', 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(tempheader)

    tempheader = ['name', 'count']

    with open(f'{character}_splperc.csv', 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(tempheader)


def open_char_data(character):

    atklog = []
    splperc = []
    atkpreexisting = []
    splpreexisting = []

    with open(f'{character}_atklog.csv', 'r', newline="") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            atklog.append([row['order'], row['date'], row['atkname'], row['dmg_output']])

        for row in atklog:

            atkpreexisting.append([row[0], row[1], row[2], row[3]])

    with open(f'{character}_splperc.csv', 'r', newline="") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            splperc.append([row['name'], row['count']])

        for row in splperc:

            splpreexisting.append([row[0], row[1]])

i = 1
j = 0
while i > 0:

    input_varSTR1 = input('Input character you would like to alter.')
    j = 0

    for entry in char_name_list:

        if input_varSTR1.lower() == entry[0]:
            j = 1
            temp_counter1 = 0

            atklog = []
            splperc = []

            with open(f'{input_varSTR1}_atklog.csv', 'r', newline="") as csvfile:

                reader = csv.DictReader(csvfile)

                for row in reader:
                    atklog.append([row['order'], row['date'], row['atkname'], row['dmg_output']])

            with open(f'{input_varSTR1}_splperc.csv', 'r', newline="") as csvfile:

                reader = csv.DictReader(csvfile)

                for row in reader:

                    splperc.append([row['name'], row['count']])

                for row in splperc:

                    print(row)
                    spldict[row[0]] = int(row[1])

            for key in atklog:

                temp_counter1 += 1

            input_varSTR2 = input('which spell was used? Enter "weapon" if the attack was not from a spell')

            k = 0

            for key in spldict:

                if key == input_varSTR2.lower():

                    spldict[input_varSTR2.lower()] += 1

                    k = 1

            if k == 0:

                spldict[input_varSTR2.lower()] = 1

            splperc = []
            for thing in spldict:
               splperc.append([thing, spldict[thing]])


            input_varSTR3 = input('what was the damage output')

            print(f'atklog:{atklog}')

            atklog.append([temp_counter1 + 1, date, input_varSTR2, input_varSTR3])

            tempheader = ['order', 'date', 'atkname', 'dmg_output']

            with open(f'{input_varSTR1}_atklog.csv', 'w', newline="") as file:

                csvwriter = csv.writer(file)
                csvwriter.writerow(tempheader)

            tempheader = ['name', 'count']

            with open(f'{input_varSTR1}_splperc.csv', 'w', newline="") as file:

                csvwriter = csv.writer(file)
                csvwriter.writerow(tempheader)

    if j == 0:

        input_varSTR2 = input(f'Would you like to make a new profile for the character {input_varSTR1}? (answer with '
                              f'"yes" or "no")')

        match input_varSTR2.lower():

            case 'yes':

                new_character_csv_files(input_varSTR1.lower())
                char_name_list.append([f'{input_varSTR1.lower()}', f'{input_varSTR1.lower()}'])

                with open('character_name_list.csv', 'w', newline="") as file:

                    csvwriter = csv.writer(file)
                    csvwriter.writerow(['name', 'char'])
                    csvwriter.writerows(char_name_list)

            case 'no':
                print('Please input a pre-existing character')

