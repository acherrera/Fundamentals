# Commands


Just showing some the commands that are used in elastic search and taking notes


**Note:** Need to alias to make this all work correctly. For some reason the
tutorial doesn't explain this but.... 

    GET /_cat/health?v 

Should actually put in the terminal as

    curl -X GET "localhost:9200/_cat/health?v"

For this reason I would recommend aliasing the command like so

    elastiget () { curl -X GET "localhost:9200$1" }
    elastiput () { curl -X PUT "localhost:9200$1" }

**BUT** Once you get into putting json data, the method becomes much, much more
difficult. For this reason, just run the command through Kibana. Download it,
run it, open web browser and go to localhost:5601


## Basic Commands

    GET /\_cat/health?v     - shows the health of cluster
    GET /\_cat/nodes?v      - shows nodes in cluster 
    GET /\_cat/indices?v    - shows indices
    PUT /\customer?pretty   - add customer index. Pretty print response
    PUT /customer/_doc/1?pretty
    {
      "name": "John Doe"
    }                       - Puts item in location
    
    GET /customer/\_doc/1?pretty    - Request ID 1
    DELETE /customer?pretty - DELETE customer index

    <REST Verb> /<Index>/<Type>/<ID>    - General Notation
    Index - created index
    Type - type associated with data
    ID - Id


## Modifying Data

If running the PUT command above multiple times, it will overwrite the data at
the location. Would need to change the '1' to a '2' to specify ID=2 for the
next case. But we do not need to even do this, it can be handled automatically
with:

    POST /customer/\_doc?pretty
    {
      "name": "Jane Doe"
    }

Here an ID will be randomly generated. Note that we use POST  instead of PUT


## Updating

Update with

    POST /customer/_doc/1/_update?pretty
    {
      "doc": { "name": "Jane Doe" }
    }

Now want to add age field?

    POST /customer/_doc/1/_update?pretty
    {
      "doc": { "name": "Jane Doe", "age": 20 }
    }

Script the update: 

    POST /customer/_doc/1/_update?pretty
    {
      "script" : "ctx._source.age += 5"
    }

Here, 'ctx.\_source.age' means the source document. Simple enough.


## Deleting document

Once again, don't overthink it. 

    DELETE /customer/_doc/2?pretty

Deletes customer with ID=2


## Bulk options

Because who wants to push one at a time? Easy, peasy

    POST /customer/_doc/_bulk?pretty
    {"index":{"_id":"1"}}
    {"name": "John Doe" }
    {"index":{"_id":"2"}}
    {"name": "Jane Doe" }


Now update and delete at the same item


    POST /customer/_doc/_bulk?pretty
    {"update":{"_id":"1"}}
    {"doc": { "name": "John Doe becomes Jane Doe" } }
    {"delete":{"_id":"2"}}



# Exploring realistic data

Downloaded a bit set of data and threw into our database using

    curl -H "Content-Type: application/json" -XPOST \
        "localhost:9200/bank/_doc/_bulk?pretty&refresh" --data-binary "@accounts.json"
    curl "localhost:9200/_cat/indices?v"


That step wasn't explained great, but just go with it. The important part is
that the data loaded in was called 'accounts.json' so that it likely what the
--databinary flag is for

## PROTIP!! 
Use this link to make BS json data

http://www.json-generator.com/

## Search API

Can be accessed from the \_search endpoint like so:

    GET /bank/_search?q=*&sort=account_number:asc&pretty
    q=*                     - matches all
    sort=account_number:asc - sort ascending 
    pretty                  - makes it pretty

Can also do the search by passing JSON data

    GET /bank/_search
    {
      "query": { "match_all": {} },
      "sort": [
        { "account_number": "asc" }
      ]
    }

This method is done through a Domain Specific Language (DSL). AKA, they just
kind of made it up because JSON is so cool.


    GET /bank/_search
    {
      "query": { "match_all": {} },
      "from": 10,
      "size": 10
    }

This starts at ten and will return ten. If 'from' not specified, will start at
0

    GET /bank/_search
    {
      "query": { "match_all": {} },
      "sort": { "balance": { "order": "desc" } }
    }

Returns all, sorts by balance and orders descending


### More Searching!

    GET /bank/_search
    {
      "query": { "match_all": {} },
      "_source": ["account_number", "balance"]
    }

Will only return the account_number and the balance. Similar to SQL select
function. 


Can use "match" in many different ways.

    GET /bank/_search
    {
      "query": { "match": { "account_number": 20 } }
    }

This will match account_number = 20 

    GET /bank/_search
    {
      "query": { "match": { "address": "mill lane" } }
    }

**TRICKY**. This one will match 'mill' or 'lane' in the address field

    GET /bank/_search
    {
      "query": { "match_phrase": { "address": "mill lane" } }
    }

This one will match only 'mill lane' in the address field

#### Boolean Searching! 
    GET /bank/_search
    {
      "query": {
        "bool": {
          "must": [
            { "match": { "address": "mill" } },
            { "match": { "address": "lane" } }
          ]
        }
      }
    }

Must contain both

    GET /bank/_search
    {
      "query": {
        "bool": {
          "should": [
            { "match": { "address": "mill" } },
            { "match": { "address": "lane" } }
          ]
        }
      }
    }

Can contain either one

    GET /bank/_search
    {
      "query": {
        "bool": {
          "must_not": [
            { "match": { "address": "mill" } },
            { "match": { "address": "lane" } }
          ]
        }
      }
    }

Can not have either one


    GET /bank/_search
    {
      "query": {
        "bool": {
          "must": [
            { "match": { "age": "40" } }
          ],
          "must_not": [
            { "match": { "state": "ID" } }
          ]
        }
      }
    }

Must match age, but not match state

#### Searching even more!!! 

    GET /bank/_search
    {
      "query": {
        "bool": {
          "must": { "match_all": {} },
          "filter": {
            "range": {
              "balance": {
                "gte": 20000,
                "lte": 30000
              }
            }
          }
        }
      }
    }

"query of boolean must match_all and filter range based on 'balance' anything
greater than or equal (gte)20000 and less than or equal (lte) 30000". Long,
yes. Difficult, not so much


## Aggregation
Group data, and extract from that group. 

