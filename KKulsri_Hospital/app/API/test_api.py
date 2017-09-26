from API import API

api = API()
status, doctors = api.find_doctors(package_id='p00001')
if status :
	print(doctors)
else :
	print('error' + doctors)