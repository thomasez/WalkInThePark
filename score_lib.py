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
            self.config = self.createNewConfig()

    def get(self, section, key):
        return self.config.get(section, key)

    def set(self, section, key, value):
        return self.config.set(section, key, value)

    def check_sqlite_exists(self):
        try:
            import pysqlite2
            return True
        except:
            return False

    def create_new_config(self):
        config = ConfigParser()
        config.add_section('wip')
        if self.check_sqlite_exists():
            config.set('wip', 'db_storage', 'sqlite')
        else:
            config.set('wip', 'db_storage', 'files')
        config.set('wip', 'course_type', 'disc')
        config.set('wip', 'default_course', 'Ekeberg')
        config.add_section('pebble')
        self.save_config()
        return config

    def save_config(self):
        # Should I just die? Prolly not, this is a GUI app.. 
        # need to remember that part.
        try:
            with open(os.environ.get('HOME') + "/" + self.configfile, "wb") as file:
                self.config.write(file)
            return True
        except IOError:
            return False

class Player:
    def __init__(self, name = ''):
        self.name = name

    def set_name(self, name):
        self.name = name
        return self.name

    def get_name(self):
        return self.name

class Course:
    def __init__(self, name = ''):
        self.par = []
        self.name = ''
        self.baskets = 18

    def set_name(self, name):
        self.name = name
        return self.name

    def get_name(self):
        return self.name

    def set_baskets(self, baskets):
        self.baskets = baskets
        return self.baskets

    def get_baskets(self):
        return self.baskets

    def get_par(self, bnum):
        return self.par[bnum]

class Walk:

    def __init__(self, course, debug = False):
        self.debug  = debug
        self.course = course
        self.basket = 1
        self.total = {}
        self.baskets = self.course.get_baskets()
        self.started_at = datetime.now()
        self.walk = []
        # This is annoying in so many ways. I'd love the array to start from 
        # 1 but it does not. walk[0] will never be used. Therefor I have
        # to set "Done" to True so we'll end up with all True when we're done.
        self.walk.append({'throws': 0, 'done': True})
        for i in range(0,(self.baskets + 1)):
            self.walk.append({'throws': 0, 'done': False})
        self.recalc()

    def set_course(self, course):
        self.course = course
        return self.course

    def get_course(self):
        return self.course

    def get_result(self):
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
                par = self.course.get_par(i)
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

    def get_score_as_list(self):
        score = []
        score.append(self.course.get_name())
        score.append(self.player.get_name())
        score.append(self.started_at.isoformat())
        for i in range(1,(self.baskets + 1)):
            score.append(self.walk[i]['throws'])
        score.append(self.total['score'])
        return score

    def get_pure_score_list(self):
        c = []
        for i in range(1,(self.baskets + 1)):
            c.append(self.walk[i]['throws'])
        return c

    def is_done(self):
        for b in self.walk:
            if b['done'] is False:
                return False
        return True

    def get_basket(self):
        return self.basket

    def get_course(self):
        return self.course

    def set_player(self, player):
        self.player = player
        return self.player

    def get_player(self):
        return self.player

    def add_throw(self, num):
        self.walk[self.basket]['throws'] += 1
        # When first started, let's assume we're gonne be done with it..
        self.walk[self.basket]['done'] = True
        return self.walk[self.basket]['throws']

    def subtract_throw(self, num):
        self.walk[self.basket]['throws'] -= 1
        return self.walk[self.basket]['throws']

    def get_throws(self):
        return self.walk[self.basket]['throws']

    def set_current_basket(self, num):
        self.basket = num
        return self.basket

    def next_basket(self):
        if self.basket == self.baskets:
            self.basket = 1
        else:
            self.basket += 1
        self.recalc()
        return self.basket

    def previous_basket(self):
        if self.basket > 1:
            self.basket = self.basket - 1
        else:
            self.basket = self.baskets
        self.recalc()
        return self.basket

