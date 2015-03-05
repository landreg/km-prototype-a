import urllib2
import json
#from elasticsearch import Elasticsearch
import array
#import requests


URL = 'http://192.168.50.7:9200/knowledge/information'
ES_HOST = {"host" : "http://192.168.50.7", "port" : 9200}
INDEX_NAME = 'knowledge'
TYPE_NAME = 'information'
REMOTE_URL = 'https://km-prototype-1076374862.eu-west-1.bonsai.io/knowledge/information'
#cp94zbqxv3:estftr8mkx@
USR = 'cp94zbqxv3'
PWD = 'estftr8mkx'

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

def SearchDataOnMeta(data):

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, REMOTE_URL, USR, PWD)
    auth_handler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)

    url = REMOTE_URL+'/_search?q=meta:'+data+'&size=5'
    out = urllib2.urlopen(url)

    

    #req = urllib2.Request(url)
    #out = urllib2.urlopen(url)
    res = out.read()
    #print data
    # returned data is JSON
    res = json.loads(res)
    # total number of results
    #print data['hits']['total']

    #code to get at the _source
    #for hit in data['hits']['hits']:
        #print = (hit["_source"])

    return res

"""def GetAllData():
    # create ES client, create index
    es = Elasticsearch(hosts = [ES_HOST])
    #res = es.search(index = INDEX_NAME, size=4, body={"query": {"query_string": {"query": data}}})
    data = es.search(index = INDEX_NAME, size=4, body={"query": {"match_all": {}}})
    #print(" response: '%s'" % (res))
    return data"""

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

"""def buildingData():
        url = "http://192.168.50.4:5000/BGREST/api/data"
        payload = json.dumps({'title': title, 'address': address, 'type': appType})
        headers = {'content-type': 'application/json'}
        r = requests.post(REMOTE_URL, data=payload, headers=headers)
        flash(r.text)
        flash(r.status_code)"""



#SearchDataOnTitle('charge')
#otherSearch('charge')
#res = SearchDataOnBody('mortgage')
#print (res["hit"])





#{"took":3,"timed_out":false,"_shards":{"total":1,"successful":1,"failed":0},"hits":{"total":1,"max_score":1.0,"hits":[{"_index":"knowledge","_type":"information","_id":"1","_score":1.0,"_source":{"itemid": "1", "body": "I want a mortgage", "tag": "mortgage, charge, want", "subtitle": "mortgage", "title": "charge"}}]}}


#{u'hits': {u'hits': [{u'_score': 1.0, u'_type': u'information', u'_id': u'1', u'_source': {u'itemid': u'1', u'body': u'I want a mortgage', u'tag': u'mortgage, charge, want', u'subtitle': u'mortgage', u'title': u'charge'}, u'_index': u'knowledge'}], u'total': 1, u'max_score': 1.0}, u'_shards': {u'successful': 1, u'failed': 0, u'total': 1}, u'took': 3, u'timed_out': False}
