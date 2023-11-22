import json


class FlowData:

    def __init__(self, device_id, pulse, factor, milliliter, cl, timestamp, datetime):
        self.__device_id = device_id
        self.__pulse = pulse
        self.__factor = factor
        self.__milliliter = milliliter
        self.__cl = cl
        self.__timestamp = timestamp
        self.__datetime = datetime

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        self.__device_id = value

    @property
    def milliliter(self):
        return self.__milliliter

    @milliliter.setter
    def milliliter(self, value):
        self.__milliliter = value

    @property
    def pulse(self):
        return self.__pulse

    @pulse.setter
    def pulse(self, value):
        self.__pulse = value

    @property
    def cl(self):
        return self.__cl

    @cl.setter
    def cl(self, value):
        self.__cl = value

    @property
    def factor(self):
        return self.__factor

    @factor.setter
    def factor(self, value):
        self.__factor = value

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.__timestamp = value

    @property
    def datetime(self):
        return self.__datetime

    @datetime.setter
    def datetime(self, value):
        self.__datetime = value
