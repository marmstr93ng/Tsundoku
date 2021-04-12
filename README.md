# Tsundoku
Lightweight library application

## Setup
* Note: Ensure Enviromental Var PYTHONPATH is set to .

## TODO
* Parse google book results
* Display total number of items found, json_data["totalItems"]
* Display search results

## IDEAS
* Personal Book Report - One thing learned
* Read status
* Num books read tracking
* Books not in library but read also tracked

api = API()
try:
    json_data = api.search("14441651")
except Exception as e:
    print(e)