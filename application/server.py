from flask import render_template, flash, redirect
from application import app
from flask import render_template
from forms import searchForm
#from ElastSearch import SearchDataOnMeta

@app.route('/')
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
    #res = SearchDataOnMeta(form.searchString.data)
    
    #print res
    #for hit in res['hits']['hits']:
     #   BodyList.append(hit["_source"]["body"])
    #    TitleList.append(hit["_source"]["title"])
    #    SubtitleList.append(hit["_source"]["sub title"])
    #print SearchList[0]
    #return render_template('searchResult.html',titleElements=TitleList, bodyElements=BodyList, subtitleElements=BodyList)
    return render_template('searchResult.html',titleElements='Transfer', bodyElements='head', subtitleElements='tails')
   
    
    
@app.route('/page', methods=['GET','POST'])
def displayPage():
    print('display knowledge article page')
    
