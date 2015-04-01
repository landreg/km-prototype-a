import urllib2
import json
import array
import requests


#alex's test database
#REMOTE_URLcred = 'https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/km_alex_test/information'

#main test database
#REMOTE_URLcred = 'https://cp94zbqxv3:estftr8mkx@km-prototype-1076374862.eu-west-1.bonsai.io/new_kmow_man/information'

#Main database
REMOTE_URLcred = 'http://gl-know-ap33.lnx.lr.net:9200/knowledge_manage/information'


def NewSearchDataOnId(data):
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
    data2 = '}}, '   
    data3 = '{"match": {"facets.foci": '    
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
                nested_data = nested_data + data3 +'"'+ foci +'"'+ data5 + data4
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