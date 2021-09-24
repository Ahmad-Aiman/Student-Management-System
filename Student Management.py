import os
import platform

#Making ListStd As Super Global Variable
global listStd 

#List Of Students
listStd = [] 

#Function For The Student Management System
def manageStudent(): 

	x = "#" * 30
	y = "=" * 28

    #Making Bye As Super Global Variable
	global bye 

    # Will Print GoodBye Message#
    # Format permits you to try and do variable substitutions and data formatting.#
	bye ="\n {}\n# {} #\n# ===> CSC305 <===  #\n# ===> GROUP PROJECT <===  #\n# {} #\n {}".format(x, y, y, x)
          


	#Printing Welcome Message And options For This Program
	print(""" 
                 
███████╗███╗░░██╗████████╗███████╗██████╗░  ░█████╗░██████╗░████████╗██╗░█████╗░███╗░░██╗  ██╗
██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║  ╚═╝
█████╗░░██╔██╗██║░░░██║░░░█████╗░░██████╔╝  ██║░░██║██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║  ░░░
██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██╔══██╗  ██║░░██║██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║  ░░░
███████╗██║░╚███║░░░██║░░░███████╗██║░░██║  ╚█████╔╝██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║  ██╗
╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═╝

Enter 1 : List Current Student 
Enter 2 : Add New Student In The List
Enter 3 : Search Current Student 
Enter 4 : Remove Selected Student
		
		""")

    #used to test code for an error which is written
	try: 
		userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
	except ValueError:
		exit("\nEnter Number Not Alphabet") #Error Message
	else:
		print("\n") #Print New Line

	#List Of Option#

    # #This Option Will Print List Of Students#
	if(userInput == 1): 
		print("List Students\n")  
		for students in listStd:
			print("=> {}".format(students))

    #This Option Will Add New Student#
	elif(userInput == 2): 
		newStd = input("Enter New Student: ")
		if(newStd in listStd): #This Condition Will Check New Student In The List Or Not
			print("\nThis Student {} Already In The Database".format(newStd))  # Print Error Message
		else:	
			listStd.append(newStd)
			print("\n=> New Student {} Successfully Add \n".format(newStd))
			for students in listStd:
				print("=> {}".format(students))	

    #This Option Will Search Student In The List#
	elif(userInput == 3):
		srcStd = input("Enter Student Name To Search: ")
		if(srcStd in listStd): #This Condition Searching The Student
			print("\n=> Record Found Of Student {}".format(srcStd))
		else:
			print("\n=> No Record Found Of Student {}".format(srcStd)) #Print Error Message

    #This Option Will Delete Student In The List
	elif(userInput == 4): 
		rmStd = input("Enter Student Name To Remove: ")
		if(rmStd in listStd): #This Condition Will Remove Student In The List
			listStd.remove(rmStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmStd))
			for students in listStd:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(rmStd)) #Print Error Message
	 
	elif(userInput < 1 or userInput > 4): #Check User Option
		print("Please Enter Valid Option")	# Print Error Message	
						
manageStudent()

#Will Restart The Program Again#
def runAgain(): 
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageStudent()
		runAgain()
	else:
		quit(bye) #Print GoodBye Message And Exit The Program

runAgain()		
