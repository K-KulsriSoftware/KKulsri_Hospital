#!/usr/bin/python
# -*- coding: utf-8 -*-

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
