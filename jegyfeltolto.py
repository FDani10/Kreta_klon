# Mindegyik diáknak, minden tárgyból (ami van neki) ad 10 random jegyet

import mysql.connector
import random

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()
querry = "SELECT diak.diak_id,tanora.tanora_id FROM `diak` inner JOIN osztaly on osztaly.osztaly_id = diak.diak_osztaly INNER JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id;"
cursor.execute(querry)
table = cursor.fetchall()

for row in table: 
    for _ in range(10):
        rN = random.randint(1,5)
        querry2 = "INSERT INTO `jegy`(`tanora_id`, `diak_id`, `beirt_jegy`) VALUES ('"+str(row[1])+"','"+str(row[0])+"','"+str(rN)+"')"
        cursor.execute(querry2)

con.commit()
print(cursor.rowcount, "record inserted.")