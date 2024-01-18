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
data = []
dmg = 0
dmg_counter = 0
analysis_char = ''
tempdata = {}

with open('character_name_list.csv', 'r', newline="") as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        char_name_list.append([row['name'], row['char']])
        temp_counter1 += 1

i = 1
while i < temp_counter1:

    with open(f'{char_name_list[i][0]}_atklog.csv', 'r', newline="") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            data.append(row)
    i += 1

input_varSTR1 = input('Do you wish to run quick data analysis? (Type "yes" or "no")')

if input_varSTR1 == 'yes':

    quickdata = {}
    quickdata_output = [['description', 'output']]
    dmg = 0
    dmg_counter = 0
    datelist = []

    for entry in data:

        if entry['date'] not in datelist:

            datelist.append(entry['date'])

    for entry in data:

        dmg += int(entry['dmg_output'])

    quickdata['team totaldmg whole campaign'] = dmg

    dmg = 0
    dmg_counter = 0

    for entry in data:

        dmg += int(entry['dmg_output'])
        dmg_counter += 1

    if dmg_counter != 0:

        quickdata['team avedmg whole campaign'] = dmg/dmg_counter

    else:

        quickdata['team avedmg whole campaign'] = 0

    for entry in quickdata:

        quickdata_output.append([entry, quickdata[entry]])

    quickdata = {}

    dmg = 0
    dmg_counter = 0
    for entry in datelist:

        quickdata[f'{entry} dmg'] = 0
        dmg_counter = 0

        for key in data:

            if key['date'] == entry:

                quickdata[f'{entry} dmg'] += int(key['dmg_output'])
                dmg_counter += 1

        tempdata[entry] = dmg_counter

    for entry in datelist:

        if tempdata[entry] != 0:

            quickdata[f'{entry} avedmg'] = quickdata[f'{entry} dmg']/tempdata[entry]

        else:

            quickdata[f'{entry} avedmg'] = 0

    for entry in quickdata:

        quickdata_output.append([entry, quickdata[entry]])

    quickdata = {}
    tempdata = {}

    for char in char_name_list:

        if char[0] != 'name':

            data = []
            quickdata_output.append([f'{char[0]} data starts here', 0])

            with open(f'{char[0]}_atklog.csv', 'r', newline="") as csvfile:

                reader = csv.DictReader(csvfile)

                for row in reader:

                    data.append(row)

            dmg = 0
            dmg_counter = 0

            for entry in data:

                dmg += int(entry['dmg_output'])

            quickdata[f'{char[0]} totaldmg whole campaign'] = dmg

            dmg = 0
            dmg_counter = 0

            for entry in data:

                dmg += int(entry['dmg_output'])
                dmg_counter += 1

            if dmg_counter != 0:

                quickdata[f'{char[0]} avedmg whole campaign'] = dmg / dmg_counter

            else:

                quickdata[f'{char[0]} avedmg whole campaign'] = 0

            for entry in quickdata:

                quickdata_output.append([entry, quickdata[entry]])

            quickdata = {}

            dmg = 0
            dmg_counter = 0
            temp_counter1 = 0
            temp_counter2 = 0

            for entry in datelist:

                quickdata[f'{char[0]} {entry} dmg'] = 0
                dmg_counter = 0

                for key in data:

                    if key['date'] == entry:

                        quickdata[f'{char[0]} {entry} dmg'] += int(key['dmg_output'])
                        dmg_counter += 1

                tempdata[entry] = dmg_counter

                temp_counter1 += 1

            for entry in quickdata:

                quickdata_output.append([entry, quickdata[entry]])

            for entry in datelist:

                if tempdata[entry] != 0:

                    quickdata[f'{char[0]} {entry} avedmg'] = quickdata[f'{char[0]} {entry} dmg'] / tempdata[entry]

                else:

                    quickdata[f'{char[0]} {entry} avedmg'] = 0

                temp_counter2 += 1

            for entry in quickdata:

                if [entry, quickdata[entry]] not in quickdata_output:

                    quickdata_output.append([entry, quickdata[entry]])

            quickdata = {}

    tempheader = ['description', 'output']

    with open(f'quick_analysis.csv', 'w', newline="") as file:

        csvwriter = csv.writer(file)
        csvwriter.writerow(tempheader)
        csvwriter.writerows(quickdata_output)


