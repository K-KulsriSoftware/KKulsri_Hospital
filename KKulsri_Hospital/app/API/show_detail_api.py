#!/usr/bin/python
# -*- coding: utf-8 -*-

class show_detail_api :

	def __init__(self, db) :
		self.db = db

	def get_doctor_query(self, doctor_name, doctor_surname) :
		return self.db.doctors.aggregate([
    		{
        		'$match' :
        		{
            		'doctor_name' : doctor_name,
					'doctor_surname' : doctor_surname
        		}
    		},
    		{
        		'$project':
        		{
					'username': '$username',
					'doctor_name_title' : '$doctor_name_title',
            		'doctor_name' : '$doctor_name',
            		'doctor_surname' : '$doctor_surname',
            		'doctor_img' : '$doctor_img',
					'doctor_img' : '$doctor_img',
					'position' : '$position',
					'expertises' : '$expertises',
					'educations' : '$educations',
					'language' : '$language',
					'working_time' : '$working_time',
        		}
     		}
		])
	
	def show_detail(self, doctor_name, doctor_surname) :
		if doctor_name == None or doctor_surname == None :
			return False, 'Incomplete input: doctor_name, doctor_surname'

		doctors = self.get_doctor_query(doctor_name,doctor_surname)
		for doctor in doctors :
			doctor.pop('_id',None)
			return True, doctor
		return False, 'No Profile'