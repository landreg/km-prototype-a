from flask import render_template, flash, redirect
from application import app
from flask import render_template
from forms import searchForm
from ElastSearch import SearchDataOnMeta


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



@app.route('/page', methods=['GET','POST'])
def displayPage():
    print('display knowledge article page')
