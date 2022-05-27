import pymysql

def iud(qry,val):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="ila")
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id


def selectall(qry):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="ila")
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    con.commit()
    con.close()
    return res

def selectall2(qry,val):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="ila")
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchall()
    con.commit()
    con.close()
    return res


def selectone(qry,val):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="ila")
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchone()
    con.commit()
    con.close()
    return res



def androidselectall(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='ila')
    cmd=con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

def androidselectallnew(q):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='ila')
    cmd=con.cursor()
    cmd.execute(q)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data



