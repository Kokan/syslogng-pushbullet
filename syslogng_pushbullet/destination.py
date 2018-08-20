# -*- coding: utf-8 -*-


class Destination(object):
    """Destination base"""

    def init(self, args):
        return True

    def deinit(self):
        pass

    def open(self):
        return True

    def is_opened(self):
        return True

    def close(self):
        return True

    def send(self, message):
        return True
