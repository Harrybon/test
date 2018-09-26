# mongoloda.py

from pymongo  import MongoClient
import gridfs

conn = MongoClient('127.0.0.1',27017)

db =conn.grid

fs = gridfs.GridFS(db)
files = fs.find()
for i in files:
    if i.filename == 'mm.jpg':
        with open(i.filename,'wb') as f:
            data = i.read()
            f.write(data)
print('Done')
conn.close()
