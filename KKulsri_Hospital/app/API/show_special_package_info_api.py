#!/usr/bin/python
# -*- coding: utf-8 -*-

class show_special_package_info_api :

	def __init__(self, db) :
		self.db = db

	def get_packages_query(self, package_id) :
		return self.db.packages.aggregate([
			{
        		'$lookup' : 
        		{
                	'from' : 'buildings',
                	'localField' : 'building_id',
                	'foreignField' : 'building_id',
                	'as' : 'building'
            	}
    		},
    		{
        		'$match' : 
        		{
            		'package_id' : package_id
            	}
    		},
    		{
        		'$project' : 
        		{
            		'package_name' : '$package_name',
            		'package_cost' : '$package_cost',
            		'description' : '$description',
            		'conditions' : '$conditions',
            		'package_notice' : '$package_notice',
            		'building_name' : '$building.building_name'
            	}
    		},
    		{
        		'$unwind' : '$building_name'
    		},

		])

	def show_special_package_info(self, package_id) :
		packages = self.get_packages_query(package_id)
		for package in packages :
			package.pop('_id',None)
			return True, package
		return False, 'No package'
