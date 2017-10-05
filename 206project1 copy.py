import operator
import os
import csv
from datetime import datetime
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

#I used a list writer and that is why I have an extra line. You said to add this note during office hours,
#saying that it is fine for those last few points! Thank you!!
#Nisa Khan nisakhan@umich.edu
#Git hub account: https://github.com/nisakhan/projectone

	import csv
	with open(file) as csvDataFile:
		csvReader = csv.reader(csvDataFile)
		next(csvReader)
		list1 = []

		for row in csvReader:
			dict1 = {}
			dict1['First'] = row[0]
			dict1['Last'] = row[1]
			dict1['Email'] = row[2]
			dict1['Class'] = row[3]
			dict1['DOB'] = row[4]
			list1.append(dict1)
		return(list1)

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	x = sorted(data, key=operator.itemgetter(col))
	firstLast = x[0]['First'] + " " + x[0]['Last']
	return(firstLast)

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	dict1 = {}
	for x in data:
		# print(x['Class'])
		if "Senior" == x["Class"]:
			dict1["Senior"] = dict1.get("Senior",0) + 1
			# print(dict1)
		if "Junior" == x["Class"]:
 			dict1["Junior"] = dict1.get("Junior",0) + 1
		if "Sophomore" == x["Class"]:
			dict1["Sophomore"] = dict1.get('Sophomore',0) + 1
		if "Freshman" == x["Class"]:
			dict1["Freshman"] = dict1.get('Freshman',0) + 1
	# print(dict1)
	# print(dict1.items())
	x = sorted(dict1.items(), key=operator.itemgetter(1), reverse = True)
	return(x)

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	days = {}
	for x in a:
		d1 = x['DOB'].split('/')[1]
		if d1 in days:
			days[d1] += 1
		else:
			days[d1] = 1
	list1 = []
	for y in days.keys():
		tuple1 = (y, days[y])
		list1.append(tuple1)
	sorted1 = sorted(list1, key=lambda k: k[1], reverse=True)
	return int(sorted1[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	s = 0
	count = 0
	for y in a:
		x = y["DOB"]
		b = datetime.strptime(x, "%m/%d/%Y")
		c = datetime.today()
		d = c-b
		s += d.days
		count += 1
	return (int((s/count)/365))

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	with open(fileName, 'w') as f:
		file1 = csv.DictWriter(f, delimiter = ',', fieldnames = ['First', 'Last', 'Email'])
		y = sorted(a, key=operator.itemgetter(col))
		for line in y:
			file1.writerow({"First":line["First"], 'Last':line["Last"], "Email":line["Email"]})


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
