from pickle import TRUE
import sqlite3
from unittest import skip
import mysql.connector
from mysql.connector import Error 
import mysql.connector
from PIL import Image
from io import BytesIO
import os
import shutil
path = r'C:\Users\ramesha\ZI\databases'
for f in os.walk(path):
        #print("================",f[2])
        for f1 in f[2]:
            if  f1.startswith('ttipl_bio_reg_db'):
                #print('=========',os.path.join(f[0],f1))
                sqliteConnection = sqlite3.connect(os.path.join(f[0],f1))
                #print("==================",sqliteConnection)
                # program logic goes here
                cursor = sqliteConnection.cursor()
                cursor1 = sqliteConnection.cursor()
                print("Database Successfully Connected to SQLite")
                
                try:
                    cursor.execute('select Rollno,Appno,Name,FatherName,DOB,VerifiedTime,VerifiedStatus,tokenno,operator_name,operator_id,locationid,device_id from candidateinfo where VerifiedStatus is not null')
                    cursor1.execute('select Rollno,Photo_REG,FPImage_LTI_REG,FPImage_RTI_REG from candidateinfo where VerifiedStatus is not null')
                    record = cursor.fetchall()
                    record2 = cursor1.fetchall()
                    cursor.close()
                    try:
                        connection = mysql.connector.connect(host='localhost',
                                                            database='sample3',
                                                            user='root',
                                                            password='root')
                        mySql_Create_Table_Query = """CREATE TABLE table1 ( 
                                                Rollno int(20) NOT NULL,
                                                Appno varchar(100) NOT NULL,
                                                Name varchar(250) NOT NULL,
                                                FatherName varchar(250),
                                                DOB TEXT,
                                                VerifiedTime TEXT,
                                                VerifiedStatus INT,
                                                tokenno TEXT,
                                                operator_name TEXT,
                                                operator_id TEXT,
                                                locationid TEXT,
                                                device_id TEXT,
                                                PRIMARY KEY (Rollno)) """
                        
                        cursor = connection.cursor()
                        result = cursor.execute(mySql_Create_Table_Query)
                        print("table1 Table created successfully ")

                    except mysql.connector.Error as error:
                        print("Failed to create table in MySQL: {}".format(error))
                    finally:
                        if connection.is_connected():
                            cursor.close()
                            print("MySQL connection is closed")
                    for record1 in record:        
                        mySql_insert_query = """INSERT INTO table1 (Rollno,Appno,Name,FatherName,DOB,VerifiedTime,VerifiedStatus,tokenno,operator_name,operator_id,locationid,device_id)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        val=(record1)
                        cursor = connection.cursor()
                        cursor.execute(mySql_insert_query,val)
                        connection.commit()
                    else:
                        print('Records inserted successfully')
                    rowscount='select count(*) from table1'
                    cursor.execute(rowscount)
                    RAM=cursor.fetchall()
                    print(RAM, "Record inserted successfully into table1")
                    
                    #images saving in folders
                    for i in record2:
                        Rollno=i[0]
                        image=i[1]
                        fpl=i[2]
                        fpr=i[3]
                        
                        # Decode the images
                        imp = Image.open(BytesIO(image))
                        rgb_imp = imp.convert('RGB')
                        iml = Image.open(BytesIO(fpl))
                        rgb_iml = iml.convert('RGB')
                        imr = Image.open(BytesIO(fpr))
                        rgb_imr = imr.convert('RGB')
                        filepath='C:/Users/ramesha/ZI/images/'
                        filepath1='C:/Users/ramesha/ZI/fpdata/'
                        #filepath2='C:/Users/ramesha/ZI/fprti/'
                        rgb_imp.save(filepath+'/'+str(Rollno)+'.jpg')
                        rgb_iml.save(filepath1+'/'+str(Rollno)+'_lti1.jpg')
                        rgb_imr.save(filepath1+'/'+str(Rollno)+'_rti1.jpg')
                        cursor.close()
                    else:
                        print('Images Saved In Folders')
                except sqlite3.Error as error:
                        sqliteConnection.close()
                        print(" ", error)
                        source=os.path.join(f[0],f1)
                        destination=r'C:\Users\ramesha\ZI\error-databases'
                        shutil.move(source, destination)
                finally:
                        # sqliteConnection
                        # sqliteConnection.close()
                        # source=os.path.join(f[0],f1)
                        # destination=r'C:\Users\ramesha\ZI\completed_db_files'
                        #shutil.move(source, destination)
                        #print('Database is Readed')
                        print("The SQLite connection is closed")
                        #mysql connection query
                
            else:
                source=os.path.join(f[0],f1)
                destination=r'C:\Users\ramesha\ZI\non_db_files'
                shutil.move(source, destination)
                print('Database Not Connected')
        else:
            print('No Database To Connect In Folder')
else:
    source = 'C:/Users/ramesha/ZI/databases'
    destination = 'C:/Users/ramesha/ZI/completed_db_files'
 
    # gather all files
    allfiles = os.listdir(source)
    print('Task Is Completed')
    # iterate on all files to move them to destination folder
    for f in allfiles:
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination, f)
        os.rename(src_path, dst_path)
        