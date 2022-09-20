# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io
from io import BytesIO
from base64 import b64decode 
import sqlite3
  
# Create a connection
sqliteConnection = sqlite3.connect('add db file path')
                #print("==================",sqliteConnection)
                # program logic goes here
cursor = sqliteConnection.cursor()
cursor1 = sqliteConnection.cursor()
print("Database Successfully Connected to SQLite")
  
  
# Prepare the query
query = 'SELECT rollno,photo FROM candidateinfo '
  
# Execute the query to get the file
cursor.execute(query)
  
data = cursor.fetchall()
print(data)
for i in data:
    print(i)
     #print('name===========',i[0])
     #print('image===========',i[1])
    Rollno=i[0]
    image=i[1]
    print(image)
    # Decode the string
    im = Image.open(BytesIO(b64decode(image.split(',')[1])))
    filepath='C:/Users/ramesha/ZI/images/'
    im.save(filepath+'/'+str(Rollno)+'.jpg')

  
# Display the image 
#im.show()
#im.save()'''

  

