from prettytable import PrettyTable
import os

tbl = PrettyTable(['FilePath','FileSize'])

DIR = 'c:/'
fileList = os.listdir(DIR)
for eachFile in fileList:
    filePath = os.path.join(Dir, eachFile)
    if os.path.isfile(filePath):
        fileSize = os.path.getsize(filePath)
        tbl.add_row( [ filePath, fileSize] )
        
tbl.align = "1"
resultString = tbl.get_string(sortby="FileSize", reversesort=True)
print(resultString)
