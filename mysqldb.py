#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from six import itervalues
import mysql.connector
from datetime import date, datetime, timedelta

class winsky:

        username = 'root'
        password = '721142'
        database = 'winsky_db'
        host = 'localhost'
        connection = ''
        connect = True
	placeholder = '%s'

        def __init__(self):
                if self.connect:
                        winsky.connect(self)
	def escape(self,string):
		return '`%s`' % string
        def connect(self):
        	config = {
        		'user':winsky.username,
        		'password':winsky.password,
        		'host':winsky.host
        	}
        	if winsky.database != None:
        		config['database'] = winsky.database

        	try:
        		cnx = mysql.connector.connect(**config)
        		winsky.connection = cnx
        		return True
        	except mysql.connector.Error as err:

			if (err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
				print "The credentials you provided are not correct."
			elif (err.errno == errorcode.ER_BAD_DB_ERROR):
				print "The database you provided does not exist."
			else:
				print "Something went wrong: " , err
			return False


	def replace(self,tablename=None,**values):
		if winsky.connection == '':
                	print "Please connect first"
                	return False

                tablename = self.escape(tablename)
				
                if values:
                        _keys = ", ".join(self.escape(k) for k in values)
                        _values = ", ".join([self.placeholder, ] * len(values))
                        sql_query = "REPLACE INTO %s (%s) VALUES (%s)" % (tablename, _keys, _values)
                else:
                        sql_query = "REPLACE INTO %s DEFAULT VALUES" % tablename

				
		cur = winsky.connection.cursor()
            	try:
                	if values:
                    		cur.execute(sql_query, list(itervalues(values)))
                	else:
                    		cur.execute(sql_query)
                	winsky.connection.commit()
                	return True
            	except mysql.connector.Error as err:
                	print ("An error occured: {}".format(err))
                	return False