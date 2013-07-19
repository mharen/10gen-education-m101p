function averageCityPopulation(states, minimumPopulation){
    return db.zips.aggregate([
        { $match: { state: { $in: states } } }
       ,{ $group: { _id: { city: "$city", state: "$state" }, totalCityPopulation: { "$sum":"$pop" } }}
       ,{ $match: { totalCityPopulation: { $gt: minimumPopulation } } }
       ,{ $group: { _id: "1", averagePopulation: { "$avg":"$totalCityPopulation" } }}
    ])
}

printjson (averageCityPopulation(['CT', 'NJ'], 25000));
printjson (averageCityPopulation(['CA', 'NY'], 25000));