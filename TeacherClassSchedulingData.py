class TeacherClassSchedulingData:

    def __init__(self):
        # let's define some data in dictionary (in future they will come from a JSON file, but for now and for clarity they are hardcoded in the class
        # Each Teacher have a name as index, a normal, a minimum and a maximum number of hours to teache a week, he/she can teach only certain grades and only certain matters
        self.teacher = {'Adam': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Italian", "Latin", "History"],
                                "gradesToTeach": ["1A", "1B"],
                                "mattersGrades": {"1A":["Italian", "Latin", "History"],
                                                  "1B":["Italian", "Latin", "History"]}
                                },
                      'Bob': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin"]}
                                },
                      'Charlie': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Mathematic", "Religion", "History"], 
                                                  "1B":["Mathematic", "Religion", "History"],
                                                  "1C":["Mathematic", "Religion", "History"],
                                                  "2A":["Mathematic", "Religion", "History"],
                                                  "2B":["Mathematic", "Religion", "History"],
                                                  "2C":["Mathematic", "Religion", "History"]}
                                },
                      'David': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Eve': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Frank': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'George': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Henry': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Ida': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'John': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["1A", "1B", "1C", "2A", "2B", "2C"],
                                "mattersGrades": {"1A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "1B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "1C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "2C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'King': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["3A", "3B", "3C"],
                                "mattersGrades": {"3A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "3B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "3C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Lady': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["3A", "3B", "3C"],
                                "mattersGrades": {"3A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "3B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "3C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Mary': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["3A", "3B", "3C"],
                                "mattersGrades": {"3A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "3B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "3C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Nora': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["3A", "3B", "3C"],
                                "mattersGrades": {"3A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "3B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "3C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                },
                      'Ocean': {
                                "normWeekHours": 18,
                                "minWeekHours": 16,
                                "maxWeekHours": 24,
                                "mattersToTeach": ["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                "gradesToTeach": ["3A", "3B", "3C"],
                                "mattersGrades": {"3A":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"], 
                                                  "3B":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"],
                                                  "3C":["Physical Education", "English", "Italian", "Latin", "Mathematic", "Religion", "History"]}
                                }
                      }
        # Three years and three section, total 9 grades. Dictionary is used for future improvement e.g. building address or reference teacher
        self.grade = {'1A': {}, '1B': {}, '1C': {}, '2A': {}, '2B': {}, '2C': {}, '3A':{}, '3B': {}, '3C': {}}
        # Seven different matters
        self.matter = {"Physical Education": {}, "English": {}, "Italian": {}, "Latin": {}, "Mathematic": {}, "Religion": {}, "History": {}}
        # Six days a week of work
        self.day = {'Monday': {}, 'Tuesday': {}, 'Wednesday': {}, 'Thursday': {}, 'Friday': {}, 'Saturday': {}}
        # Five different hours of teaching a day
        self.hour = {'08:30-09:30': {}, '09:30-10:30': {}, '10:30-11:30': {}, '11:30-12:30': {}, '12:30-13:30': {}}
        # Class rooms for future improvement
        self.room = {'Piano 1 - Stanza 1': {}, 'Piano 1 - Stanza 2': {}, 'Piano 1 - Stanza 3': {},
                'Piano 2 - Stanza 1': {}, 'Piano 2 - Stanza 2': {}, 'Piano 2 - Stanza 3': {},
                'Piano 3 - Stanza 1': {}, 'Piano 3 - Stanza 2': {}, 'Piano 3 - Stanza 3': {}} # Optional
        # Desiderata, usefull for Cost Function but not only; for each teacher we have the numers of day off and the desired day
        self.desiderata = { 'Teacher': 
                      {
                      'Adam': {
                                "offDays": 2,
                                "freeDay": ['Friday', 'Saturday']
                                },
                      'Bob': {
                                "offDays": 1,
                                "freeDay": ['Saturday']
                                },
                      'Charlie': {
                                "offDays": 1,
                                "freeDay": ['Monday']
                                },
                      'David': {
                                "offDays": 1,
                                "freeDay": ['Tuesday']
                                },
                      'Eve': {
                                "offDays": 1,
                                "freeDay": ['Wednesday']
                                },
                      'Frank': {
                                "offDays": 1,
                                "freeDay": ['Thursday']
                                },
                      'George': {
                                "offDays": 1,
                                "freeDay": ['Friday']
                                },
                      'Henry': {
                                "offDays": 1,
                                "freeDay": ['Saturday']
                                },
                      'Ida': {
                                "offDays": 1,
                                "freeDay": ['Monday']
                                },
                      'John': {
                                "offDays": 1,
                                "freeDay": ['Tuesday']
                                },
                      'King': {
                                "offDays": 1,
                                "freeDay": ['Wednesday']
                                },
                      'Lady': {
                                "offDays": 1,
                                "freeDay": ['Thursday']
                                },
                      'Mary': {
                                "offDays": 1,
                                "freeDay": ['Friday']
                                },
                      'Nora': {
                                "offDays": 1,
                                "freeDay": ['Saturday']
                                },
                      'Ocean': {
                                "offDays": 1,
                                "freeDay": ['Monday']
                                }
                      }
                     }
        # Set the number of hours to be teached for eache grade
        self.hoursForMatterForGrade = {
            ('1A', 'Physical Education'): 2,
            ('1A', 'English'): 6,
            ('1A', 'Italian'): 6,
            ('1A', 'Latin'): 4,
            ('1A', 'Mathematic'): 6,
            ('1A', 'Religion'): 2,
            ('1A', 'History'): 4,
            ('1B', 'Physical Education'): 2,
            ('1B', 'English'): 6,
            ('1B', 'Italian'): 6,
            ('1B', 'Latin'): 4,
            ('1B', 'Mathematic'): 6,
            ('1B', 'Religion'): 2,
            ('1B', 'History'): 4,    
            ('1C', 'Physical Education'): 2,
            ('1C', 'English'): 6,
            ('1C', 'Italian'): 6,
            ('1C', 'Latin'): 4,
            ('1C', 'Mathematic'): 6,
            ('1C', 'Religion'): 2,
            ('1C', 'History'): 4,
            ('2A', 'Physical Education'): 2,
            ('2A', 'English'): 6,
            ('2A', 'Italian'): 8,
            ('2A', 'Latin'): 2,
            ('2A', 'Mathematic'): 6,
            ('2A', 'Religion'): 2,
            ('2A', 'History'): 4,
            ('2B', 'Physical Education'): 2,
            ('2B', 'English'): 6,
            ('2B', 'Italian'): 8,
            ('2B', 'Latin'): 2,
            ('2B', 'Mathematic'): 6,
            ('2B', 'Religion'): 2,
            ('2B', 'History'): 4,    
            ('2C', 'Physical Education'): 2,
            ('2C', 'English'): 6,
            ('2C', 'Italian'): 8,
            ('2C', 'Latin'): 2,
            ('2C', 'Mathematic'): 6,
            ('2C', 'Religion'): 2,
            ('2C', 'History'): 4,
            ('3A', 'Physical Education'): 2,
            ('3A', 'English'): 6,
            ('3A', 'Italian'): 8,
            ('3A', 'Mathematic'): 6,
            ('3A', 'Religion'): 2,
            ('3A', 'History'): 6,
            ('3B', 'Physical Education'): 2,
            ('3B', 'English'): 6,
            ('3B', 'Italian'): 8,
            ('3B', 'Mathematic'): 6,
            ('3B', 'Religion'): 2,
            ('3B', 'History'): 6,    
            ('3C', 'Physical Education'): 2,
            ('3C', 'English'): 6,
            ('3C', 'Italian'): 8,
            ('3C', 'Mathematic'): 6,
            ('3C', 'Religion'): 2,
            ('3C', 'History'): 6
        }

        self.consecutiveHours = {
            ('1A', 'English'): {'hours':2, 'hourToStart': "10:30-11:30", 'day': 'Friday'},
            ('1A', 'Mathematic'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Monday'},
            ('1B', 'Physical Education'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Tuesday'},
            ('1B', 'Italian'): {'hours':2, 'hourToStart': "08:30-09:30", 'day': 'Thursday'},
            ('1C', 'Latin'): {'hours':2, 'hourToStart': "09:30-10:30", 'day': 'Saturday'},
            ('1C', 'Religion'): {'hours':2, 'hourToStart': "10:30-11:30", 'day': 'Friday'},
            ('2A', 'History'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Monday'},
            ('2A', 'Mathematic'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Tuesday'},
            ('2B', 'English'): {'hours':2, 'hourToStart': "08:30-09:30", 'day': 'Thursday'},
            ('2B', 'Physical Education'): {'hours':2, 'hourToStart': "09:30-10:30", 'day': 'Saturday'},
            ('2C', 'Italian'): {'hours':2, 'hourToStart': "10:30-11:30", 'day': 'Friday'},
            ('2C', 'Latin'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Monday'},
            ('3A', 'Religion'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Tuesday'},
            ('3A', 'History'): {'hours':2, 'hourToStart': "08:30-09:30", 'day': 'Thursday'},
            ('3B', 'English'): {'hours':2, 'hourToStart': "09:30-10:30", 'day': 'Saturday'},
            ('3B', 'Mathematic'): {'hours':2, 'hourToStart': "10:30-11:30", 'day': 'Friday'},
            ('3C', 'Physical Education'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Monday'},
            ('3C', 'Italian'): {'hours':2, 'hourToStart': "11:30-12:30", 'day': 'Tuesday'}
        }        
        
    def getTeacher(self):
        return self.teacher
    
    def getGrade(self):
        return self.grade
    
    def getMatter(self):
        return self.matter
    
    def getDay(self):
        return self.day
    
    def getHour(self):
        return self.hour
    
    def getDesiderata(self):
        return self.desiderata
    
    def getHoursForMatterForGrade(self):
        return self.hoursForMatterForGrade
    
    def getConsecutiveHours(self):
        return self.consecutiveHours
    
    
    