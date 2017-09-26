from pymongo import MongoClient
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

	# input : username(str)
	def show_profile(self, username=None) :
		list_patient = []
		if username == None :
			return False, 'no input username'
		patients = self.db.patients.find({'username':username})
		for patient in patients:
			list_patient.append(patient)
		if (len(list_patient) != 0):
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
		if (len(list_detail) != 0):
			return True, (list_detail)
		else:
			return False, "No doctor_name"
