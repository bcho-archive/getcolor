#coding: utf-8

from getcolor.database import db


class Color(db.Model):
    hexcode = db.Column(db.String(7), primary_key=True)
    r = db.Column(db.Integer)
    g = db.Column(db.Integer)
    b = db.Column(db.Integer)
    name = db.Column(db.String(100))
    med_name = db.Column(db.String(100))
    short_name = db.Column(db.String(100))
    descriptions = db.relationship('Descriptions', backref='color')

    def __init__(self, **data):
        self._assign(data)
        self._rgb2hex()

    def _assign(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def add_descriptions(self, descs):
        for desc in descs:
            self.descriptions.append(Descriptions(desc=desc))

    def _rgb2hex(self):
        self.hexcode = '#%02x%02x%02x' % (
                int(self.r), int(self.g), int(self.b))


class Descriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(300))
    color_id = db.Column(db.String(7), db.ForeignKey('color.hexcode'))

    def __init__(self, **data):
        self._assign(data)

    def _assign(self, data):
        for key, value in data.items():
            setattr(self, key, value)
