#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from find_doctors_api import find_doctors_api
from show_profile_api import show_profile_api
from show_detail_api import show_detail_api
from edit_profile_api import edit_profile_api
from register_api import register_api
from show_general_list_api import show_general_list_api
from show_departments_api import show_departments_api
from show_special_package_info_api import show_special_package_info_api
from create_order_api import create_order_api
from show_confirmation_info_api import show_confirmation_info_api
from doctor_query_api import doctor_query_api

class API :

	def __init__(self) :
		self.client = MongoClient("kkulsri.cloudapp.net:27017")
		self.db = self.client.kkulsridb
		self.find_doctors_api = find_doctors_api(self.db)
		self.show_profile_api = show_profile_api(self.db)
		self.show_detail_api = show_detail_api(self.db)
		self.edit_profile_api = edit_profile_api(self.db)
		self.register_api = register_api(self.db)
		self.show_general_list_api = show_general_list_api(self.db)
		self.show_departments_api = show_departments_api(self.db)
		self.show_special_package_info_api = show_special_package_info_api(self.db)
		self.create_order_api = create_order_api(self.db)
		self.show_confirmation_info_api = show_confirmation_info_api(self.db)
		self.doctor_query_api = doctor_query_api(self.db)

	# input : package_id(str), day(list of str), time('ช่วงเช้า'  or 'ช่วงบ่าย'), doctor_firstname(str), doctor_lastname(str), gender('ชาย' or 'หญิง')
	def find_doctors(self, package_id=None, days=None, time=None, doctor_firstname=None, doctor_lastname=None, gender=None) :
		return self.find_doctors_api.find_doctors(package_id,days,time,doctor_firstname,doctor_lastname,gender)
		
	# input : package_id(str), user_id(str)
	def auto_find_doctors(self, package_id=None, user_id=None) :
		# use user_id in phase II
		return self.find_doctors(package_id=package_id)

	# input : username(str)
	def show_profile(self, username=None) :
		return self.show_profile_api.show_profile(username)

	# input :doctor_name(str), doctor_surname(str)
	def show_detail(self, doctor_name=None, doctor_surname=None) :
		return self.show_detail_api.show_detail(doctor_name,doctor_surname)
		
	# input : email(str), telphone_number(str), emergency_phone(str), sumit(bool)
	def edit_profile(self, email=None, telphone_number=None, emergency_phone=None, submit=False) :
		return self.edit_profile_api.edit_profile(email,telphone_number,emergency_phone,submit)

	# input : username(str), patient_name_title(str), patient_name(str), patient_surname(str), patient_img(str), id_card_number(str), gender(bool), order_ids(list),
	# birthday_year(int), birthday_month(int), birthday_day(int), blood_group_abo(int), blood_group_rh(int), race(str), nationallity(str), Religion(str), Status(int), pateint_address(str), occupy(str),
	# telphone_number(str), father_name(str), mother_name(str), emergency_name(str), emergency_phone(str), mergency_addr(str), email(str), congenital_disease(list)
	def register(self, username=None, patient_name_title=None, patient_name=None, patient_surname=None, patient_img=None,
				 id_card_number=None, gender=None, order_ids=None, birthday_year=None, birthday_month=None, birthday_day=None,
				 blood_group_abo=None, blood_group_rh=None, race=None, nationallity=None, Religion=None, Status=None, 
				 pateint_address=None, occupy=None, telphone_number=None, father_name=None, mother_name=None, emergency_name=None,
				 emergency_phone=None, emergency_addr=None, email=None, congenital_disease=None, submit=False) :
		return self.register_api.register(username, patient_name_title, patient_name, patient_surname, patient_img, 
			   id_card_number, gender, order_ids, birthday_year, birthday_month, birthday_day, blood_group_abo, 
			   blood_group_rh, race, nationallity, Religion, Status, pateint_address, occupy, telphone_number, 
			   father_name, mother_name, emergency_name, emergency_phone, emergency_addr, email, congenital_disease,submit)

	#input : -
	def show_general_list(self) :
		return self.show_general_list_api.show_general_list()

	#input : -
	def show_departments(self) :
		return self.show_departments_api.show_departments()

	#input : package_id(string)
	def show_special_package_info(self, package_id=None) :
		return self.show_special_package_info_api.show_special_package_info(package_id)

	#input: package_id,doctor_id,patient_id,time
	def show_confirmation_info(self,package_id=None, doctor_id=None, username=None, time=None) :
		return self.show_confirmation_info_api.show_confirmation_info(package_id, doctor_id, username, time)

	#input: package_id,doctor_id,patient_id,time,notice
	def create_order(self,package_id=None, doctor_id=None, username=None, notice='', time=None) :
		return self.create_order_api.create_order(package_id, doctor_id, username, notice, time)

	#input: -
	def get_all_doctors(self) :
		return self.doctor_query_api.get_all_doctors()

	#input: doctor_id(str)
	def get_doctor_detail(self,doctor_id) :
		return self.doctor_query_api.get_doctor_detail(doctor_id)

	#input: -
	def get_all_doctors_name(self) :
		return self.doctor_query_api.get_all_doctors_name()