import tornado
import pymongo

conn = pymongo.Connection("localhost",27017)#(... "mongodb://user:password@staff.mongohq.com:10066/your_mongohq_db")
#·····················
#创建到MongoDB的链接↑(端口默认)
#·····················

