#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import eel
import os
from datetime import date
import wx

eel.init('web')

input_path = ''
flag = 0


@eel.expose
def saveData(name, date1):
    conn = sqlite3.connect('birthday_new.db')
    print('Opened database successfully')
    conn.execute('''CREATE TABLE IF NOT EXISTS Pictures
	         (
	         ID  INTEGER PRIMARY KEY AUTOINCREMENT,
	         NAME TEXT NOT NULL,
	         DATE1 DATE,
	         PHOTO BLOB		
	      );''')
    print('Table created successfully')
    conn.close()

    insertBLOB(name, date1)


@eel.expose
def convertToBinaryData(filename):

    # Convert digital data to binary format

    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


@eel.expose
def insertBLOB(name, date1):
    try:
        global flag
        global input_path
        flag = 0
        sqliteConnection = sqlite3.connect('birthday_new.db')
        cursor = sqliteConnection.cursor()

        print('Connected to SQLite')
        sqlite_insert_blob_query = \
            """ INSERT INTO Pictures
		                          (name,date1,photo) VALUES (?, ?, ?)"""

        empPhoto = convertToBinaryData(input_path)
        data_tuple = (name, date1, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        flag=1
        print('Image and file inserted successfully as a BLOB into a table')
        cursor.close()
    except sqlite3.Error as error:
        print ('Failed to insert blob data into sqlite table', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('the sqlite connection is closed')

    print(flag)
    return flag

@eel.expose
def flagValue():
    return flag

@eel.expose
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


@eel.expose
def readBlobData():
    print("readBlobData()")
    try:
        Name = []
        person_id = []
        today = date.today()
        today_date = today.strftime("%Y-%m-%d")
        sqliteConnection = sqlite3.connect('birthday_new.db')
        cursor = sqliteConnection.cursor()
        print(" readblobdata Connected to SQLite")
        sql_fetch_blob_query = """SELECT ID,NAME,DATE1,PHOTO FROM Pictures WHERE DATE1=?"""
        cursor.execute(sql_fetch_blob_query, (today_date,))
        record = cursor.fetchall()
        print(record)
        for row in record:
            print("Id = ", row[0], "Name = ", row[1], "Date = ", row[2])
            name = row[1]
            date1 = row[2]
            photo = row[3]
            Name.append(row[1])

            print("Storing employee image and resume on disk \n")
            id = str(row[0])
            photoPath = os.path.abspath(os.getcwd()) + "\web\pics\\" + id + ".jpg"
            print("path is=====> ", photoPath)
            writeTofile(photo, photoPath)
            person_id.append(row[0])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
        print("sqlite connection is closed")

        print(Name)
        print(person_id)
    if(len(Name)!=0 and len(person_id)!=0):
        print("Yes")
        return Name,person_id
    else:
        print("No")
        return ""




@eel.expose
def pythonFunction(wildcard='*'):
    global input_path
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    input_path = path
    print(input_path)
    return path



eel.start('index.html')




			
