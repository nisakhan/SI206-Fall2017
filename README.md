# Project2
Starter Code and descriptions for Project2

#Nisa Khan

#find_urls
#This finds urls in strings of lists and extracts just the urls
#My code here uses regular expression, looking for http:// at the beginning of the url.
#the . that allows you to find the ending such as .com or .co

#grab_headlines
#This grabs the most popular headlines in the Michigan Daily
#We are using Beautiful Soup in order to link to the internet
#Then, we iterate through "pane-mostread" as seen on line 43, this is the Most Read section of the page
#li is one of the division on the page
#We then append these popular headlines into a list.

#get_umsi_data
#This goes through UMSI's directory and turns them into a dictionary of Names: Profession
#We need to use the html parser on Beautiful Soup in order to go through this page
#At line 68, we are going through all 12 pages of the UMSI Pagel
#We then use soup to go through the rows, and then go in deeper of the divs to find the Names
#Then you do it again with the position-- here you need to go in deeper into the divs to find the position's text. You do this through for loops.
#Add to the dictionary and return it.

#num_students
#Starting line 93, we initialize phd_students to 0
#We iterate using a for loop through the values of the dictionary of data
#Every time there is the string of PhD student in the variable, we add to the count of phd_students
