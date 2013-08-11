import csv
from score_lib import Player, Course, Walk, WipConfig

class Db:
    def __init__(self):
        return None

    def get_course_list(self):
        import glob
        list = []
        for file in glob.glob("*.course"):
            list.append(file.replace('.course', ''))
        return list

    def get_course(self, name):
        course = Course();
        with open(name + '.course', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            # It's just one line..
            row = reader.next()
            course.par = []
            course.name = row.pop(0)
            course.baskets = int(row.pop(0))
            course.par.append(0);
            coursepar = 0
            for i in range(0,course.baskets):
                coursepar += int(row[i])
                # course.par[i-1] = int(row[i])
                course.par.append(int(row[i]))
            course.par[0] = course.coursepar = coursepar
        return course
             
    def save_score(self, Walk):
        with open('wip_score.csv', 'awb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', \
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(Walk.get_score_as_list())

    def save_score_as_course(self, Walk, coursename):
        with open(coursename + '.course', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', \
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
            sac = Walk.get_pure_score_list()
            sac.insert(0, coursename)
            writer.writerow(sac)


