#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
class building_query_api :

	def __init__(self, db) :##
		self.db = db

	def get_all_buildings(self) :##
		cursor = self.db.buildings.aggregate([
			{
            	'$match' : {}
        	}
		])
		buildings = []
		for building in cursor :
			building.pop('_id', None)
			buildings.append(building)
		return True, buildings

	def get_building_detail(self,building_id) :##
		cursor = self.db.buildings.aggregate([
			{
            	'$match' : 
            		{
            			'building_id' : building_id
            		}
        	}
		])
		for building in cursor :
			building.pop('_id', None)
			return True, building
		return False, "No match profile"

	def get_all_buildings_name(self) :
		cursor = self.db.buildings.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'building_id' : '$building_id',
        			'building_name' : '$building_name',
        		}
        	}
		])
		buildings = []
		for building in cursor :
			building.pop('_id', None)
			buildings.append(building)
		return True, buildings

	def update_building_profile(self, building_id, building_name) :
		if building_id == None or building_name == None :
			return False, 'Incomplete input'
		self.db.buildings.update_one(
			{
        		'building_id': building_id
    		},
    		{
        		'$set': 
        		{
        			'building_name' : building_name,
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_building(self, building_id) :
		if building_id == None :
			return False, 'Incomplete input: building_id'
		self.db.building.delete_one(
			{
				"building_id": building_id
			}
		)
		return True, 'Successfully Removed'