# -*- coding: utf-8 -*-

import requests

PUSH_URL = "https://api.pushbullet.com/v2/pushes"
DEVICES_URL = "https://api.pushbullet.com/v2/devices"


class PushbulletClient(object):
    """Pushbullet client"""

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Access-Token": self.api_key})

    def list_devices(self):
        """List devices"""
        return self.session.get(DEVICES_URL).json()

    def device_by_nickname(self, nickname):
        """Get device identifier with a nickname"""
        devices = self.list_devices()
        return next((d["iden"] for d in devices.get("devices", [])
                     if nickname == d.get("nickname")), None)

    def push_note(self, device_iden, title, body):
        """Push note to a device"""
        self.session.post(
            PUSH_URL,
            json={
                "device_iden": device_iden,
                "type": "note",
                "title": title,
                "body": body
            })
