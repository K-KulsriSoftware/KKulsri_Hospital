#!/usr/bin/python
# -*- coding: utf-8 -*-

class show_departments_api :

	def __init__(self, db) :
		self.db = db

	def get_departments_query(self) :
		return self.db.packages.aggregate([
    		{
        		'$lookup' : 
        		{
            		'from' : 'departments',
            		'localField' : 'department_id',
            		'foreignField' : 'department_id',
            		'as' : 'department'
        		}
    		},
    		{
        		'$group' : 
        		{
            		'_id' : '$department',
            		'package_list' : 
            		{
                		'$push' : 
                		{
                    		'package_id' : '$package_id',
                    		'package_name' : '$package_name'
                		}
           			}
        		}
    		},
    		{
        		'$project' : 
        		{
            		'department_id' : '$_id.department_id',
            		'department_name' : '$_id.department_name',
            		'package_list' : '$package_list'
        		}
    		}
		])

	def show_departments(self) :
		cursor = self.get_departments_query()
		result = []
		for temp in cursor:
			temp.pop('_id',None)
			result.append(temp)
		return True,result