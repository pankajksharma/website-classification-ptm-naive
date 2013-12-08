import json, MySQLdb
from lib.mysql import connection

data_set = {
    'entertain'  : [],
    'politics'   : [],
    'econonics'  : [],
    'sports'     : [],
    'education'  : [],
    'religion'   : [],
    'health'     : [],
    }

data_counts= {
    'entertain'  :0,
    'politics'   :0,
    'econonics'  :0,
    'sports'     :0,
    'education'  :0,
    'religion'   :0,
    'health'     :0,
    }

cursor = connection.cursor()
query = "SELECT * FROM `data_new` WHERE `dp` <> 'Null' "
cursor.execute(query)
data = cursor.fetchall ()
count  = 0

#Divide data assuming each belongs to single category
for row in data :
    cat = json.loads(row[2])[0]
    data_set[cat].append(row)    #Append 
    data_counts[cat] += 1

for i in range(10):
    model = ModelCreator(i, data_set, data_counts)
    model.create()
    tester = ModelTester(i, data_set, data_counts)
    tester.test()