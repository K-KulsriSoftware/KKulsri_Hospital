#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

class create_order_api :

	def __init__(self, db) :
		self.db = db

	def get_package_cost(self,package_id) :
		cursor = self.db.packages.aggregate([
    		{
        		'$match' : 
        		{
            		'_id' : package_id
            	}
    		},
    		{
        		'$project' : 
        		{
            		'package_cost' : '$package_cost'
            	}
    		},
		])
		for temp in cursor:
			return temp['package_cost']

	def insert_query(self, package_id, doctor_id, username, notice, time, bought_time) :
		self.db.orders.insert(
			{
    			"package_id" : package_id,
    			"doctor_id" : doctor_id,
    			"patient_id" : username,
    			"cost" : self.get_package_cost(package_id),
    			"time" : 
    			{
    				'start' : datetime(time['year'], time['month'], time['date'], time['start_hr'], 0),
    				'finish' : datetime(time['year'], time['month'], time['date'], time['finish_hr'], 0)
    			},
    			"bought_time" :
    			{
    				'start' : datetime(bought_time['year'], bought_time['month'], bought_time['date'], bought_time['start_hr'], 0),
    				'finish' : datetime(bought_time['year'], bought_time['month'], bought_time['date'], bought_time['finish_hr'], 0)
    			},
    			"notice" : notice
			}
    	)

	def create_order(self, package_id, doctor_id, patient_id, notice, time, bought_time) :
		self.insert_query(package_id, doctor_id, patient_id, notice, time, bought_time)
		return True,'Successfully Added'