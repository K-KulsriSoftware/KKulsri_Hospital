#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

class create_order_api :

	def __init__(self, db) :
		self.db = db

	def get_new_order_id(self):
		cursor = self.db.orders.aggregate([
			{
				'$match' : {}
			},
			{
				'$sort' : 
				{
					'order_id' : -1
				}
			},
			{
				'$limit' : 1
			}
		])
		for temp in cursor:
			temp = int(temp['order_id'][1:]) + 1
			if temp < 10 :
				return 'o0000' + str(temp)
			elif temp < 100 :
				return 'o000' + str(temp)
			elif temp < 1000 :
				return 'o00' + str(temp)
			elif temp < 10000 :
				return 'o0' + str(temp)
			elif temp < 100000 :
				return 'o' + str(temp)
			else :
				return 'o000000'

	def get_package_cost(self,package_id) :
		if package_id == None :
			return 'No input package ID specified'
		cursor = self.db.packages.aggregate([
    		{
        		'$match' : 
        		{
            		'package_id' : package_id
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

	def insert_query(self, package_id, doctor_id, username, notice, time) :
		self.db.orders.insert(
			{
    			"order_id" : self.generate_new_order_id(),
    			"package_id" : package_id,
    			"doctor_id" : doctor_id,
    			"user_id" : username,
    			"cost" : self.get_package_cost(package_id),
    			"time" : 
    			{
    				'start':datetime(time['year'],time['month'],time['date'],time['start_hr'],0),
    				'finish':datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)
    			},
    			"notice" : notice
			}
    	)

	def create_order(self,package_id, doctor_id, username, notice, time) :
		if package_id == None or doctor_id == None or username == None or package_id == None or time == None :
			return False,'Incomplete input: package_id, doctor_id, username, package_id, time'
		self.insert_query(package_id, doctor_id, username, notice, time)
		return True,'Successfully Added'