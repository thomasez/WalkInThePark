import csv
from datetime import datetime
import time
import os
from ConfigParser import ConfigParser

class WipConfig:

    def __init__(self):
        self.configfile = ".walkintheparkrc"
        self.config = ConfigParser()
        try:
            self.config.readfp(open(os.environ.get('HOME') + "/" + self.configfile, "r"))
        except IOError:
            self.config = createNewConfig()

    def get(self, section, key):
        return self.config.get(section, key)

    def set(self, section, key, value):
        return self.config.set(section, key, value)

    def createNewConfig(self):
        config = ConfigParser()
        config.add_section('wip')
        config.set('wip', 'course_type', 'disc')
        config.set('wip', 'default_course', 'Ekeberg')
        config.add_section('pebble')
        saveConfig(self.config)
        return config

    def saveConfig(self):
        # Should I just die? Prolly not, this is a GUI app.. 
        # need to remember that part.
        try:
            with open(os.environ.get('HOME') + "/" + self.configfile, "wb") as file:
                self.config.write(file)
            return True
        except IOError:
            return False

    def getCourseList():
        return ['Ekeberg', 'Muselunden', 'Stovner']

class Player:
    def __init__(self, name = ''):
        self.name = name

    def setName(self, name):
        self.name = name
        return self.name

    def getName(self):
        return self.name

class Course:
    def __init__(self, name = ''):
        self.par = []
        self.name = ''
        self.baskets = 18
        if name:
            self.load(name)

    def load(self, name):
        with open(name + '.course', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            # It's just one line..
            row = reader.next()
            self.par = []
            self.name = row.pop(0)
            self.baskets = int(row.pop(0))
            self.par.append(0);
            coursepar = 0
            for i in range(0,self.baskets):
                coursepar += int(row[i])
                # self.par[i-1] = int(row[i])
                self.par.append(int(row[i]))
            self.par[0] = self.coursepar = coursepar
             
    def setName(self, name):
        self.name = name
        return self.name

    def getName(self):
        return self.name

    def setBaskets(self, baskets):
        self.baskets = baskets
        return self.baskets

    def getBaskets(self):
        return self.baskets

    def getPar(self, bnum):
        return self.par[bnum]

class Walk:

    def __init__(self, course, debug = False):
        self.debug  = debug
        self.course = course
        self.basket = 1
        self.total = {}
        self.baskets = self.course.getBaskets()
        self.started_at = datetime.now()
        self.walk = []
        # This is annoying in so many ways. I'd love the array to start from 
        # 1 but it does not. walk[0] will never be used. Therefor I have
        # to set "Done" to True so we'll end up with all True when we're done.
        self.walk.append({'throws': 0, 'done': True})
        for i in range(0,(self.baskets + 1)):
            self.walk.append({'throws': 0, 'done': False})
        self.recalc()

    def setCourse(self, course):
        self.course = course
        return self.course

    def getCourse(self):
        return self.course

    def getResult(self):
        return self.total

    def recalc(self):
        score = 0
        total_par = 0
        first = 0
        second = 0
        par_first = 0
        par_second = 0
        for i in range(1,(self.baskets + 1)):
            par = 0
            if self.walk[i]['throws'] > 0:
                par = self.course.getPar(i)
                if i <= (self.baskets / 2):
                    first += self.walk[i]['throws']
                    par_first += par
                else:
                    second += self.walk[i]['throws']
                    par_second += par
            score += self.walk[i]['throws']
            total_par += par
        self.total['res_first']  = first - par_first
        self.total['res_second'] = second - par_second
        self.total['par_first']  = par_first
        self.total['par_second'] = par_second
        self.total['score']      = score
        self.total['par']        = total_par
        self.total['result']     = score - total_par

    def getScoreAsList(self):
        score = []
        score.append(self.course.getName())
        score.append(self.player.getName())
        score.append(self.started_at.isoformat())
        for i in range(1,(self.baskets + 1)):
            score.append(self.walk[i]['throws'])
        score.append(self.total['score'])
        return score

    def isDone(self):
        for b in self.walk:
            if b['done'] is False:
                return False
        return True

    def getBasket(self):
        return self.basket

    def getCourse(self):
        return self.course

    def setPlayer(self, player):
        self.player = player
        return self.player

    def getPlayer(self):
        return self.player

    def addThrow(self, num):
        self.walk[self.basket]['throws'] += 1
        # When first started, let's assume we're gonne be done with it..
        self.walk[self.basket]['done'] = True
        return self.walk[self.basket]['throws']

    def subtractThrow(self, num):
        self.walk[self.basket]['throws'] -= 1
        return self.walk[self.basket]['throws']

    def getThrows(self):
        return self.walk[self.basket]['throws']

    def setCurrentBasket(self, num):
        self.basket = num
        return self.basket

    def nextBasket(self):
        if self.basket == self.baskets:
            self.basket = 1
        else:
            self.basket += 1
        self.recalc()
        return self.basket

    def previousBasket(self):
        if self.basket > 1:
            self.basket = self.basket - 1
        else:
            self.basket = self.baskets
        self.recalc()
        return self.basket

    def saveScore(self):
        with open('score.csv', 'awb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', \
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(Walk.getScoreAsList())

