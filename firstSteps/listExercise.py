#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

courses = {
  'mar2014': (
            {
                   'lecture_id'	: 'P1',
                   'name'   : 'Programmierung I',
                   'author' : 'N.N.',
                   'teacher': 'Loose'
                   },
			{
                   'lecture_id'	: 'P2',
                   'name'   : 'Programmierung II',
                   'teacher': 'Loose',
                   'author' : 'N.N.',
                   'prereq' : 'P1'
                   },
			{
                   'lecture_id'	: 'DB',
                   'name'   : 'Datenbanken',
                   'teacher': 'Preuss',
                   'author' : 'Li'
                   }
           	),
  'sep2014': (
              {
                      'lecture_id'	: 'OOSL',
                      'name'   : 'OO Skriptsprachen',
                      'teacher': 'Preuss'
                      },
              {
	                  'lecture_id'	: 'DB',
                      'name'   : 'Datenbanken',
                      'teacher': 'Preuss',
                      'author':  'Li'
                      }
              ),
  'mar2015': (
              {       'lecture_id'	: 'NoSQL',
				      'name'   : 'NoSQL Datenbanken',
                      'teacher': 'Edlich'
                       },
              )
}

#prüfen ob in dem Semester der Kurs angeboten wird
def is_offered(courses, course, semester) :
    for i in courses:
        dictionariesCoursesContent = courses[i]
        if i == semester :
            for j in dictionariesCoursesContent :
                if j["lecture_id"] == course :
                    return j["lecture_id"] == course
    return "nicht vorhanden"

print(is_offered(courses, 'p1', 'mar2014')) # => True
print(is_offered(courses, 'NoSQL', 'mar2015'))
print(is_offered(courses, 'NoSQL', 'sep2014'))
print(is_offered(courses, 'P1', 'mar2015'))


'''def is_offered(courses, lecture_id, semester):
    semester_offers = courses.get(semester, None)
    if not semester_offers:
        return False
    for offer in semester_offers:
        if offer.get('lecture_id', None) == lecture_id:
            return True
    return False

print(is_offered(courses, 'p1', 'mar2014')) # => True
print(is_offered(courses, 'NoSQL', 'mar2015'))
print(is_offered(courses, 'NoSQL', 'sep2014'))
'''
'''def involved(courses, person) :
    for i in courses:
        dictionariesCoursesContent = courses[i]
        print(courses[i])
            for j in dictionariesCoursesContent:
                print("Hello")
    return "nicht vorhanden"

print(involved(courses, 'Edlich'))
'''