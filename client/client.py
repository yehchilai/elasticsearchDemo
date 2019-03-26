from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(['http://user:secret@localhost:9200/'])

result = es.get(index="bank", doc_type='account', id=1)

# print(result)

body = {
  "size": 0,
  "aggs": {
    "state-type": {
      "terms": {
        "field": "state.keyword"
      },
      "aggs": {
        "money": {
          "avg": {
            "field": "balance"
          }
        },
        "gender":{
          "terms": {
            "field": "gender.keyword"
          },
          "aggs": {
            "income": {
              "avg": {
                "field": "balance"
              }
            }
          }
        }
      }
    }
  }
}

search_result = es.search(index='bank', doc_type='account', body=body)
total = search_result['hits']['total']
state = search_result['aggregations']['state-type']['buckets'][0]['key']
income = search_result['aggregations']['state-type']['buckets'][0]['gender']['buckets'][0]['income']['value']

print('hit_total: {x}, state: {y}, male average income: {z}'.format(x=total, y=state, z=state))