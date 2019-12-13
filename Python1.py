

#Dirshe Salat


courses = {150:'CSCI 150', 161:'CSCI 161', 162:'CSCI 162', 231:'CSCI 231', 241:'CSCI 241', 251:'CSCI 251', 260:'CSCI 260', 300:'CSCI 300', 303:'CSCI 303', 304:'CSCI 304', 307:'CSCI 307', 353:'CSCI 353', 385:'CSCI 385', 355:'CSCI 355', 461:'CSCI 461', 475:'CSCI 475', 480:'CSCI 480'}

course_prereq = {150:[], 161:[], 162:[161],
      231:[162], 241:[161], 251:[], 260:[150],
      300:[241], 303:[162], 304:[162], 307:[162], 
      353:[231], 385:[353], 355:[231], 461:[303,304,307,231],
      475:[303,304,307], 480:[470]}

coursenum = 1

pastCourses = []

while (coursenum):
	coursenum = (int)(raw_input("Please enter a course number or press 0 to exit: "))
	if courses.has_key(coursenum):
    
		pastCourses.append(coursenum)
    
	elif coursenum == 0:
		pass
	else:
		print "Course does not exist. Try again"

print "You entered: "
for i in pastCourses:
	print i

print "You can take these course(s): "

for course in course_prereq.keys():
  if course in pastCourses:
    continue
  AP = True
  for prerequisite in course_prereq[course]:
    if prerequisite not in pastCourses:
      AP = False
  if AP:
    print "CSCI " + (str)(course)

