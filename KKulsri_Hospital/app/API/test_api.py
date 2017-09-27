#!/usr/bin/python
# -*- coding: utf-8 -*-
from API import API
from pprint import pprint

api = API()

#test find_doctors
#status, result = api.find_doctors(package_id='p00001')
#test auto_find_doctors
#status, result = api.auto_find_doctors(package_id='p00001')
#if status :
#	pprint(result)
#else :
#	print('error' + result)

#test show_profile
#status , result = api.show_profile(username='ekekjubjub')
#print (status ," : ", result)

#test show_detail
#status , result = api.show_detail(doctor_name= "จักรพงษ์" , doctor_surname='คล้ายหนองสรวง')
#status , result = api.show_detail('jakapong' ,'klainongsuang')
#print (status ," : ", result)


#test show_special_package_info
status,result = api.show_special_package_info('p00002')

if status : 
	pprint (result)
