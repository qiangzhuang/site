#import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template
from flask_misaka import markdown
from app import app, APP_ROOT, APP_STATIC
import os


def get_most_recent_file():
    return os.path.join(APP_STATIC, "posts","post1.md")


def gimme_data(f):
    with open(f) as fd:
        return fd.read()

@app.route('/')
def show_recent_post():
    # get most recent markdown post in the folder of posts
    
    return render_template("markdown.html", post=gimme_data(get_most_recent_file()))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

#if __name__ == '__main__':
#    app.run()
