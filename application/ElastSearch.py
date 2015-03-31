import urllib2
import json
#from elasticsearch import Elasticsearch
import array
import requests



#URL = 'http://192.168.50.7:9200/knowledgetest/information'
#ES_HOST = {"host" : "http://192.168.50.7", "port" : 9200}
#INDEX_NAME = 'knowledge'
#TYPE_NAME = 'information'

#REMOTE_URL = 'https://km-prototype-1076374862.eu-west-1.bonsai.io/knowledge/information' #for testing

#REMOTE_URLcred = 'https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/knowledgelive/information' #for live

REMOTE_URL = 'https://km-prototype-1076374862.eu-west-1.bonsai.io/knowledgelive/information' #for live

#alex's test database
REMOTE_URLcred = 'https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/new_kmow_man/information'

#REMOTE_URLcred = 'https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/knowledgetest/information'

USR = 'cp94zbqxv3'
PWD = 'estftr8mkx'

def NewSearchDataOnId(data):
    '''passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, REMOTE_URL, USR, PWD)
    auth_handler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)

    url = REMOTE_URL+'/'+data
    out = urllib2.urlopen(url)
    res = out.read()
    res = json.loads(res)

    return res'''
    payload = json.dumps({"query": {"match" : {"id": data}}})
    headers = {'content-type': 'application/json'}

    res = requests.get(REMOTE_URLcred+'/_search', data=payload, headers=headers)
    res = json.loads(res.text)

    return res

#sort_type must be either score popularity date
def NewSearchDataOnContent(data, sort_type, page_size, page_number, fields, order):
    if page_number == 1:
        page_from = 0
    else:
        page_from = ((page_number - 1) * page_size)

    if sort_type == 'score':
        sort = '_score'
    elif sort_type == 'popularity':
        sort = 'popularity'
    elif sort_type == 'date':
        sort = 'lastupdate'
    else:
        sort = '_score'

    payload = json.dumps({"from":page_from, "size":page_size, "query": {"multi_match" : {"query": data, "fields": fields}},"sort": [{sort:{"order": order}}] })

    headers = {'content-type': 'application/json'}
    res = requests.get(REMOTE_URLcred+'/_search', data=payload, headers=headers)
    res = json.loads(res.text)

    return res

def NewSearchDataAllContent(data, fields):
    payload = json.dumps({"query": {"multi_match" : {"query": data, "fields": fields}}})

    headers = {'content-type': 'application/json'}
    res = requests.get(REMOTE_URLcred+'/_search', data=payload, headers=headers)
    res = json.loads(res.text)

    return res

def NewSearchwithFoci(data, sort_type, page_size, page_number, fields, order, facets):
    if page_number == 1:
        page_from = str(0)
    else:
        page_from = str((page_number - 1) * page_size)

    page_size = str(page_size)
    if sort_type == 'score':
        sort = '_score'
    elif sort_type == 'popularity':
        sort = 'popularity'
    elif sort_type == 'date':
        sort = 'lastupdate'
    else:
        sort = '_score'

    data1 = '{"nested": {"path": "facets", "query": {"bool": {"must": [ {"match": {"facets.name": '
    data2 = '}}, {"match": {'
    data3 = '"facets.foci": '
    data4 = ', '
    data5 = '}}'
    data6 = ']}}}}'

    num_facets = 0
    nested_data = ''

    for facet in facets:
        num_facets = num_facets + 1
        nested_data = nested_data + data1 +'"'+ facet.name +'"'+ data2
        num_foci = 0
        for foci in facet.foci_list:
            num_foci = num_foci + 1
            if len(facet.foci_list) > num_foci:
                nested_data = nested_data + data3 +'"'+ foci +'"'+ data4
            else:
                nested_data = nested_data + data3 +'"'+ foci +'"'+ data5
        if len(facets) > num_facets:
            nested_data = nested_data + data6 + data4
        else:
            nested_data = nested_data + data6

    query_data = '{"from":"'+page_from+'", "size":"'+page_size+'", "query": {"bool": {"must": [{"multi_match" : {"query":"'+data+'", "fields": ['
    num_fields = 0
    for field in fields:
        num_fields = num_fields + 1
        if len(fields) > num_fields:
            query_data = query_data +'"'+ field +'"'+ data4
        else:
            query_data = query_data +'"'+ field +'"]'

    payload= query_data + '}}, '+nested_data+']}},"sort": [{"'+sort+'":{"order": "'+order+'"}}] }'
    print payload
    headers = {'content-type': 'application/json'}
    res = requests.get(REMOTE_URLcred+'/_search', data=payload, headers=headers)
    res = json.loads(res.text)

    return res

