from flask import render_template, flash, redirect
from application import app
from flask import render_template
from forms import searchForm
from ElastSearch import SearchDataOnMeta, SearchDataOnId

#Store current item ID - defualt to first item
storeditemid = 1

#Demonstration landing page
@app.route('/')
@app.route('/index')
def landing():
    return render_template('landing.html')

#Static demostration pages
@app.route('/lr-content-static')
def lrcontentstatic():
    return render_template('lr-content.html')

@app.route('/gov-content-static')
def govcontentstatic():
    return render_template('gov-content.html')

@app.route('/lr-content-std-static')
def lrcontentstdstatic():
    return render_template('lr-content-std.html')

#Test search of elasticsearch
@app.route('/search', methods=['GET'])
def index():
    form = searchForm()
    return render_template('index.html', form=form)

@app.route('/search-result', methods=['POST'])
def searchResult():
    form = searchForm()

    SearchList = []
    BodyList = []
    TitleList = []
    SubtitleList = []

    res = SearchDataOnMeta(form.searchString.data)

    for hit in res['hits']['hits']:
        BodyList.append(hit["_source"]["body"])
        TitleList.append(hit["_source"]["title"])
        SubtitleList.append(hit["_source"]["sub title"])

    return render_template('searchResult.html',titleElements=TitleList, bodyElements=BodyList, subtitleElements=BodyList)


#Select your theme
@app.route('/lr-page/<int:itemid>', methods=['GET'])
def displayLrPage(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        subtitle = (hit["_source"]["sub title"])

    return render_template('lr-page.html',searchElements=body)

@app.route('/gov-page/<int:itemid>', methods=['GET'])
def displayGovPage(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        subtitle = (hit["_source"]["sub title"])

    return render_template('page.html',searchElements=body)

@app.route('/lr-page-std/<int:itemid>', methods=['GET'])
def displayLrPageStd(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        subtitle = (hit["_source"]["sub title"])

    return render_template('lr-page-std.html',searchElements=body)
