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

	def update_doctor_profile(self, doctor_id, doctor_name_title, doctor_name, doctor_surname, gender, birthday, 
		                      office_phone_number, email, department_id, doctor_img, position, expertises, 
		                      educations, language, working_time) :
		if doctor_id == None or doctor_name_title == None or doctor_name == None or doctor_surname == None or
		   gender == None or birthday == None or office_phone_number == None or email == None or 
		   department_id == None or doctor_img == None or position == None or expertises == None or
		   educations == None or language == None or working_time == None :
			return False, 'Incomplete input'
		self.db.doctors.update_one(
			{
        		'username': doctor_id
    		},
    		{
        		'$set': 
        		{
        			'doctor_name_title' : doctor_name_title,
        			'doctor_name' : doctor_name,
        			'doctor_surname' : doctor_surname,
        			'gender' : gender,
        			'birthday' : birthday,
        			'office_phone_number' : office_phone_number,
	               	'email': email,
	               	'department_id' : department_id,
	               	'doctor_img' : doctor_img,
	               	'position' : position,
	               	'expertises' : expertises,
	               	'educations' : educations,
	               	'language' : language,
	               	'working_time' : working_time
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_doctor(self, doctor_id) :
		if doctor_id == None :
			return False, 'Incomplete input: doctor_id'
		self.db.doctor.delete_one(
			{
				"username": doctor_id
			}
		)
		return True, 'Successfully Removed'