#!/usr/bin/python
# -*- coding: utf-8 -*-
from API import API

api = API()

status, doctors = api.find_doctors(package_id='p00001')
if status :
	print(doctors)
else :
	print('error' + doctors)


#test show_profile
#status , patient = api.show_profile(username='ekekjubjub')
#print (status ," : ", patient)

#test show_detail
#status , doctor = api.show_detail(doctor_name= "จักรพงษ์" , doctor_surname='คล้ายหนองสรวง')
#status , doctor = api.show_detail('jakapong' ,'klainongsuang')
#print (status ," : ", doctor)
