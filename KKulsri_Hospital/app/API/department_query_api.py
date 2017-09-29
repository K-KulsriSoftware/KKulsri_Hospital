#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
class department_query_api :

	def __init__(self, db) :##
		self.db = db

	def get_all_departments(self) :##
		cursor = self.db.departments.aggregate([
			{
            	'$match' : {}
        	}
		])
		departments = []
		for department in cursor :
			department.pop('_id', None)
			departments.append(department)
		return True, departments

	def get_department_detail(self,department_id) :##
		cursor = self.db.departments.aggregate([
			{
            	'$match' : 
            		{
            			'department_id' : department_id
            		}
        	}
		])
		for department in cursor :
			department.pop('_id', None)
			return True, department
		return False, "No match profile"

	def get_all_departments_name(self) :
		cursor = self.db.departments.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'department_id' : '$department_id',
        			'department_name' : '$department_name',
        		}
        	}
		])
		departments = []
		for department in cursor :
			department.pop('_id', None)
			departments.append(department)
		return True, departments

	def update_department_profile(self, department_id, department_name) :
		if department_id == None or department_name == None :
			return False, 'Incomplete input'
		self.db.departments.update_one(
			{
        		'department_id': department_id
    		},
    		{
        		'$set': 
        		{
        			'department_name' : department_name_title,
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_department(self, department_id) :
		if department_id == None :
			return False, 'Incomplete input: department_id'
		self.db.department.delete_one(
			{
				"department_id": department_id
			}
		)
		return True, 'Successfully Removed'