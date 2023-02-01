
import json
import sys

data1 = { "a": 
            {"b": 
            {"c":"d"
        }
    }
 }

searchkey=sys.argv[1]

def get_value(myobject, key):
    if type(myobject) == str:
        myjson = json.loads(myobject)
    if type(myobject) is dict:
        for jsonkey in myobject:
            if type(myobject[jsonkey]) in (list, dict):
                get_value(myobject[jsonkey], key)
            elif jsonkey == key:

                print(myobject[jsonkey])

    elif type(myobject) is list:
        for item in myobject:
            if type(item) in (list, dict):
                get_value(item, key)

get_value(data1,searchkey)
