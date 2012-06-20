import time

class Output(object):
    def __init__(self):
        self.context = ''
        self.level = 0
        self.timestamps = False

    def write(self, s, level=0):
        if level > self.level:
            return
        if self.level > 1 or self.timestamps:
            timestamp = time.strftime('%H:%M:%S ')
        else:
            timestamp = ''
        print '%s%s> %s' % (timestamp, self.context, s)

    def writelines(self, lines, level=0):
        for line in lines:
            for line in line.rstrip('\n').split('\n'):
                self.write(line.rstrip('\n'), level=level)

out = Output()
