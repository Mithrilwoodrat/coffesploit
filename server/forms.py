# -*- coding: utf-8 -*-
from server import main
from flask import url_for
from wtforms import Form
from wtforms import TextField
from wtforms.validators import Required


def homelink():
    return url_for('index')


class StatusForm(Form):
    def __init__(self, status):
        super(StatusForm, self).__init__()
        arments = {}
        if status is not None:
            for arg in status:
                arments[arg] = TextField(arg)