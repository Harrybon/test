# mongo1.py

from pymongo import MongoClient

from random import randint
conn = MongoClient('localhost',27017)

db = conn.grade

# myset = db.class4
myset1 = db.class0

#索引
# index = myset.ensure_index('name')
# print(index)
# index = myset.ensure_index([('age',-1)])
# for i in myset.list_indexes():
#     print(i)
#删除所有索引
# myset.drop_indexes()
#按索引名称删除，单个索引
# myset.drop_index('name_1')
#创建复合索引
# myset.ensure_index([('name',1),('age',-1)])
# myset.drop_index('name_1_age_-1')
# myset.ensure_index('name',name = 'MyIndex',unique = True)
# myset.ensure_index('age',sparse = True)

# 聚合操作
# p = [
#     {'$group':{'_id':'$King','count':{'$sum':1}}},
#     {'$match':{'count':{'$gt':1}}}
#     ]
# cursor = myset.aggregate(p)
# for i in cursor:
#     print(i)
cursor = myset1.find()

for i in cursor:
    myset1.update({'_id':i['_id']},{'$set':{'score':{'chinease':randint(60,100),'math':randint(60,100),'english':randint(60,100)}}})

# l1 = [{'$group':{'_id':'$gender','num':{'$sum':1}}}]
l2 = [{'$match':{'gender':'m'}},{'$project':{'_id':0,'name':1,'score.chinease':1}}]
# l3 = [{'$match':{'gendre':'w'}},{'$sort':{'score.english':-1}}]
cursor = myset1.aggregate(l2)

for i in cursor:
    print(i)
print('Done')
conn.close()