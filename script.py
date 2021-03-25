


import sqlite3
liste = list()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect(path):
    con = sqlite3.connect(path)
    con.row_factory = dict_factory
    cursor = con.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table_name in tables:
        cur1 = con.cursor()
        cur1.execute("Select * from "+table_name["name"])
        results = cur1.fetchall()

        for i in results:
            dumylist = {table_name["name"] : i}
            liste.append(dumylist)
    
    with open(table_name["name"]+".json",'w') as newfile:
        newfile.write("[\n")
        for i in liste:
            newfile.write(str(i))
            newfile.write("\n,")
        newfile.write("\n]")
    newfile.close()

def connect_comp(path,query):
    con = sqlite3.connect(path)
    con.row_factory = dict_factory
    cursor = con.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table_name in tables:
        cur1 = con.cursor()
        cur1.execute(query)
        results = cur1.fetchall()

        for i in results:
            dumylist = {table_name["name"] : i}
            liste.append(dumylist)
    
    with open(table_name["name"]+".json",'w') as newfile:
        newfile.write("[\n")
        for i in liste:
            newfile.write(str(i))
            newfile.write("\n,")
        newfile.write("\n]")
    newfile.close()

#Enter your path here    
connect("YOUR DB PATH")
# OR
#connect("YOUR DB PATH", "YOUR QUERY")
