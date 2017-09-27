#!/usr/bin/python
# -*- coding: utf-8 -*-
from API import API
from pprint import pprint

api = API()

#test find_doctors
#status, result = api.find_doctors(package_id='p00001')
#status, result = api.find_doctors(package_id='p00001',days=['mon'])
#status, result = api.find_doctors(package_id='p00001',days=['mon','tue'],time='ช่วงเช้า')
#status, result = api.find_doctors(package_id='p00001',days=['wed','sat'],time='ช่วงบ่าย',gender='ชาย')
#status, result = api.find_doctors(days=['wed','sat'],time='ช่วงบ่าย',gender='ชาย')
#status, result = api.find_doctors(package_id='p00001',days=['wed','sat'],time='ช่วงบ่าย',gender='ชาย')

#test auto_find_doctors
#status, result = api.auto_find_doctors(package_id='p00001')

#test show_profile
#status, result = api.show_profile(username='ekekjubjub')

#test show_detail
#status, result = api.show_detail(doctor_name="จักรพงษ์", doctor_surname='คล้ายหนองสรวง')
#status, result = api.show_detail(doctor_name="Jackapong", doctor_surname='K.')

#test edit_profile
#status, result = api.edit_profile(email="eiei@gmail.com", telphone_number="0923485995", emergency_phone="0653251554", submit=True)

#test register
'''
status, result = api.register("watermelon", "นางสาว", "สมหญิง", "ชำนาญคอม", "img.html", "1309905889674", True, [], 1996, 
							  1, 1, 1, 2, "ไทย", "ไทย", "พุทธ", 1, "37/16 สุขุมวิทย์ กทม", "โปรแกรมเมอร์", "0818453265", 
							  "วิศรุต ชำนาญคอม", "วริศรา หล่อเภรี", "มหาอินทร์ การช่างเยี่ยม", "0845263254", "98/14 ทองหล่อ กทม", 
							  "st@gmail.com", [], True)
'''

#test show_general_list
#status,result = api.show_general_list()

#test show_departments
#status,result = api.show_departments()

#test show_special_package_info
#status,result = api.show_special_package_info('p00002')

#test create_order
'''
status,result = api.create_order('p00003','d002', 'admao', 'test notice',
				{
    	    		"year" : 2018,
					"date" : 13,
					"month" : 11,
					"start_hr" : 9,
					"finish_hr" : 10,
    			})
'''

#test show_confirmation_info
'''
status,result = api.show_confirmation_info('p00003','d002', 'admao',
				{
    	    		"year" : 2017,
					"date" : 12,
					"month" : 11,
					"start_hr" : 9,
					"finish_hr" : 10,
    			})
'''

if status :
	pprint(result)
else :
	print('ERROR: ' + result)