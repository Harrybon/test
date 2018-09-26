# mongofilesmal.py
#小文件存储
from pymongo import MongoClient
import bson.binary

conn = MongoClient('127.0.0.1',27017)
db = conn.image
myset = db.MM


#存储图片
# f = open('mm.jpg','rb')
# content = bson.binary.Binary(f.read())
# myset.insert({'filename':'mm.jpg','data':content})
#提取图片

img = myset.find_one({'filename':'mm.jpg'})
#将内容写入本地

with open('mm.jpg','wb') as f:
    f.write(img['data'])


conn.close()