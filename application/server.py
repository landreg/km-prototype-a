from flask import render_template, flash, redirect, request
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


#########################################################################################################################
### Redundant code used from static code demonstration and multiple themes
#########################################################################################################################
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

#Select your theme
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

#########################################################################################################################

#Elasticsearch
@app.route('/')
@app.route('/index')
@app.route('/search')
def index():
    form = searchForm()
    return render_template('index.html', form=form)

@app.route('/search-result', methods=['POST'])
def searchResult():
    form = searchForm()

    #print "This is the form data 1 " + str(form.searchString.data)

    noResults = "<h3>Your search did not match any articles</h3><p><a id=\"no_article\" href=\"/search\">Click here to search again</a></p>"
    searchResults = ""

    search = form.searchString.data

    if form.searchString.data != "":

        #print "This is the form data 2 " + str(form.searchString.data)

        #pass in 'score' 'date' 'popularity'
        res = NewSearchDataOnContent(form.searchString.data, 'date', 5, 1)
        hit = res['hits']['hits']

        totalNoHits = int(res['hits']['total'])
        
        for hit in res['hits']['hits']:
            #print hit
            articleId = hit["_source"]["id"]
            searchResults += "<h3><a id=\"article_id_" + articleId + "\" href =\"/lr-page/" + articleId + "\">" + hit["_source"]["title"] + "</a></h3>"
            searchResults += "<p>" + hit["_source"]["scope"] + "</p>"

        if searchResults == "":
            searchResults = noResults
    else:

        return render_template('index.html', form=form)

    return render_template('searchResult.html',searchElements=searchResults, form=form, search=search,  searchtype='date', totalnohits=totalNoHits, pagesize=5, pageno=1)

@app.route('/search-update', methods=['GET'])
def searchUpdate():

    form = searchForm()

    #search=and&searchtype=data&pagesize=5&pageno=1

    print request.args.get('search')
    print request.args.get('searchtype')
    print request.args.get('pagesize')
    print request.args.get('pageno')

    search = request.args.get('search')
    searchType = request.args.get('searchtype')
    pageSize = int(request.args.get('pagesize'))
    pageNo = int(request.args.get('pageno'))



    noResults = "<h3>Your search did not match any articles</h3><p><a id=\"no_article\" href=\"/search\">Click here to search again</a></p>"
    searchResults = ""

    if request.args.get('search') != "":

        #pass in 'score' 'date' 'popularity'
        res = NewSearchDataOnContent(search, searchType, pageSize, pageNo)
        hit = res['hits']['hits']

        totalNoHits = int(res['hits']['total'])

        print "Total number of hits " + str(res['hits']['total'])

        for hit in res['hits']['hits']:

            articleId = hit["_source"]["id"]
            searchResults += "<h3><a id=\"article_id_" + articleId + "\" href =\"/lr-page/" + articleId + "\">" + hit["_source"]["title"] + "</a></h3>"
            searchResults += "<p>" + hit["_source"]["scope"] + "</p>"

        if searchResults == "":
            searchResults = noResults
    else:

        return render_template('index.html', form=form)

    return render_template('searchResult.html', searchElements=searchResults, search=search, searchtype=searchType, totalnohits=totalNoHits, pagesize=pageSize, pageno=pageNo)

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


    return render_template('lr-page.html',searchElements=pr_body, related_list = rl_article_list)
