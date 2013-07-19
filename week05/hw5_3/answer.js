function topClass(sortDirection){
    return db.grades.aggregate([
        { $unwind: "$scores" }
       ,{ $match: { "scores.type": { $in: ["homework", "exam"] } } }
       ,{ $group: { _id: { studentId: "$student_id", classId: "$class_id" }, averageScorePerStudentPerClass: { "$avg":"$scores.score" } }}
       ,{ $group: { _id: "$_id.classId", averageScorePerClass: { "$avg":"$averageScorePerStudentPerClass" } } }
       ,{ $sort: { averageScorePerClass: sortDirection } }
       ,{ $limit: 1 }
    ])
}

printjson (topClass(-1));
printjson (topClass(1));