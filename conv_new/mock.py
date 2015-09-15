import datetime
import csv
import sys


# Class responsible for Mocking database
class mockdb:
    def __init__(self):
        self.filename = 'user_log.csv'

    def write_data_csv(self, data):
        with open(self.filename, 'w') as fp:
            write = csv.writer(fp, delimiter=',')
            write.writerows(data)

    def read_csv(self):
        read = csv.reader(open("user_log.csv", "rt"))
        out = []
        for row in read:
            out.append(row)
        return out

    def empty_file(self):
        fileopen = open(self.filename, "w")
        fileopen.truncate()
        fileopen.close()


        # mockobj = mockdb()
        # mockobj.empty_file()
        # time = datetime.datetime.utcnow()
        # data = [['1','101','2',time],['2','102','3',time]]
        # mockobj.write_data_csv(data)
        # print mockobj.read_csv()
