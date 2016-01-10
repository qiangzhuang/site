#import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template
from flask_misaka import markdown
from app import app, APP_ROOT, APP_STATIC, APP_POSTS
import os, datetime

#@app.before_request
#def before_request():
 #   if request.url.startswith('http://'):
  #      url = request.url.replace('http://', 'https://', 1)
   #     code = 301
    #    return redirect("/", code=code)

def gimme_data(f):
    with open(f) as fd:
        return fd.read()

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

def list_dir(path):
	d = os.listdir(path)
	l = []
	for item in d:
		l.append(dict(name=item, modified=datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(path,item))).strftime('%Y-%m-%d %H:%M:%S')))
	return l

@app.route('/about')
def about():
	path = os.path.abspath(os.path.join(APP_STATIC, "about.md"))
	return render_template("markdown.html", post=gimme_data(path))


@app.route('/')
@app.route('/<dir1>')
@app.route('/<dir1>/')
@app.route('/<dir1>/<second>')
def temp(dir1='',second=''):
	path = os.path.abspath(os.path.join(APP_POSTS,dir1, second))
	if os.path.isdir(path) and path.startswith(APP_POSTS):
	#	return list_dir(path)[0]['name']
		return render_template("showdir.html", dircontents=list_dir(path),dir1=dir1, second=second)
	elif os.path.isfile(path) and path.startswith(APP_POSTS):
		return render_template("markdown.html", post=gimme_data(path), dir1=dir1, second=second)
	return render_template('404.html'), 404

#if __name__ == '__main__':
#    app.run()
