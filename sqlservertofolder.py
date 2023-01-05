import mysql.connector
import base64
from PIL import Image
import io
from io import BytesIO
from base64 import b64decode 
import sqlite3
import pyodbc 

  
# Create a connection
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-EM7D5DR;DATABASE=jaipur121;Trusted_Connection=yes;')

cursor = conn.cursor()
#query = 'SELECT  rollno FROM results where rollno = 31320003'
query = 'SELECT  rollno,imagedata FROM imagedata where rollno = 332233936'

cursor.execute(query)
  
data = cursor.fetchall()
#print(data)
rollno = '332233936'
for i in data:
    #print(i)
     #print('name===========',i[0])
    #print('image===========',i[1])
    #Rollno=i[0]
    image=i[1]
    #print(image)
    #print(image)
    # Decode the string
    im = Image.open(BytesIO(b64decode(image.split(',')[1])))
    filepath='D:/images/'
    im.save(filepath+'/'+str(rollno)+'.jpg')

  
# Display the image 
#im.show()
#im.save()'''