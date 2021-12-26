import csv
from os.path import exists

program = True
scoreboard = {}

while program:
    print('1. Load event file')
    print('2. Show current scoreboard')
    print('3. Export scoreboard')
    print('4. Quit')

    #load file
    if exists('score.csv'):
        with open('score.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                scoreboard[row[0]] = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]),
                                      int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]),
                                      int(row[13])]
    else:
        with open('score.csv', 'w', newline='') as csvfile:
            csv.writer('')

    prompt = int(input('Enter an option: '))

    if prompt == 1:
        prompt = 0
        while prompt < 1 or prompt > 12:
            prompt = int(input('What month are the scores going into (1-12)? '))
        try:
            filename = input('Type in the event file you are importing here: ')
            with open(filename, newline='') as csvfile:
                spamreader = csv.reader(csvfile)
        except:
            print('File error')
        else:
            for row in spamreader:
                if row[0] not in scoreboard:
                    scoreboard[row[0]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    scoreboard[row[0]][prompt - 1] += int(row[1])
                    scoreboard[row[0]][12] += int(row[1])
            print('Load successful.')
    elif prompt == 2:
        if len(scoreboard) == 0:
            print('No scores to report.')
        else:
            scoreboard = dict(sorted(scoreboard.items(), key=lambda x: x[1][12], reverse=True))
            for key, value in scoreboard.items():
                print(key + ' ' + str(scoreboard[key][0]) + ' ' + str(scoreboard[key][1]) + ' ' +  str(scoreboard[key][2]) + ' ' + str(scoreboard[key][3]) + ' ' +
                      str(scoreboard[key][4]) + ' ' + str(scoreboard[key][5]) + ' ' + str(scoreboard[key][6]) + ' ' + str(scoreboard[key][7]) + ' ' +
                      str(scoreboard[key][8]) + ' ' + str(scoreboard[key][9]) + ' ' + str(scoreboard[key][10]) + ' ' + str(scoreboard[key][11]) + ' - ' + str(scoreboard[key][12]))
    elif prompt == 3:
        scoreboard = dict(sorted(scoreboard.items(), key=lambda x: x[1][12], reverse=True))
        with open('score.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for key, value in scoreboard.items():
                spamwriter.writerow([key, scoreboard[key][0], scoreboard[key][1], scoreboard[key][2], scoreboard[key][3], scoreboard[key][4],
                                     scoreboard[key][5], scoreboard[key][6], scoreboard[key][7], scoreboard[key][8], scoreboard[key][9],
                                     scoreboard[key][10], scoreboard[key][11], scoreboard[key][12]])
    else:
        print('Goodbye.')
        program = False
