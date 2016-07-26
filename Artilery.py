#Artilery Computer for Arma 3

import math #imports math functions for sqrt and sin cosine usage

def angleinputA(): #prompts user to put compass bearing when pointing compass at target
	A = float(input('\nEnter the angle that the compass shows when pointing at the TARGET '))
	return A

def angleinputB():#prompts user to put compass bearing when pointing compass at artilerty position
	B = float(input('Enter the angle that the compass shows when pointing at the ARTILERY POSITION '))
	return B

def anglecalc(A, B): #Finds angle between spotter and artilery gun
	if B > 180 and A > 180: #suggets a formula for different situations of a 0-360 degree compass
		if B > A:
			C = B-A
		else:
			C = A-B
	elif B > 180:
		C = 360-B+A
	elif A > 180:
		C = 360-A+B
	elif B > A:
		C = B-A
	elif A > B:
		C = A-B
	elif A == B:
		C = A-B
	return C

def distanceST(): # Distance between Spotter and target
	ST = float(input('Enter the distance between you and the TARGET ')) #Prompts user
	return ST
def distanceSA(): #Distance between spotter and artilery
	SA = float(input ('Enter the distance between the spotter and the ARTILERY '))
	return SA
	
def lawofcos(C, ST, SA): #Uses law of cosine to find distance between artilery and target
	CR = math.radians(C) #converts degree given C into radians 
	AT = math.sqrt(ST**2+SA**2-(2*ST*SA*math.cos(CR))) #uses law of cosine
	return AT
	
def lawofcosA(ST, SA, AT): #uses law of inverse cosine to find the angle between the target, the artilery, and the spotter
	BR = math.acos((ST**2-SA**2-AT**2)/(-2*AT*SA))
	Bart = math.degrees(BR) #converts the radian result into degrees assigns it to variable Bart meaning angle from artiliry point of view
	return Bart
	
def anglecalcArt(A, B, Bart): #Finds the compass bearing for the artilery position to face the target
	if B >= 180: #finds the opposite bearing from the artilry point of view by taking the spotters bearing direction and putting 180 degrees on it on either direction
		B2= B-180
		print(B2)
	else: 
		B2= B+180
		print(B2)
	if B > B2:
		Bearing=B2+Bart #adds or subtracts the values of B2 from Bart to find the actual compass bearing
	else:
		Bearing=B2-Bart
	return Bearing

	

def calculations(): #uses all the inputs to calculate relevent data
	A = angleinputA()
	B = angleinputB()
	C = anglecalc(A, B)
	ST = distanceST()
	SA = distanceSA()
	AT = lawofcos(C, ST, SA)
	Bart = lawofcosA (ST, SA, AT)
	Bearing = anglecalcArt(A, B, Bart) 
	print('\nThe ANGLE between the artilery and the spotter and target is',"%.2f" %  Bart, 'degrees') #may need this later for troubleshooting bugs
	print('The DISTANCE between the artilery and the target is',"%.2f" %  AT)
	print('The BEARING of the artilery to the target is',"%.2f" %  Bearing)
	

def repeat(): #function to ask the user if he would like to make another recalculation
	out = input('\nWould you like to recalculate again y/n? ')
	return out

	
def main(): #main function
	try:
		calculations()
	except:
		print('\nYou fucked up somewhere\n')
		out = repeat()
		if out == 'y':
			try:
				main()
			except:
				exit()
		else:
			exit()

	try:
		out = repeat()
		if out == 'y':
			main()
		else:
			exit()
	except:
		exit()


main()
