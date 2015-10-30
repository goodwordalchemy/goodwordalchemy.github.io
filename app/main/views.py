from flask import render_template
from . import main
from .. import pages


@main.route('/')
def home():
    return "hello!"