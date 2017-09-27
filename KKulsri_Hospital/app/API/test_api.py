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
'''
#test edit_profile
status , result = api.edit_profile(email="eiei@gmail.com", telphone_number="0923485995", emergency_phone = "0653251554", submit=True)
if status :
	pprint(result)
else :
	print('error' + result)
'''
'''
#test show_general_list
status,result = api.show_general_list()

if status :
	pprint (result)

#test show_departments
status,result = api.show_departments()

if status :
	pprint (result)

#test show_special_package_info
status,result = api.show_special_package_info('p00002')

if status :
	pprint (result)

#test create_order
status,result = api.create_order('p00003','d002', 'admao', 'test notice',
				{
    	    		"year" : 2017,
					"date" : 12,
					"month" : 11,
					"start_hr" : 9,
					"finish_hr" : 10,
    			})

if status :
	pprint (result)
'''
#test show_confirmation_info
status,result = api.show_confirmation_info('p00003','d002', 'admao',
				{
    	    		"year" : 2017,
					"date" : 12,
					"month" : 11,
					"start_hr" : 9,
					"finish_hr" : 10,
    			})
if status :
	pprint (result)
