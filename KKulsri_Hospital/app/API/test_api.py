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
