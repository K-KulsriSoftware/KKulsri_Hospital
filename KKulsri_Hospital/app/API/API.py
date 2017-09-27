#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import datetime
#import find_doctors

class API :

	def __init__(self) :
		self.client = MongoClient()
		self.client = MongoClient("kkulsri.cloudapp.net:27017")
		self.db = self.client.kkulsridb

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

	def display_doctor_filter(self, doctor) :
		display_doctor = {}
		display_doctor['username'] = doctor['username']
		display_doctor['doctor_name'] = doctor['doctor_name']
		display_doctor['doctor_surname'] = doctor['doctor_surname']
		display_doctor['department'] = doctor['department']
		display_doctor['doctor_img'] = doctor['doctor_img']
		return display_doctor

	# input : package_id(str), day(list of str), time('ช่วงเช้า'  or 'ช่วงบ่าย'), doctor_firstname(str), doctor_lastname(str), gender('ชาย' or 'หญิง')
	def find_doctors(self, package_id=None, days=None, time=None, doctor_firstname=None, doctor_lastname=None, gender=None) :
		if package_id == None :
			return False, 'no input package id'
		department = self.db.packages.aggregate([{'$match':{'package_id':package_id}},{'$project':{'department':1}}])
		for tmp in department :
			department = tmp['department']
			break
		if type(department) != type('') :
			return False, 'no package or department'
		doctors = self.db.doctors.find({'department':department})
		result_doctors = []
		for doctor in doctors :
			if doctor_firstname != None :
				if not doctor_firstname in doctor['doctor_name'] :
					continue
			if doctor_lastname != None :
				if not doctor_lastname in doctor['doctor_surname'] :
					continue
			if gender != None :
				if self.translate_gender(gender) != doctor['gender'] :
					continue
			if days != None and time != None :
				check = True
				for day in days :
					if day in doctor['working_time'] :
						for working_time in doctor['working_time'][day] :
							for now_check_time in range(working_time['start'], working_time['stop']) :
								if (time == 'ช่วงเช้า' and 9 <= now_check_time <= 12) or (time == 'ช่วงบ่าย' and 13 <= now_check_time <= 17) :
									check = False
									break
				if check :
					continue
			elif days != None :
				check = True
				for day in days :
					if day in doctor['working_time'] :
						check = False
						break
				if check :
					continue
			elif time != None :
				check = True
				for day in doctor['working_time'] :
					for working_time in doctor['working_time'][day] :
						for now_check_time in range(working_time['start'], working_time['stop']) :
							if (time == 'ช่วงเช้า' and 9 <= now_check_time <= 12) or (time == 'ช่วงบ่าย' and 13 <= now_check_time <= 17) :
								check = False
								break
				if check :
					continue

			result_doctors.append(self.display_doctor_filter(doctor))
		return True, result_doctors

	# input : package_id(str), user_id(str)
	def auto_find_doctors(self, package_id=None, user_id=None) :
		# use user_id in phase II
		return self.find_doctors(package_id=package_id)

	# Jakapong begin
	# input : username(str)
	def show_profile(self, username=None) :
		list_patient = []
		if username == None :
			return False, 'no input username'
		patients = self.db.patients.find({'username' : username})
		for patient in patients :
			list_patient.append(patient)
		if len(list_patient) != 0 :
			return True, (list_patient)
		else:
			return False, "No username"
	# input :doctor_name, doctor_surname
	def show_detail(self, doctor_name=None, doctor_surname=None) :
		list_detail = []
		if doctor_name == None :
			return False, 'no input doctor_name'

	#	doctors = self.db.doctors.find(	[{'$match':{'doctor_name':doctor_name}},{'$match':{"doctor_surname":doctor_surname}}])
		doctors = self.db.doctors.find({'doctor_name':doctor_name,"doctor_surname":doctor_surname})
		for doctor in doctors:
			list_detail.append(doctor)
		if len(list_detail) != 0 :
			return True, (list_detail)
		else:
			return False, "No doctor_name"

	# input : email(str), telphone_number(str), emergency_phone(str), sumit(bool)
	def edit_profile(self, email=None, telphone_number=None, emergency_phone = None, submit= False ) :
		if email == None or telphone_number == None or emergency_phone == None:
			return False, "Incommplete Input"
		if submit :
			self.db.patients.update_one(
    			{
        			'username': 'admao'
    			},
    			{
        			'$set': {
	                	'email': email,
		                'telphone_number' : telphone_number ,
		                'emergency_phone' : emergency_phone
        			}
    			}
			)
			return True,'successfully Updated'
		else :
			return False, "Incommplete"



	#Jakapong End
	#Watcharachat	TAY
	#input : -
	def show_general_list(self) :
		#cursor = self.db.packages.find({'general_inspection' : True })
		cursor = self.db.packages.aggregate([
    		{
        		'$lookup':{
        		    'from': 'departments',
        		    'localField': 'department_id',
        	   		'foreignField': 'department_id',
            		'as': 'department'
                }
    		},
    		{
        		'$match': {
            	'department.department_name': 'อายุรกรรม'
            	}
    		},
    		{
        		'$project': {
            		'package_id': '$package_id',
            		'package_name': '$package_name',
            		'package_cost': '$package_cost',
            		'description': '$description'
            	}
    		}
		])
		result = []
		for temp in cursor:
			temp.pop('_id',None)
			result.append(temp)
		return True,result

	#input : -
	def show_departments(self) :
		cursor = self.db.packages.aggregate([
    		{
        		'$lookup' : {
            		'from' : 'departments',
            		'localField': 'department_id',
            		'foreignField': 'department_id',
            		'as': 'department'
        		}
    		},
    		{
        		'$group' : {
            		'_id' : '$department',
            		'package_list' : {
                		'$push': {
                    		'package_id': '$package_id',
                    		'package_name': '$package_name'
                		}
           			}
        		}
    		},
    		{
        		'$project' : {
            		'department_id' : '$_id.department_id',
            		'department_name' : '$_id.department_name',
            		'package_list' : '$package_list'
        		}
    		}
		])
		result = []
		for temp in cursor:
			temp.pop('_id',None)
			result.append(temp)

		return True,result

	#input : package_id(string)
	def show_special_package_info(self,package_id=None) :
		if package_id == None :
			return False,'No input package ID specified'

		cursor = self.db.packages.aggregate([
			{
        		'$lookup' : {
                	'from' : 'buildings',
                	'localField' : 'building_id',
                	'foreignField' : 'building_id',
                	'as' : 'building'
            	}
    		},
    		{
        		'$match' : {
            		'package_id' : package_id
            	}
    		},
    		{
        		'$project' : {
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
		for temp in cursor:
			temp.pop('_id',None)
			return True,temp
	#input: order_id,package_id,doctor_id,patient_id,cost,time,notice UNFINISHED
	def show_confirmation_info(self,package_id=None, doctor_id=None, username=None, notice='', time=None) :
		if package_id == None or doctor_id == None or package_id == None or time == None :
			return False,'Not enough input to proceed'
		cursor = self.db.orders.aggregate([
		])
		#o000001
		return True,order_id


	def generate_orderid(self):
		cursor = self.db.orders.aggregate([
			{
            	'$count' : 'counting'
        	}
		])
		total_order = 0
		for temp in cursor:
			total_order = temp['counting']
		orderamount = total_order + 1
		if orderamount < 10 :
			return 'o0000' + str(orderamount)
		elif orderamount < 100 :
			return 'o000' + str(orderamount)
		elif orderamount < 1000 :
			return 'o00' + str(orderamount)
		elif orderamount < 10000 :
			return 'o0' + str(orderamount)
		elif orderamount < 100000 :
			return 'o' + str(orderamount)
		else :
			return 'o000000'

	def get_package_cost(self,package_id) :
		if package_id == None :
			return 'No input package ID specified'
		cursor = self.db.packages.aggregate([
    		{
        		'$match' : {
            		'package_id' : package_id
            	}
    		},
    		{
        		'$project' : {
            		'package_cost' : '$package_cost'
            	}
    		},
		])
		for temp in cursor:
			return temp['package_cost']

	#input: order_id,package_id,doctor_id,patient_id,cost,time,notice UNFINISHED
	def create_order(self,package_id=None, doctor_id=None, username=None, notice='', time=None) :
		if package_id == None or doctor_id == None or package_id == None or time == None :
			return False,'Not enough input to proceed'
		self.db.orders.insert(
			{
    			"order_id" : self.generate_orderid(),
    			"package_id" : package_id,
    			"doctor_id" : doctor_id,
    			"user_id" : username,
    			"cost" : self.get_package_cost(package_id),
    			"time" : {'start':datetime(time['year'],time['month'],time['date'],time['start_hr'],0),'finish':datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)},
    			"notice" : notice
			}
    	)
		#o00000
		return True,'successfully added'
	#Watcharachat End
