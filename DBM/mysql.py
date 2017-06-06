#-*- coding:utf-8 -*-
#!/usr/bin/python2

import MySQLdb as DB

class MySQL(db):
    def __init__(self,host="hostlocal",usr="root",passwd="root",dbase="webpy"):
        self.conn = DB.connect(host,usr,passed,dbase)
        self.cursor = conn.cursor()
        pass
    def insert(self,table,**item):
        keys = ""
        valuse = ""
        
        for key,value in item:
            keys = keys.join(",").join(item)
            values = valuse.join(","+'"').join(value).join('"')
            pass
        keys = keys[1:]
        values = valuse[1:]
        self.cursor.execute("INSERT INTO %s\( %s \) VALUES\(  \) ")
        pass
    pass

