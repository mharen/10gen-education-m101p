start mongod.exe --replSet m101 --logpath "\data\rs1.log" --dbpath \data\rs1 --port 27017 --smallfiles --oplogSize 10
start mongod.exe --replSet m101 --logpath "\data\rs2.log" --dbpath \data\rs2 --port 27018 --smallfiles --oplogSize 10
start mongod.exe --replSet m101 --logpath "\data\rs3.log" --dbpath \data\rs3 --port 27019 --smallfiles --oplogSize 10
