#!/usr/bin/python
# -*- coding: utf-8 -*-

class find_doctors_api :

	def __init__(self, db) :
		self.db = db

	def translate_gender(self, gender) :
		if type(gender) == type(True) :
			if gender :
				return 'ชาย'
			else :
				return 'หญิง'
		else :
			if gender == 'ชาย' :
				return True
			else :
				return False

	def get_doctors_query(self, package_id) :
		return self.db.packages.aggregate([
		    {
		        '$match' :
		        {
		            'package_id' : package_id
		        }
		    },
		    {
		        '$lookup' :
		        {
		            'from' : 'doctors',
		            'localField' : 'department_id',
		            'foreignField' : 'department_id',
		            'as' : 'doctor'
		        }
		    },
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
		        '$unwind' : '$department'
		    },
		    {
		        '$unwind' : '$doctor'
		    },
		    {
		        '$project' :
		        {
		            'username' : '$doctor.username',
		            'doctor_name_title' : '$doctor.doctor_name_title',
		            'doctor_name' : '$doctor.doctor_name',
		            'doctor_surname' : '$doctor.doctor_surname',
		            'department_name' : '$department.department_name',
		            'doctor_img' : '$doctor.doctor_img',
		            'working_time' : '$doctor.working_time',
		            'gender' : '$doctor.gender'
		        }
		    }
		])

	def check_correct_conditions(self, doctor, days, time, doctor_firstname, doctor_lastname, gender) :
		if doctor_firstname != None :
			if not doctor_firstname in doctor['doctor_name'] :
				return False
		if doctor_lastname != None :
			if not doctor_lastname in doctor['doctor_surname'] :
				return False
		if gender != None :
			if common_function.translate_gender(gender) != doctor['gender'] :
				return False
		if days != None and time != None :
			check = True
			for day in days :
				for working_time in doctor['working_time'][day] :
					for now_check_time in range(working_time['start'], working_time['stop']) :
						if (time == 'ช่วงเช้า' and 9 <= now_check_time <= 12) or (time == 'ช่วงบ่าย' and 13 <= now_check_time <= 17) :
							check = False
			if check :
				return False
		elif days != None :
			check = True
			for day in days :
				if len(doctor['working_time'][day]) > 0 :
					check = False
			if check :
				return False
		elif time != None :
			check = True
			for day in doctor['working_time'] :
				for working_time in doctor['working_time'][day] :
					for now_check_time in range(working_time['start'], working_time['stop']) :
						if (time == 'ช่วงเช้า' and 9 <= now_check_time <= 12) or (time == 'ช่วงบ่าย' and 13 <= now_check_time <= 17) :
							check = False
			if check :
				return False
		return True

	def find_doctors(self, package_id, days, time, doctor_firstname, doctor_lastname, gender) :
		if package_id == None :
			return False, 'Incomplete input: package_id'
		doctors = self.get_doctors_query(package_id)
		result_doctors = []
		for doctor in doctors :
			if self.check_correct_conditions(doctor, days, time, doctor_firstname, doctor_lastname, gender) :
				doctor.pop('_id', None)
				doctor.pop('working_time', None)
				doctor.pop('gender', None)
				result_doctors.append(doctor)
		return True, result_doctors