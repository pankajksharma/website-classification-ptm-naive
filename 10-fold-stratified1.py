import json, MySQLdb
from lib.mysql import connection
from lib.model_creater import ModelCreator
from lib.model_tester import ModelTester

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

true_cases = 0.0
all_cases = sum([v for v in data_counts.values()])
for i in range(10):
    print i
    model = ModelCreator(i, data_set, data_counts, 'dp')
    model.create()
    tester = ModelTester(i, data_set, data_counts, 'words', 'dp-word')
    true_cases += tester.test()
print true_cases/all_cases
