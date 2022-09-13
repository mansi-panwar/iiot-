from __future__ import print_function

hostname = 'localhost'
username = 'root'
password = '*********'
database = 'sensors'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    #cur.execute('CREATE DATABASE sensors;')
    cur.execute('USE sensors;')
    cur.execute( """CREATE TABLE sensors(time_stamp VARCHAR(30) PRIMARY KEY, T1 DECIMAL(6,4) NOT NULL,T2 DECIMAL(6,4) NOT NULL,T3 DECIMAL(6,4) NOT NULL,T4 DECIMAL(6,4) NOT NULL,T5 DECIMAL(6,4) NOT NULL,T6 DECIMAL(6,4) NOT NULL ,T7 DECIMAL(6,4) NOT NULL, T8 DECIMAL(6,4) NOT NULL,T9 DECIMAL(6,4) NOT NULL,T10 DECIMAL(6,4) NOT NULL, T11 DECIMAL(6,4) NOT NULL,T12 DECIMAL(6,4) NOT NULL,T13 DECIMAL(6,4) NOT NULL , T14 DECIMAL(6,4) NOT NULL,E1 DECIMAL(10,6) NOT NULL,E2 DECIMAL(10,6) NOT NULL,E3 DECIMAL(10,6) NOT NULL,E4 DECIMAL(10,6) NOT NULL,E5 DECIMAL(10,6) NOT NULL);""" )
    cur.execute('SELECT * FROM sensors')

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )

print( "Using mysql.connector:" )
import mysql.connector
myConnection = mysql.connector.connect( host=hostname,passwd=password, user=username,db=database,auth_plugin='mysql_native_password')
doQuery( myConnection )
myConnection.close()
