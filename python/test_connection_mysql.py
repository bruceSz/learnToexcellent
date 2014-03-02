import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='test',passwd='123456',db='test',port=3306)
    cur = conn.cursor()
    count = cur.execute('select * from test')

    result = cur.fetchone()
    print result

    results = cur.fetchmany(5)

    for r in results:
        print r
    
    cur.scroll(0,mode='absolute')
    results = cur.fetchall()
    for r in results:
        print r[1]

    cur.close()
    conn.close()

except MySQLdb.Error as e:
    print "Mysql Error %d: %s" %(e.args[0],e.args[1])

