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
    return steps[1:]

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

def createBigTable():
    fileName = 'game.csv'
    f = open(fileName, 'w')
    f.write('#;f1;f2;f3;s11;s12;s13;x1;s21;s22;s23;x2;s31;s32;s33;x3\n')
    steps = [[]]
    for i in range(1,4):
        steps.append(getPeriodsForParticipant(i))
    for i in range(0, len(steps[1])):
        s = '{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10};{11};{12};{13};{14};{15}\n'.format(i+1,
                                                                                             steps[1][i][indexOfTitle("Profit")],
                                                                                             steps[2][i][indexOfTitle("Profit")],
                                                                                             steps[3][i][indexOfTitle("Profit")],
                                                                                             steps[1][i][indexOfTitle("s[1]")],
                                                                                             steps[1][i][indexOfTitle("s[2]")],
                                                                                             steps[1][i][indexOfTitle("s[3]")],
                                                                                             steps[1][i][indexOfTitle("x")],
                                                                                             steps[2][i][indexOfTitle("s[1]")],
                                                                                             steps[2][i][indexOfTitle("s[2]")],
                                                                                             steps[2][i][indexOfTitle("s[3]")],
                                                                                             steps[2][i][indexOfTitle("x")],
                                                                                             steps[3][i][indexOfTitle("s[1]")],
                                                                                             steps[3][i][indexOfTitle("s[2]")],
                                                                                             steps[3][i][indexOfTitle("s[3]")],
                                                                                             steps[3][i][indexOfTitle("x")])
        f.write(s)

import matplotlib.pyplot as plt

def drawGraphForParticipant(participantNumber):
    x = []
    p = []
    dots = []
    for i in range(1,4):
        steps = getPeriodsForParticipant(i)
        d = []
        for line in steps:
            d.append(line[indexOfTitle('s[{0}]'.format(participantNumber))])
            if i == 3:
                p.append(line[indexOfTitle('Period')])
                x.append(line[indexOfTitle('x')])
        dots.append(d)
    plt.plot(p,x,'-')
    plt.plot(p,dots[0],'r-')
    plt.plot(p,dots[1], 'g-')
    plt.plot(p,dots[2], 'y-')
    plt.title('Player {0}'.format(participantNumber))
    plt.show()

def drawGraphForKey(key):
    colors = ['r-', 'g-','b-']
    for i in range(1,4):
        steps = getPeriodsForParticipant(i)
        x = []
        y = []
        for line in steps:
            x.append(line[indexOfTitle('Period')])
            y.append(line[indexOfTitle(key)])
        plt.plot(x, y, colors[i-1])
    plt.title(key)
    if key == "Profit":
        plt.ylim((0,10))
    plt.show()

# drawGraphForParticipant(1)
# drawGraphForParticipant(2)
# drawGraphForParticipant(3)

# drawGraphForKey("Profit")
createBigTable()