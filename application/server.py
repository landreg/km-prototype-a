from flask import render_template, flash, redirect
from application import app
from flask import render_template
from forms import searchForm
from ElastSearch import SearchDataOnMeta, SearchDataOnId

storeditemid = 1


@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/test', methods=['GET','POST'])
def displaySearchResult():

    b = '<h2>Bankruptcy - Applications for Form J restrictions</h2>' + '<p class="lead">' + 'Where one or more of joint registered proprietors is subject to a petition in bankruptcy or bankruptcy order, neither a bankruptcy notice nor a bankruptcy restriction will be entered. However, the Official Receiver or trustee in bankruptcy may apply in form RX1 for a Form J restriction once the bankruptcy order has been made.</p>'


    page = b
    return render_template('test.html',searchElements=page)

@app.route('/gov-base', methods=['GET','POST'])
def footer():
    form = searchForm()
    return render_template('gov-base.html')

#@app.route('/test', methods=['GET','POST'])
#def test():
#    form = searchForm()
#    return render_template('test.html')


@app.route('/index', methods=['GET','POST'])
def index():
    form = searchForm()
    return render_template('index.html', form=form)

@app.route('/search', methods=['GET','POST'])
def searchResult():
    form = searchForm()

    SearchList = []
    BodyList = []
    TitleList = []
    SubtitleList = []

    #flash('Searched for "%s"' %(form.searchString.data))
    res = SearchDataOnMeta(form.searchString.data)

    #print res
    for hit in res['hits']['hits']:
        BodyList.append(hit["_source"]["body"])
        TitleList.append(hit["_source"]["title"])
        SubtitleList.append(hit["_source"]["sub title"])
    #print SearchList[0]
    return render_template('searchResult.html',titleElements=TitleList, bodyElements=BodyList, subtitleElements=BodyList)



@app.route('/page/<int:itemid>', methods=['GET'])
def displayPage(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        subtitle = (hit["_source"]["sub title"])

    print storeditemid

    return render_template('page.html',searchElements=body)

@app.route('/lr-content-static', methods=['GET'])
def lrcontentstatic():
    form = searchForm()
    return render_template('lr-content.html')

@app.route('/gov-content-static')
def govcontentstatic():
    return render_template('gov-content.html')

@app.route('/lr-page/<int:itemid>', methods=['GET'])
def displayLrPage(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        subtitle = (hit["_source"]["sub title"])

    print storeditemid

    return render_template('lr-page.html',searchElements=body)

@app.route('/lr-page', methods=['GET'])
def lrcontent():
        global storeditemid

        itemid = storeditemid
        res = SearchDataOnId(str(itemid))

        for hit in res['hits']['hits']:
            body = (hit["_source"]["body"])
            title = (hit["_source"]["title"])
            subtitle = (hit["_source"]["sub title"])

        print storeditemid

        return render_template('lr-page.html',searchElements=body)

@app.route('/gov-page', methods=['GET'])
def govcontent():
        global storeditemid

        itemid = storeditemid
        res = SearchDataOnId(str(itemid))

        for hit in res['hits']['hits']:
            body = (hit["_source"]["body"])
            title = (hit["_source"]["title"])
            subtitle = (hit["_source"]["sub title"])

        print storeditemid

        return render_template('page.html',searchElements=body)

@app.route('/gov-page/<int:itemid>', methods=['GET'])
def displayGovPage(itemid):

    global storeditemid

    storeditemid = itemid
    res = SearchDataOnId(str(itemid))

    for hit in res['hits']['hits']:
        body = (hit["_source"]["body"])
        title = (hit["_source"]["title"])
        subtitle = (hit["_source"]["sub title"])

    print storeditemid

    return render_template('page.html',searchElements=body)
