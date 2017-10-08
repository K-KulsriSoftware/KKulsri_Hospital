#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from bson.objectid import ObjectId
class create_order_api :

    def __init__(self, db) :
        self.db = db

    def get_package_cost(self,package_id) :
        cursor = self.db.packages.aggregate([
            {
                '$match' : 
                {
                    '_id' : ObjectId(package_id)
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

    def find_bought_time(self) :
        time = datetime.now()
        year = int(time.strftime('%Y'))
        month = int(time.strftime('%m'))
        date = int(time.strftime('%d'))
        hr = int(time.strftime('%H'))
        min = int(time.strftime('%M'))
        return {'year' : year, 'month' : month, 'date' : date, 'hr' : hr, 'min' : min}

    def insert_query(self, package_id, doctor_id, patient_id, notice, time, bought_time) :
        self.db.orders.insert(
            {
                'package_id' : ObjectId(package_id),
                'doctor_id' : ObjectId(doctor_id),
                'patient_id' : ObjectId(patient_id),
                'cost' : self.get_package_cost(package_id),
                'time' : 
                {
                    'start' : datetime(time['year'], time['month'], time['date'], time['start_hr'], 0),
                    'finish' : datetime(time['year'], time['month'], time['date'], time['finish_hr'], 0)
                },
                'bought_time' : datetime(bought_time['year'], bought_time['month'], bought_time['date'], bought_time['hr'], bought_time['min']),
                'notice' : notice
            }
        )

    def create_order(self, package_id, doctor_id, patient_id, notice, time) :
        bought_time = self.find_bought_time()
        self.insert_query(package_id, doctor_id, patient_id, notice, time, bought_time)
        return True, 'Successfully Added'