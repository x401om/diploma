def getLines(fileName):
    with open('data.xls') as f:
        s = f.read()
    return s.split('\n')

lines = getLines('data.xls')

def getGlobalsHeader():
    for line in lines:
        line = line.split('\t')
        if 'globals' in line and 'Period' in line:
            return line

def getGlobals():
    for line in lines:
        line = line.split('\t')
        if 'globals' in line and 'Period' not in line:
            return line

def getPeriodsHeader():
    for line in lines:
        line = line.split('\t')
        if 'subjects' in line and 'Period' in line:
            return line

def getPeriods():
    periods = []
    for line in lines:
        line = line.split('\t')
        if 'Period' not in line and 'subjects' in line and 'globals' not in line:
            periods.append(line)
    return periods

def getPeriodsForParticipant(participantNumber):
    periods = getPeriods()
    header = getPeriodsHeader()
    index = header.index('Subject')
    steps = []
    for line in periods:
        if int(line[index]) == participantNumber:
            steps.append(line)
    return steps

headerForSteps = 'game;time;subject;group;grSubject;type;profit;penalty;x;s1;s2;s3\n'

def indexOfTitle(title):
    header = getPeriodsHeader()
    return header.index(title)

def createTableForParticipant(participantNumber):
    fileName = 'steps_' + str(participantNumber) + '.csv'
    f = open(fileName, 'w')
    f.write(headerForSteps)
    steps = getPeriodsForParticipant(participantNumber)
    globalsHeader = getGlobalsHeader()
    type = getGlobals()[int(globalsHeader.index('types[{0}]'.format(participantNumber)))]
    for s in steps:
        f.write('36;{0};{1};1;{2};{3};{4};{5};{6};{7};{8};{9}\n'.format(s[indexOfTitle('Period')],
                                                                 s[indexOfTitle('Subject')],
                                                                 s[indexOfTitle('Subject')],
                                                                 type,
                                                                 s[indexOfTitle('Profit')],
                                                                 s[indexOfTitle('Penalty')],
                                                                 s[indexOfTitle('x')],
                                                                 s[indexOfTitle('s[1]')],
                                                                 s[indexOfTitle('s[2]')],
                                                                 s[indexOfTitle('s[3]')]))


import matplotlib.pyplot as plt

def draw():
    x = [1,2,3,4,5,6,7,8]
    y = [5,2,2,5,6,2,1,5]
    plt.plot(x,y,'-')
    plt.show()

draw()

