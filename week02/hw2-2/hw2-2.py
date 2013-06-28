
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.students
grades = db.grades


def count():
    print "Grades: "
    
    try:
        recordCount = grades.count()
        print recordCount
        return recordCount
        
    except:
        print "Unexpected error:", sys.exc_info()

        
def drop_lowest_grade():
    print "Finding lowest grade for each student"
    
    try:
        print "making cursor"
        cursor = grades.find({ "type": "homework" }).sort([("student_id",pymongo.ASCENDING), ("score",pymongo.ASCENDING)])
        print "assigning previous_student_id=none"
        previous_student_id = None
        print "iterating through cursor"

        haveRecordsAlreadyBeenRemoved = count() != 800
        
        if (haveRecordsAlreadyBeenRemoved):
            print "It looks like records have already been removed so we won't do that again (we'll just print)"

        for doc in cursor:
            current_student_id = doc["student_id"]
            
            if(previous_student_id == None or previous_student_id != current_student_id):
                current_student_lowest_score = doc["score"]
                current_student_lowest_score_doc_id = doc["_id"]
                print current_student_lowest_score_doc_id, current_student_id, current_student_lowest_score
                if (not haveRecordsAlreadyBeenRemoved):
                    print "score removed"
                    db.grades.remove(current_student_lowest_score_doc_id)
                
            previous_student_id = current_student_id
    
    except:
        print "Unexpected error:", sys.exc_info()[0]
        


count()
drop_lowest_grade()
count()