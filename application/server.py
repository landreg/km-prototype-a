from flask import render_template, flash, redirect, request, session, make_response
from application import app
from flask import render_template
from sets import Set
from forms import searchForm, uploadContentForm, uploadResultsForm
from ElastSearch import NewSearchDataOnContent, NewSearchDataOnId, NewSearchDataOnRelated, UploadContent

class article(object):
    def __init__(self, title=None, itemid=None, scope=None):
        self.title = title
        self.itemid = itemid
        self.scope = scope

class ext_link(object):
    def __init__(self, title=None, link=None):
        self.title = title
        self.link = link

class facet(object):
    def __init__(self, name):
        self.name = name
        self.foci_list = []

    def add_foci(self, foci):
        self.foci_list.append(foci)

    def remove_duplicates(self):
        old_list = self.foci_list
        self.foci_list = list(Set(old_list))

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


@app.route('/search-result', methods=['GET'])
def searchUpdate():

    minPageSize = 5
    form = searchForm()
    facet_list = []

    #Get store page size from cookie
    cookiePageSize = request.cookies.get('cookie-pagesize')

    print cookiePageSize
    print request.args.get('search')
    print request.args.get('searchtype')
    print request.args.get('pagesize')
    print request.args.get('pageno')

    search = request.args.get('search')

    if request.args.get('searchtype') == None:
        searchType = 'score'
        pageNo = 1
        pageSize = int(cookiePageSize)
    else:
        searchType = request.args.get('searchtype')
        pageSize = int(request.args.get('pagesize'))
        pageNo = int(request.args.get('pageno'))

    if pageSize == None:
        pageSize = minPageSize


    noResults = "<h3>Your search did not match any articles</h3><p><a id=\"no_article\" href=\"/search\">Click here to search again</a></p>"
    searchResults = ""

    if request.args.get('search') != "":

        fields = ["scope", "keywords^5", "title"] #what fields are we searching on

        order = "desc" #asc or desc

        #for searchType pass in 'score' 'date' 'popularity'
        res = NewSearchDataOnContent(search, searchType, pageSize, pageNo, fields, order)
        hit = res['hits']['hits']

        totalNoHits = int(res['hits']['total'])

        print "Total number of hits " + str(res['hits']['total'])

        for hit in res['hits']['hits']:
            articleId = hit["_source"]["id"]
            searchResults += "<h3><a id=\"article_id_" + articleId + "\" href =\"/lr-page/" + articleId + "\">" + hit["_source"]["title"] + "</a></h3>"
            searchResults += "<p>" + hit["_source"]["scope"] + "</p>"

            #loop through the list of facets
            for items in hit["_source"]["facets"]:
                if "name" in items:
                    #store the name of the facet
                    facet_name = items['name']

                    #check if this facet already exists
                    index = -1
                    for i, v in enumerate(facet_list):
                        #return the index of the element if it does
                        if v.name == facet_name:
                            index = i
                            break
                        #return -1 if it doesn't
                        else:
                            index = -1

                    if index == -1:
                        #add a new facet item
                        data = facet(facet_name)
                        for foci in items['foci']:
                            #add the foci
                            data.add_foci(foci)
                        #add the facet item to the list
                        facet_list.append(data)
                    else:
                        #get an existing facet item
                        data = facet_list.pop(index)
                        for foci in items['foci']:
                            #add foci to that item
                            data.add_foci(foci)
                        #add the facet item back to the list
                        facet_list.append(data)

        #finally remove any foci duplicates for each facet item
        for data in facet_list:
            data.remove_duplicates()

        if searchResults == "":
            searchResults = noResults
    else:
        return render_template('index.html', form=form)

    resp = make_response(render_template('searchResult.html', form=form, searchElements=searchResults, search=search, searchtype=searchType, totalnohits=totalNoHits, pagesize=pageSize, pageno=pageNo, facetElements=facet_list))

    #Set or create cookie to store number of results on the page
    cookie = str(pageSize)
    resp.set_cookie('cookie-pagesize', cookie)
    print request.cookies.get('cookie-pagesize')

    return resp

@app.route('/lr-page/<itemid>', methods=['GET'])
def displayLrPage(itemid):

    form = searchForm()

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

    return render_template('lr-page.html', form=form, searchElements=pr_body, related_list = rl_article_list, external_list = rl_external_list)

@app.route('/uploadcontent', methods=['GET','POST'])
def uploadPage():

    form = uploadContentForm()
    if form.validate_on_submit():
        files = request.files.getlist("files[]")
        filenames = []
        for file in files:
            filename = str(file.filename)
            res = UploadContent(file)
            if str(res)[0] != "2":
                filenames.append("File " + filename+" failed to upload. Status code is " + str(res))
        return render_template('/uploadresults.html', filenames=filenames)
    return render_template('uploadcontent.html',form=form)

@app.route('/uploadresults', methods=['GET','POST'])
def uploadResultsPage():

    form = uploadResultsForm()
    if form.validate_on_submit():
        return redirect('/uploadcontent')
    return render_template('uploadresults.html', form=form, filenames=filenames)
