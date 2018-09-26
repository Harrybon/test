# pymongo.py

from pymongo import MongoClient
#连接数据库
conn = MongoClient('localhost',27017)
#创建数据库对象
db = conn.stu
#创建集合对象
myset = db.class4
myset1 = db.class0
#操作
# print(dir(myset))

# myset.insert({'name':'张铁林','King':'乾隆'})
# myset.insert([{'name':'张国立','King':'康熙'},{'name':'陈道明','King':'康熙'}])
# myset.insert_many([{'name':'唐国强','King':'雍正'},{'name':'陈建斌','King':'雍正'}])
# myset.insert_one({'name':'郑少秋','King':'乾隆'})
# myset.save({'_id':1,'name':'聂远','King':'乾隆'})
# myset.save({'_id':1,'name':'吴奇隆','King':'四爷'})
# for i in myset.find({},{'_id':0}):
#     # print(i)
#     print(i['name'],'---',i['King'])
# print('*****************************************')
# print(myset.find_one())
# print('******************************************')
# print(myset.find_one({'name':'陈道明'},{'_id':0}))
# print('*****************************************')
# for i in myset.find({'_id':{'$eq':1}}):
#     print(i)
# print(myset.find_one({'_id':{'$eq':1}}))
# cursor = myset.find({},{'_id':0})

# print(cursor.next())
# for i in cursor.skip(3).limit(3):
#     print(i)
# for i in cursor.sort([('name',-1)]):
#     print(i)

# for i in myset1.find({'$or':[{'gender':'w'},{'age':{'$lt':19}}]},{'_id':0}):
#     print(i)
# print(myset1.find_one({'name':'sisi'},{'_id':0}))
# myset1.update({'name':'sisi'},{'$unset':{'tel':''}})
# print(myset1.find_one({'name':'sisi'},{'_id':0}))
# print(myset1.find_one({'name':'Tom'},{'_id':0}))
# myset1.update({'name':'Tom'},{'$set':{'age':20}},multi=True)
# print(myset1.find_one({'name':'Tom'},{'_id':0}))
# myset.update({'name':'梁家辉'},{'$set':{'King':'咸丰'}},upsert=True)
# myset.update_many({'King':'咸丰'},{'$set':{'name':'阿辉'}})
# myset.update_one({'King':'康熙'},{'$set':{'king_name':'玄烨'}})

# 删除

# myset.remove({'King':'四爷'})
# myset.remove({'King':'咸丰'},multi=False)
# myset1.remove({'gender':'w'},multi=True)
print(myset.find_one_and_delete({'King':'咸丰'}))


print('操作成功')
conn.close() 