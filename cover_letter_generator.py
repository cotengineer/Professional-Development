"""
Cover letter generator program to help speed up tedious job appliaction processes
"""

import subprocess
import string

#For Current date command without time: $ date +'%B %d, %Y'
#more date format options at: https://www.lifewire.com/display-date-time-using-linux-command-line-4032698

#get the date from system
date_command = "date +'%B %d, %Y' "
output = subprocess.check_output(['bash','-c', date_command])
date = str(output)

#put a line of space between sections
new = "\n\line\line\n"

#go to next line without space between section
new0 = "\n\line\n"

#Puts single space or comma between parameters on same line/row 
s = " "
c = ", "

#Personal Input information for generation
print("Fill out the following to generate form: \n")
fname = raw_input("First Name: ")
lname = raw_input("Last Name: ")
email = raw_input("What's your email: ")
phone = raw_input("What's your phone number: ")
company = raw_input("Name of the Company/Organization receiving letter: ")
position = raw_input("The position letter is about: ")
street_num = raw_input("Home Street Number: ")
street_name = raw_input("Home Street Name: ")
city = raw_input("Home City: ")
state = raw_input("Home State: ")
zip_code = raw_input("Home Zip Code: ")
comp_city = raw_input("What is the company's City?: ")
comp_state = raw_input("What is the company's State?: ")

#Addressing receiver properly
cond = False
while (cond == False):
	x = int(input("\n\n\n-----------------------\nPress 1 if letter is to Company or\nPress 2 if letter is to Specific person: \n\n"))

	
	if (x == 1):
		to = "Sir/Madam"
		honor = ""
		intro = "Dear "+to+c
		cond = True

	if (x == 2):
		rfname = raw_input("First Name of Person Receiving Letter: ")
		rlname = raw_input("Last Name of Person Receiving Letter: ")
		to = rfname+s+rlname
		
		while (cond == False):
			specs = int(input("\n\n\n-----------------------\nPress 1 if individual is a Mr.\nPress 2 if individual is a Mrs.\nPress 3 if individual is a Doctor\nPress 4 for other: \n\n"))
		
			if (specs == 1):
				honor = "Mr."
				break
			
			if (specs == 2):
				honor = "Mrs."
				break
				
			if (specs == 3):
				honor = "Dr."
				break
				
			if (specs == 4):
				honor = raw_input("What does this individual go by?: \n\n")
				break

		intro = "Dear"+s+honor+s+rlname+c
		cond = True

talent = []
print("-----------------------")
def skillset():
	skill = raw_input("\nWhat relatable skill should be added?: \n")
	talent.append(skill)

user = 1
skillset()
while user != 0:
		
	check = int(input("\n\nPress 1 to add another skill\nPress 2 if finished adding skills\n\n"))
		
	if check == 1: 
		skillset()
	if check != 1 and len(talent) > 0:
		user = 0
	

#Talent string organizer	
print("skill(s) added successfully:")
for i in talent:
	print(i)
print("\n")	

if len(talent) == 1:
	talent_string = talent[0]
	
if len(talent) == 2:
	talent_string = talent[0]+" and "+talent[1]

if len(talent) > 2:
	talent_string = talent[0]
	talent_string_cat = ""
	for i in range(1,len(talent)-1):
		talent_string_cat = talent_string_cat+talent[i]+", "
	talent_string = talent[0]+c+talent_string_cat+"and"+s+talent[len(talent)-1]


print("\n-----------------------\nSelect choice for professional experience areas:")
choose = int(input("1) industry\n2) academia\n3) government\n4) industry and academia\n5) academia and government\n6) industry and government \n7) industry, academia, and government\n\n"))

choices = ["industrial","academic","governmental","industrial and academic","academic and governmental","industrial and governmental","industrial, academic, and governmental"] 
choice = choices[choose-1]




company_research = raw_input("\n-----------------------\nWhat field or project is the company currently focusing on that you could fit in with?: \n\n")	
accomplishments1 = raw_input("\n-----------------------\nWhat's a major accomplishment that relates to the job?: \nOne of these accomplishments was <FILL IN BLANK>.\n\n")
accomplishments2 = raw_input("\n-----------------------\nWhat's a 2nd major accomplishment that relates to the job?: \nSimilarly, I found success with <FILL IN THE BLANK> which yielded outstanding results!\n\n")
accomplishments3 = raw_input("\n-----------------------\nWhat's a 3rd major accomplishment that relates to the job?: \nAnother powerful example is shown in <FILL IN THE BLANK>.\n\n")

#main formatting of cover letter
opening = "With great interest, I am writing in response to your job posting for the "+position+" position. Upon reviewing the details for the position against my background, I strongly believe that I have the necessary skills to become a valuable asset to your organization."

body1 = "While researching your company, I noticed that it is currently focusing on "+company_research+". I would make a great addition to "+company+" for progressing in this area. I am proficient in "+talent_string+" which is more than beneficial for "+company_research+". By utilizing these skills in my career, I was able to achieve a number of profitable accomplishments. One of these accomplishments was "+accomplishments1+". Similarly, I found success with "+accomplishments2+" which yielded outstanding results! Another powerful example is shown in "+accomplishments3+". "

body2 = "My formal experience can be found in "+choice+" areas. Having this experience allowed me to thrive in diverse teams and work cultures which yielded innovated project outcomes. Given my high drive to succeed, passion for solving problems, and team leadership abilities, I am confident that filling this position would have a huge positive and lasting impact at "+company+"! "

closing = "Please accept these attached documents and feel free to contact me at your earliest convenience for further discussion. I appreciate your time and consideration for the "+position+" position!"

ending = "Sincerely"

#condenser
myaddress = new0+street_num+s+street_name+new0+city+c+state+s+zip_code
company_address = company+new0+comp_city+c+comp_state
contact = new0+email+new0+phone

header = myaddress+contact+new+date+new+company_address+new+intro
goodbye = new+ending+c+new+fname+s+lname



#Cover Letter Generator
namefile = 'cover_letter.rtf'
ofile = open(namefile,'w')
ofile.write("""{\\rtf1
{\\f0 \\fs42 \\b """+fname+s+lname+""" \\b0\line\n}"""+header+new+opening+new+body1+new0+new0+body2+new+closing+goodbye+"""}""")
ofile.close()

#finish verification
print("\n\n\n-----------------------\nCover letter file created for: "+fname+s+lname+"\n")

