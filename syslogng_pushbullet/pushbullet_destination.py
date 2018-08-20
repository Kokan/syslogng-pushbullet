# -*- coding: utf-8 -*-

from __future__ import print_function

import requests

from .destination import Destination
from .pushbullet import PushbulletClient


class PushbulletDestination(Destination):
    """Pushbullet destination for syslog-ng"""

    title_template = "%(HOST)s %(PROGRAM)s [%(PID)s]"
    body_template = "%(MESSAGE)s"

    def __init__(self):
        self.api_key = None
        self.device = None
        self.device_iden = None

    def init(self, args):
        if any(k not in args for k in ("api_key", "device")):
            return False
        self.api_key = args["api_key"]
        self.device = args["device"]
        if "title_template" in args:
            self.title_template = args["title_template"]
        if "body_template" in args:
            self.body_template = args["body_template"]
        self.client = PushbulletClient(self.api_key)
        self.device_iden = self.client.device_by_nickname(self.device)
        if not self.device_iden:
            return False
        return True

    def send(self, message):
        try:
            self.client.push_note(self.device_iden,
                                  self.title_template % message,
                                  self.body_template % message)
        except requests.HTTPError:
            return False
        else:
            return True
