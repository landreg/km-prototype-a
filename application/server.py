from flask import render_template, flash, redirect
from application import app
from flask import render_template
from forms import searchForm

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    form = searchForm()
    return render_template('index.html', form=form)

@app.route('/search', methods=['GET','POST'])
def searchResult():
    form = searchForm()

    flash('Searched for "%s"' %(form.searchString))

    return render_template('searchResult.html',searchElements=form.searchString)
