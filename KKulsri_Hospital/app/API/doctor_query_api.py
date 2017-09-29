#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
class doctor_query_api :

	def __init__(self, db) :
		self.db = db

	def get_all_doctors(self) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : {}
        	}
		])
		doctors = []
		for doctor in cursor :
			doctor.pop('_id', None)
			doctors.append(doctor)
		return True, doctors

	def get_doctor_detail(self,doctor_id) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : 
            		{
            			'username' : doctor_id
            		}
        	}
		])
		for doctor in cursor :
			doctor.pop('_id', None)
			return True, doctor
		return False, "No match profile"

	def get_all_doctors_name(self) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'doctor_id' : '$username',
        			'doctor_name_title' : '$doctor_name_tile',
        			'doctor_first_name' : '$doctor_name',
        			'doctor_surname' : '$doctor_surname'
        		}
        	}
		])
		doctors = []
		for doctor in cursor :
			doctor.pop('_id', None)
			doctors.append(doctor)
		return True, doctors