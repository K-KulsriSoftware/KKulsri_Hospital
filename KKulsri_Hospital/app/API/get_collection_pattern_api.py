#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

class get_collection_pattern_api :

	def __init__(self, db) :
		self.db = db

	def str_type_name(self, field_type) :
		print(field_type)
		if field_type == type(0) :
			return 'int'
		if field_type == type(0.2) :
			return 'double'
		if field_type == type(datetime(1,1,1,1,0)) :
			return 'date'
		if field_type == type(True) :
			return 'bool'
		if field_type == type('') :
			return 'string'
		if field_type == type({}) :
			return 'dict'
		if field_type == type([]) :
			return 'list'

	def read_dict(self, collection_name, record_dict) :
		result = []
		for field in record_dict :
			field_type = self.str_type_name(type(record_dict[field]))
			if field_type == 'dict' :
				result.append({'field_name' : field, 'field_type' : 'dict', 'dict' : self.read_dict(record_dict[field])})
			elif field_type == 'list' :
				if collection_name == 'patients' and field == 'congenital_disease':
					result.append({'field_name' : field, 'field_type' : 'string'})
				else :
					result.append({'field_name' : field, 'field_type' : 'list', 'value' : self.str_type_name(type(record_dict[field][0]))})
			else :
				#print(field_type)
				result.append({'field_name' : field, 'field_type' : field_type})
		return result

	def get_collection_pattern(self, collection_name) :
		if collection_name == None :
			return False, 'Incomplete input: collection_name'
		all_collections_name = self.db.collection_names()
		if collection_name not in all_collections_name :
			return False, 'No collection name :' + collection_name
		cursor = self.db[collection_name].aggregate([
			{
				'$match' : {}
			},
			{
				'$limit' : 1
			}
		])
		result = []
		for record in cursor :
			record.pop('_id', None)
			result = self.read_dict(collection_name, record)
		return True, result