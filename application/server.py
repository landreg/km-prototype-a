from flask import render_template, flash, redirect
from application import app
from flask import render_template
from forms import searchForm
from ElastSearch import NewSearchDataOnContent, NewSearchDataOnId, NewSearchDataOnRelated

class article(object):
    def __init__(self, title=None, itemid=None, scope=None):
        self.title = title
        self.itemid = itemid
        self.scope = scope

#rl_article_list = []

#Store current item ID - defualt to first item
storeditemid = 1

#Demonstration landing page
@app.route('/landing')
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
@app.route('/')
@app.route('/index')
@app.route('/search')
def index():
    form = searchForm()
    return render_template('index.html', form=form)

@app.route('/search-result', methods=['POST'])
def searchResult():
    form = searchForm()

    noResults = "<h2>Your search did not match any articles</h2><p><a id=\"no_article\" href=\"/search\">Click here to search again</a></p>"
    searchResults = ""

    if form.searchString.data != "":

        res = NewSearchDataOnContent(form.searchString.data)
        hit = res['hits']['hits']

        for hit in res['hits']['hits']:

            articleId = hit["_source"]["id"]
            searchResults += "<h2><a id=\"article_id_" + articleId + "\" href =\"/lr-page/" + articleId + "\">" + hit["_source"]["title"] + "</a></h2>"
            searchResults += "<p>" + hit["_source"]["scope"] + "</p>"

        if searchResults == "":
            searchResults = noResults
    else:

        return render_template('index.html', form=form)

    return render_template('searchResult.html',searchElements=searchResults)


#Select your theme
@app.route('/lr-page/<itemid>', methods=['GET'])
def displayLrPage(itemid):

    global storeditemid

    rl_article_list = []

    storeditemid = itemid
    prime_res = NewSearchDataOnId(str(itemid))
    related_res = NewSearchDataOnRelated(str(itemid))

    for hit in prime_res['hits']['hits']:
        pr_body = (hit["_source"]["content"])
        pr_title = (hit["_source"]["title"])
        pr_scope = (hit["_source"]["scope"])

    #create an object list to store related article information
    for hit in related_res['hits']['hits']:
        rl_article_list.append(article(hit["_source"]["title"], hit["_source"]["id"], hit["_source"]["scope"]))

    #print rl_article_list[0].title

    return render_template('lr-page.html',searchElements=pr_body, related_list = rl_article_list)

@app.route('/gov-page/<int:itemid>', methods=['GET'])
def displayGovPage(itemid):

    global storeditemid

    storeditemid = itemid
    res = NewSearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["content"])
        title = (hit["_source"]["title"])
        scope = (hit["_source"]["scope"])

    return render_template('page.html',searchElements=body)

@app.route('/lr-page-std/<int:itemid>', methods=['GET'])
def displayLrPageStd(itemid):

    global storeditemid

    storeditemid = itemid
    res = NewSearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["content"])
        title = (hit["_source"]["title"])
        scope = (hit["_source"]["scope"])

    return render_template('lr-page-std.html',searchElements=body)
