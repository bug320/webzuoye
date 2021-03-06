#-*- coding:utf-8 -*-
#!/usr/bin/python2

import MySQLdb as DB

class MySQL(object):
    def __init__(self,host="localhost",usr="root",passwd="root",dbase="webpy"):
        self.conn = DB.connect(host,usr,passwd,dbase, charset='utf8')
        # 这里让 查询结果不再是 tuple 类型 而是 字典的形式返回
        self.cursor =self.conn.cursor(cursorclass = DB.cursors.DictCursor)
        pass
    def close(self):
        self.conn.close()
        pass
    def insert(self,table,**item):
        keys = ""
        values = ""
        
        for key,value in item.items():
            #debug start
            #print "key=",key
            #print "value=",value,"type(value)=",type(value)
            #debug end
            keys = keys + ","+key
            values = values + ",\"" + value +"\""
            # debug start
            #print "OO"
            #print "keys=",keys
            #print "values=",values
            # debug end
            pass
        keys = keys[1:]
        values = values[1:]
        ## debug start
        print keys
        print values
        ## debug end
        try :
            sql = "INSERT INTO %s( %s ) VALUES( %s )" % (table,keys,values)
            #debug start
            ##INSERT INTO SYS(loopSize,lengthSize) VALUES ("7","4")
            #  print "sql = ",sql
            #debug end
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e :
            self.conn.rollback() 
            print "insert error --- ",e
        pass
    #def select(self,table):
    #    #result = []
    #    try:
    #        self.cursor.execute("SELECT * FROM %s" % table )
    #        result = self.cursor.fetchall()
    #        return result
    #    except Exception as e :
    #        self.conn.rollback()
    #        print "select error ---  ",e
    #        return None
    #    pass
    def select(self,table,where=None,*slc):
        sln = len(slc)
        slec = ""
        if sln:
            for it in slc:
                slec = slec + "," + it
            slec = slec[1:]
        else:
            slec ="*"
        try:
            if where:
                sql = "SELECT %s FROM %s WHERE %s" % (slec,table,where)
            else:
                sql = "SELECT %s FROM %s " % (slec,table)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
            pass
        except Exception as e:
            self.conn.rollback()
            print "select error ----" ,e
            return None
            pass
                
        pass
   # def select(self,table,sql):
   #     try:
   #         self.cursor.execute(sql)
   #         result = self.cursor.fetchall()
   #         return result
   #     except Exception as e:
   #         self.conn.rollback()
   #         print "select error --- ",e
   #     pass
    
    def update(self,table,**args):
        where = args.get("where")
        if where:
            del args["where"]
        sets = ""
        for key,value in args.items():
            sets = sets + "," + key + "=\"" + value + "\"" 
        try:
            if where:
                sql = "UPDATE %s SET %s WHERE %s" % (table,sets,where)
            else:
                sql = "UPDATE %s SET %s "  % (table,sets)
            pass
        except Exception as e:
           self.conn.commit()
           print "Update Error ---" ,e
           pass
        pass

    # def update(self,table,sql):
    #     try:
    #         self.cursor.execute(sql)
    #         self.conn.commit()
    #     except Exception as e:
    #         self.conn.commit()
    #         print "Update Error ---" ,e
    #         pass
    #
    #     pass
    
    def delete(self,table,**args):
        where = args.get("where")
        try:
            if where :
                sql = "DELETE FROM %s WHERE %s" % (table,where)
            else:
                sql = "DELETE FROM %s" % (table)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self,conn.rollback()
            print  "Delete ERROR ---",e
        pass
   #def delete(self,table,sql):
   #     # sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
   #     try :
   #         self.cursor.execute(sql)
   #         self.conn.commit()
   #         pass
   #     except Exception as e :
   #         self,conn.rollback()
   #         print "Delete Error! --- ",e
   #         pass
   #     pass
   # pass
if __name__ == "__main__":
    db = MySQL()
    #db.insert("SYS",loopSize="7",lengthSize="4")
    db.delete("SYS",where=" loopSize='17' ")
    #db.delete("SYS","DELETE FROM SYS WHERE loopSize='17' ")
    result = db.select("SYS")
    print type(result)
    print result


