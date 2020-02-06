import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='hp1617wy',
                             password='Arp182019',
                             db='hp1617wy_',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

searchName = input("Enter search term: ")
print(searchName)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * FROM Student WHERE FirstName = " + " '" + searchName + "'"
        print(sql)
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
