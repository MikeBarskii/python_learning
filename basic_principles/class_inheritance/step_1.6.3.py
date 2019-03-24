# https://stepik.org/lesson/24462/step/9?unit=6768
import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def log(self, msg):
        super().log(msg)

    def append(self, object):
        super().append(object)
        self.log(object)
