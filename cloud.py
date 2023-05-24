import requests
from bs4 import BeautifulSoup
import mysql.connector as con

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
source = requests.get(url)
soup = BeautifulSoup(source.text,'html.parser')
movies = soup.find('tbody',class_="lister-list")
count=0
pictures=[]
dic={}#has name and rank as key
year=[]
for title in soup.find_all('td',class_='titleColumn'):
	if count==10:
		break
	lst2 = title.text.strip().split('\n')
	lst2[0]=lst2[0].replace('.','')
	lst2[1]=lst2[1].strip()
	dic[lst2[0]]=lst2[1]
	year.append(title.find('span',class_='secondaryInfo').text.strip('()'))
	count+=1
count = 0
for pic in soup.find_all('td',class_='posterColumn'):
	if count==10:
		break
	img = pic.find('img')
	pictures.append(img['src'])
	count+=1

#sql part
Db = con.connect(
	host="localhost",
	user="root",
	password="",
	database="demo"
)
cursor = Db.cursor()
cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'movies'")
res = cursor.fetchone()

if res[0]==0:
	cursor.execute('''
		CREATE TABLE movies(
			id INT NOT NULL,
			title VARCHAR(255),
			year int,
			img VARCHAR(255),
			PRIMARY KEY(id)
			
		)

	''')
	Db.commit()

for i,v in enumerate(dic):
	cursor.execute("SELECT * FROM movies WHERE id=%s AND title=%s",(v,dic[v]))
	isExist = cursor.fetchone()
	if isExist:
		if str(isExist[1])==str(dic[v]):
			continue
		sql = "UPDATE movies SET title=%s,year=%s,img=%s WHERE id=%s"
		que = (div[v],year[i],pictures[i],v)
		cursor.execute(sql,que)
	else:
		cursor.execute("INSERT INTO movies VALUES(%s,%s,%s,%s)",(v,dic[v],year[i],pictures[i]))

Db.commit()
cursor.close()
Db.close()