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
        
class ext_link(object):
    def __init__(self, title=None, link=None):
        self.title = title
        self.link = link

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

    noResults = "<h3>Your search did not match any articles</h3><p><a id=\"no_article\" href=\"/search\">Click here to search again</a></p>"
    searchResults = ""

    if form.searchString.data != "":
        
        #Parameters: data, sort_type, page_size, page_number
        #pass in 'score' 'date' 'popularity' for sort_type
        res = NewSearchDataOnContent(form.searchString.data, 'score', 5, 1)
        #hit = res['hits']['hits'][2]
        #print res['hits']['total']
        for hit in res['hits']['hits']:
            articleId = hit["_source"]["id"]
            searchResults += "<h3><a id=\"article_id_" + articleId + "\" href =\"/lr-page/" + articleId + "\">" + hit["_source"]["title"] + "</a></h3>"
            searchResults += "<p>" + hit["_source"]["scope"] + "</p>"

            for item in hit["_source"]["facets"]:
                if "id" in item:
                    rl_id = item['id']
        if searchResults == "":
            searchResults = noResults
    else:

        return render_template('index.html', form=form)

    return render_template('searchResult.html',searchElements=searchResults)



@app.route('/lr-page/<itemid>', methods=['GET'])
def displayLrPage(itemid):

    global storeditemid

    rl_article_list = []
    rl_external_list = []

    storeditemid = itemid

    prime_res = NewSearchDataOnId(str(itemid))
    #this line will only get articles that have the primary article in THEIR related list only
    #related_res = NewSearchDataOnRelated(str(itemid))
    
    #business requirement is that only articles that their id in the PRIMARY article's related list  
    for hit in prime_res['hits']['hits']:
        pr_body = (hit["_source"]["content"])
        pr_title = (hit["_source"]["title"])
        pr_scope = (hit["_source"]["scope"])
        for item in hit["_source"]["kmlinks"]:
            if "id" in item:
                rl_id = item['id']
                related_res = NewSearchDataOnId(str(rl_id))
                #create an object list to store related article information
                for hit in related_res['hits']['hits']:
                    rl_article_list.append(article(hit["_source"]["title"], hit["_source"]["id"], hit["_source"]["scope"]))
            
        #create an object list to store external related links
        for item in hit['_source']['extlinks']:
            if "url" in item:
                rl_external_list.append(ext_link(item["name"], item["url"]))
    
    return render_template('lr-page.html',searchElements=pr_body, related_list = rl_article_list, external_list = rl_external_list)
