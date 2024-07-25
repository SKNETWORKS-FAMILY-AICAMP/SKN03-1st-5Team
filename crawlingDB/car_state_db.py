import pymysql
import pandas as pd

read_data = pd.read_csv("car_info.csv", delimiter='\t')
con = pymysql.connect(host='localhost', user='root', password='root1234', db='car_registration_status', charset='utf8', autocommit=False) 
cur = con.cursor(pymysql.cursors.DictCursor)

for i in range(len(read_data)):
    city = read_data["시도명"][i]
    gun_gu = read_data["시군구"][i]

    for j in range(4):
        usages = j
        offical_car = int(read_data[f"관용{j}"][i].replace(",",""))
        own_car = int(read_data[f"자가용{j}"][i].replace(",",""))
        commercial = int(read_data[f"영업용{j}"][i].replace(",",""))
        total = int(read_data[f"계{j}"][i].replace(",",""))
        sql = "INSERT INTO car_data (city, gun_gu, usages,offical_car, own_car,commercial,  total) VALUES (\"%s\", \"%s\", %d, %d, %d, %d, %d);" % (city, gun_gu, usages,offical_car, own_car,commercial,  total)

        cur.execute(sql)
cur.execute('commit;')