#!/usr/bin/python
# -*- coding: utf-8 -*-
class show_doctor_in_department_api :

	def __init__(self, db) :
		self.db = db

	def doctor_in_department(self) :
		return self.db.doctors.aggregate([
			{
				'$group' :
				{
					'_id' : '$department_id',
					'doctors' : 
					{
						'$push' :
						{
							'doctor_name_title' : '$doctor_name_title',
							'doctor_name' : '$doctor_name',
							'doctor_name_surname' : '$doctor_surname',
							'doctor_img' : '$doctor_img'
						}
					}
				}
			},
			{
				'$lookup' :
				{
					'from' : 'departments',
		            'localField' : '_id',
		            'foreignField' : 'department_id',
		            'as' : 'department'
				}
			},
			{
				'$project' :
				{
					'department_name' : '$department.department_name',
					'doctors' : '$doctors'
				}
			},
                        {
                                '$unwind' : '$department_name'
                        }
		])

	def show_doctor_in_department(self) :
		cursor = self.doctor_in_department()
		departments = []
		for department in cursor :
			department.pop('_id', None)
			departments.append(department)
		return True, departments