#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

class register_api :

	def __init__(self, db) :
		self.db = db
	
	def insert_query(self, username, patient_name_title, patient_name, patient_surname, patient_img, id_card_number, gender, 
				 order_ids, birthday_year, birthday_month, birthday_day, blood_group_abo, blood_group_rh, race, nationallity, 
				 Religion, Status, pateint_address, occupy, telphone_number, father_name, mother_name, emergency_name,
				 emergency_phone, emergency_addr, email, congenital_disease) :
		self.db.patients.insert(
			{
    			'username' : username,
    			'patient_name_title' : patient_name_title,
    			'patient_name' : patient_name,
    			'patient_surname' : patient_surname,
    			'patient_img' : patient_img,
    			'id_card_number' : id_card_number,
    			'gender' : gender,
				'order_ids' : order_ids,
				'birthday' : datetime(birthday_year, birthday_month, birthday_day),
				'blood_group_abo' : blood_group_abo,
				'blood_group_rh' : blood_group_rh,
				'race' : race,
				'nationallity' : nationallity,
				'Religion' : Religion,
				'Status' : Status,
				'pateint_address' : pateint_address,
				'occupy' : occupy,
				'telphone_number' : telphone_number,
				'father_name' : father_name,
				'mother_name' : mother_name,
				'emergency_name' : emergency_name,
				'emergency_phone' : emergency_phone,
				'emergency_addr' : emergency_addr,
				'email' : email,
				'congenital disease' : congenital_disease
			}
	    )


	def register(self, username, patient_name_title, patient_name, patient_surname, patient_img, id_card_number, gender, 
				 order_ids, birthday_year, birthday_month, birthday_day, blood_group_abo, blood_group_rh, race, nationallity, 
				 Religion, Status, pateint_address, occupy, telphone_number, father_name, mother_name, emergency_name,
				 emergency_phone, emergency_addr, email, congenital_disease, submit) :
		if username == None or patient_name_title == None or patient_name == None or patient_surname == None :
			return False, 'Incommplete Input: username, patient_name_title, patient_name, patient_surname'
		if patient_img == None or id_card_number == None or gender == None or order_ids == None or birthday_year == None :
			return False, 'Incommplete Input: patient_img, id_card_number, gender, order_ids, birthday_year'
		if birthday_month == None or birthday_day == None or blood_group_abo == None or blood_group_rh == None or race == None :
			return False, 'Incommplete Input: birthday_month, birthday_day, blood_group_abo, blood_group_rh, race'
		if nationallity == None or Religion == None or Status == None or pateint_address == None or occupy == None :
			return False, 'Incommplete Input: nationallity, Religion, Status, pateint_address, occupy'
		if telphone_number == None or father_name == None or mother_name == None or emergency_name == None :
			return False, 'Incommplete Input: telphone_number, father_name, mother_name, emergency_name'
		if emergency_phone == None or emergency_addr == None or email == None or congenital_disease == None :
			return False, 'Incommplete Input: emergency_phone, emergency_addr, email, congenital_disease'
		if submit :
			self.insert_query(username, patient_name_title, patient_name, patient_surname, patient_img, id_card_number, gender, 
				 order_ids, birthday_year, birthday_month, birthday_day, blood_group_abo, blood_group_rh, race, nationallity, 
				 Religion, Status, pateint_address, occupy, telphone_number, father_name, mother_name, emergency_name,
				 emergency_phone, emergency_addr, email, congenital_disease)
			return True,'Successfully Added'
		else :
			return False, 'Fail Added'