def NewSearchDataOnItem(data):
    payload = json.dumps({"query": {"match" : {"items.item" : data}}})
    headers = {'content-type': 'application/json'}

    res = requests.get(REMOTE_URLcred+'/_search', data=payload, headers=headers)
    res = json.loads(res.text)

    return res

def NewSearchDataOnRelated(data):
    payload = json.dumps({"query": {"match" : {"kmlinks.id": data}}})
    headers = {'content-type': 'application/json'}

    res = requests.get(REMOTE_URLcred+'/_search', data=payload, headers=headers)
    res = json.loads(res.text)

    return res

def UploadContent(files):
    try:
        content = json.load(files)
    except ValueError:
        return 400
    if "id" in content:
        id_value = content["id"]
        headers = {'content-type': 'application/json'}
        r = requests.post(REMOTE_URLcred+'/'+id_value, data=json.dumps(content), headers=headers)
        return r.status_code
    else:
        return 400


'''
def SearchDataOnId(data):

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, REMOTE_URL, USR, PWD)
    auth_handler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)

    url = REMOTE_URL+'/_search?q=itemid:'+data+'&size=1'
    out = urllib2.urlopen(url)
    res = out.read()
    res = json.loads(res)

    return res

def SearchDataOnRelated(data):
    #open the URL
    url = REMOTE_URL+'/_search?q=related:'+data+'&size=5'
    out = urllib2.urlopen(url)
    res = out.read()
    res = json.loads(res)

    return res

def SearchDataOnMeta(data):

    #authenticate the ES URL
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, REMOTE_URL, USR, PWD)
    auth_handler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)

    #open the URL
    url = REMOTE_URL+'/_search?q=meta:'+data+'&size=5'
    out = urllib2.urlopen(url)
    res = out.read()
    res = json.loads(res)

    return res


def SearchDataOnBody(data):
    url = URL+'/_search?q=body:'+data+'&size=5'
    req = urllib2.Request(url)
    out = urllib2.urlopen(req)
    res = out.read()
    #print res
    # returned data is JSON
    res = json.loads(res)
    # total number of results
    #print data['hits']['total']
    lst = []
    #code to get at the _source
    for hit in res['hits']['hits']:
        d = {}
        d['hit'] = (hit["_source"])
        lst.append(d)
    #print res
    #return json.dumps(lst)
    return res



'''


'''
#SearchDataOnTitle('charge')
#otherSearch('charge')
#res = SearchDataOnBody('mortgage')
#print (res["hit"])

#res = NewSearchOnItem('chargeWithTransferLease')
#res = NewSearchOnId('legalEquitableCharge')
#res = NewSearchContent('specifically')

#print (res)'''

'''res = NewSearchDataOnContent('and', 'score', 10, 1)
#print res
hit = res['hits']['hits']
#print hit
for hit in res['hits']['hits']:
    #print hit
    for ids in hit['_source']['kmlinks']:
        print ids
        articleId = ids['id']
        print articleId'''

'''class Facet(object):
    def __init__(self, name):
        self.name = name
        self.foci_list = []

    def add_foci(self, foci):
        self.foci_list.append(foci)

fields = ["scope", "title", "keywords^5"]
facets = []
data = Facet('appn_type')
data.add_foci('tp')
facets.append(data)
data = Facet('colour')
data.add_foci('red')
data.add_foci('green')
facets.append(data)

res = NewSearchwithFoci('lion', 'score', 20, 1, fields, 'desc', facets)'''

#print res

#{"took":3,"timed_out":false,"_shards":{"total":1,"successful":1,"failed":0},"hits":{"total":1,"max_score":1.0,"hits":[{"_index":"knowledge","_type":"information","_id":"1","_score":1.0,"_source":{"itemid": "1", "body": "I want a mortgage", "tag": "mortgage, charge, want", "subtitle": "mortgage", "title": "charge"}}]}}


#{u'hits': {u'hits': [{u'_score': 1.0, u'_type': u'information', u'_id': u'1', u'_source': {u'itemid': u'1', u'body': u'I want a mortgage', u'tag': u'mortgage, charge, want', u'subtitle': u'mortgage', u'title': u'charge'}, u'_index': u'knowledge'}], u'total': 1, u'max_score': 1.0}, u'_shards': {u'successful': 1, u'failed': 0, u'total': 1}, u'took': 3, u'timed_out': False}