infinitywhileloop = False
while infinitywhileloop == False:

    input_varSTR1 = input('team or player specific analysis? (type player name or "team")')

    if input_varSTR1.lower() == 'team':

        input_varSTR2 = input('Total damage or average damage analysis? (type "total" or "average")')

        match input_varSTR2:

            case 'total':

                input_varSTR3 = input('Total campaign analysis or day specific analysis? (type "total" or date in '
                                      'dd/mm/yyyy format')

                if input_varSTR3.lower() == 'total':

                    for entry in data:

                        dmg += int(entry['dmg_output'])

                    print(f"The party's total dmg output for the total campaign is {dmg}")

                else:

                    for entry in data:

                        if entry['date'] == input_varSTR3:

                            dmg += int(entry['dmg_output'])

                    print(f"The party's total dmg output on {input_varSTR3.lower()} is {dmg}")

            case 'average':

                input_varSTR3 = input('Total campaign analysis or day specific analysis? (type "total" or date in '
                                      'dd/mm/yyyy format')

                if input_varSTR3.lower() == 'total':

                    for entry in data:

                        dmg += int(entry['dmg_output'])
                        dmg_counter += 1

                    if dmg_counter != 0:

                        print(f"The party's average dmg output for the total campaign is {dmg / dmg_counter}")

                    else:

                        print(f"The party's average dmg output for the total campaign is 0")

                else:

                    for entry in data:

                        if entry['date'] == input_varSTR3:

                            dmg += int(entry['dmg_output'])
                            dmg_counter += 1

                    if dmg_counter != 0:

                        print(f"The party's average dmg output on {input_varSTR3.lower()} is {dmg / dmg_counter}")

                    else:

                        print(f"The party's average dmg output on {input_varSTR3.lower()} is 0")

    else:
        i = 0
        while i < len(char_name_list):

            if char_name_list[i][0] == input_varSTR1.lower():

                analysis_char = input_varSTR1.lower()

            i += 1

        data = []
        with open(f'{analysis_char}_atklog.csv', 'r', newline="") as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:

                data.append(row)

        input_varSTR2 = input('Total damage or average damage analysis? (type "total" or "average")')

        match input_varSTR2:

            case 'total':

                input_varSTR3 = input('Total campaign analysis or day specific analysis? (type "total" or date in '
                                      'dd/mm/yyyy format')

                if input_varSTR3.lower() == 'total':

                    for entry in data:

                        dmg += int(entry['dmg_output'])

                    print(f"{analysis_char}'s total dmg output for the total campaign is {dmg}")

                else:

                    for entry in data:

                        if entry['date'] == input_varSTR3:

                            dmg += int(entry['dmg_output'])

                    print(f"{analysis_char}'s total dmg output on {input_varSTR3.lower()} is {dmg}")

            case 'average':

                input_varSTR3 = input('Total campaign analysis or day specific analysis? (type "total" or date in '
                                      'dd/mm/yyyy format')

                if input_varSTR3.lower() == 'total':
                    for entry in data:

                        dmg += int(entry['dmg_output'])
                        dmg_counter += 1

                    if dmg_counter != 0:

                        print(f"{analysis_char}'s average dmg output for the total campaign is {dmg / dmg_counter}")

                    else:

                        print(f"{analysis_char}'s average dmg output for the total campaign is 0")

                else:
                    for entry in data:

                        if entry['date'] == input_varSTR3:

                            dmg += int(entry['dmg_output'])
                            dmg_counter += 1

                    if dmg_counter != 0:

                        print(f"{analysis_char}'s average dmg output on {input_varSTR3.lower()} is {dmg / dmg_counter}")

                    else:

                        print(f"{analysis_char}'s average dmg output on {input_varSTR3.lower()} is 0")

