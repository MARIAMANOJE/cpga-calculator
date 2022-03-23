# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:36:31 2021

@author: Manoj
"""

def cgpa():
	TotalScore = 0	
	Grade = 0
	numberOfCourses = int(input("Please Enter the total number of Courses you Offered: "))	
	for x in range(numberOfCourses):	
		Course1 = input("Enter The subject name:")		
		unit = int(input ("How many Unit is the Course you took: "))
        
		score = int(input("Please Enter your Score:"))
		TotalScore = unit*5
		if (score >= 70):
			grade = 5
		elif(score < 70 and  score >= 60):
			grade = 4 
		elif(score < 60 and  score >= 50 ):
			grade = 3
		elif(score < 50 and  score >=45):
			grade = 2
		elif (score < 45 and  score>=40):
			grade = 1
		else :
			grade = 0 
		Grade += unit*grade
	Cgpa =float((Grade / TotalScore) * 5)
	print("THANKS FOR ALL YOUR INPUT YOUR CGPA IS : " + str(Cgpa))
cgpa()

