#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime
class orders_query_api :

	def __init__(self, db) :
		self.db = db

	def get_all_orders(self) :
		cursor = self.db.orders.aggregate([
			{
            	'$match' : {}
        	}
		])
		orders = []
		for order in cursor :
			order.pop('_id', None)
			orders.append(order)
		return True, orders




	def get_order_detail(self,order_id) :
		cursor = self.db.orders.aggregate([
			{
            	'$match' :
            		{
            			'order_id' : order_id
            		}
        	}
		])
		for order in cursor :
			order.pop('_id', None)
			return True, order
		return False, "No match order"


	def get_all_orders_with_package_and_user(self) :
		cursor = self.db.orders.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'order_id' : '$order_id',
        			'package_id' : '$package_id',
                    'user_id' : '$user_id'
        		}
        	}
		])
		orders = []
		for order in cursor :
			order.pop('_id', None)
			orders.append(order)
		return True, orders


	def update_order(self, order_id, package_id, doctor_id, username, notice, cost, time) :
		if order_id == None or package_id == None or doctor_id ==None or username == None or notice == None or cost == None or time == None:
			return False, 'Incommplete Input'

		self.db.orders.update_one(
    		{
        		'order_id': order_id
    		},
    		{
        		'$set':
        		{
            			'package_id' : package_id,
            			'doctor_id' : doctor_id,
            			'user_id' : username,
            			'cost' : cost ,
            			'time' :
            			{
            				'start':datetime(time['year'],time['month'],time['date'],time['start_hr'],0),
            				'finish':datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)
            			},
            			'notice' : notice

        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_order(self, order_id) :
		if order_id == None :
			return False, 'Incomplete input: order_id'
		self.db.orders.delete_one(
            {
                "order_id": order_id
            }
        )
		return True, 'Successfully Removed'


	def create_order(self, order_id, package_id, doctor_id, username, notice, cost, time) :
		if order_id == None or package_id == None or doctor_id ==None or username == None or notice == None or cost == None or time == None:
			return False, 'Incommplete Input'

		self.db.orders.insert(
			{
                'order_id' : order_id,
                'package_id' : package_id,
                'doctor_id' : doctor_id,
                'user_id' : username,
                'cost' : cost ,
                'time' :
                {
                    'start':datetime(time['year'],time['month'],time['date'],time['start_hr'],0),
                    'finish':datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)
                },
                'notice' : notice
			}
	    )
		return True,'Successfully Added'
