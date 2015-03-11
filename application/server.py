from flask import render_template, flash, redirect
from application import app
from flask import render_template
from forms import searchForm
from ElastSearch import SearchDataOnMeta, SearchDataOnId, SearchDataOnRelated

class article(object):
    def __init__(self, title=None, itemid=None, scope=None):
        self.title = title
        self.itemid = itemid
        self.scope = scope

#rl_article_list = []

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
    ScopeList = []

    res = SearchDataOnMeta(form.searchString.data)

    hit = res['hits']['hits']
    for hit in res['hits']['hits']:
        BodyList.append(hit["_source"]["body"])
        TitleList.append(hit["_source"]["title"])
        ScopeList.append(hit["_source"]["scope"])

    return render_template('searchResult.html',titleElements=TitleList, bodyElements=BodyList, subtitleElements=BodyList)


#Select your theme
@app.route('/lr-page/<int:itemid>', methods=['GET'])
def displayLrPage(itemid):

    global storeditemid

    rl_article_list = []

    storeditemid = itemid
    prime_res = SearchDataOnId(str(itemid))
    related_res = SearchDataOnRelated(str(itemid))

    for hit in prime_res['hits']['hits']:
        pr_body = (hit["_source"]["body"])
        pr_title = (hit["_source"]["title"])
        pr_scope = (hit["_source"]["scope"])

    #create an object list to store related article information
    for hit in related_res['hits']['hits']:
        rl_article_list.append(article(hit["_source"]["title"], hit["_source"]["itemid"], hit["_source"]["scope"]))

    print rl_article_list[0].title

    return render_template('lr-page.html',searchElements=pr_body, related_list = rl_article_list)

@app.route('/gov-page/<int:itemid>', methods=['GET'])
def displayGovPage(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        scope = (hit["_source"]["scope"])

    return render_template('page.html',searchElements=body)

@app.route('/lr-page-std/<int:itemid>', methods=['GET'])
def displayLrPageStd(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        scope = (hit["_source"]["scope"])

    return render_template('lr-page-std.html',searchElements=body)
