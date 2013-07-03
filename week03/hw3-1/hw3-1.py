import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students


def count():
    print "Students: "
    
    try:
        recordCount = students.count()
        print recordCount
        return recordCount
        
    except:
        print "Unexpected error:", sys.exc_info()

        
def print_scores():
    print "Finding homework scores for each student"
    
    try:
        print "making cursor"
        cursor = students.find({ "scores.type": "homework" })

        for doc in cursor:
            scores = doc["scores"]
            print doc["_id"], doc["scores"]
            removed_score = remove_lowest_homework(scores)
            print doc["_id"], doc["scores"]
            
            db.students.save(doc)
            #db.grades.remove(current_student_lowest_score_doc_id)
                
    except:
        print "Unexpected error:", sys.exc_info()[0], sys.exc_traceback.tb_lineno 
        

def remove_lowest_homework(scores):
    if (len(scores) == 0):
        return;
        
    # find lowest score
    lowest_homework_score_index = -1;
    iter = enumerate(scores)
    
    for i, score in iter:
        if(score["type"] == u"homework"):
            if(lowest_homework_score_index < 0 or score["score"] < scores[lowest_homework_score_index]["score"]):
                lowest_homework_score_index = i
            
    # remove lowerst score
    if(lowest_homework_score_index >= 0):
        return scores.pop(lowest_homework_score_index)


count()
print_scores()
count()