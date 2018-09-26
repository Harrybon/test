# mongofile.py  grid

from pymongo  import MongoClient
import gridfs

conn = MongoClient('127.0.0.1',27017)

db =conn.grid

fs = gridfs.GridFS(db)
f = open('mm.jpg','rb')
fs.put(f.read(),filename = 'mm.jjpg')
conn.close()

