# create a dictionary list of 3 students 
student1={
    "name":"John",
    "age": 25,
    "subjects": ["maths", "physics", "chemistry"]
}
student2={
    "name":"Alice",
    "age": 22,
    "subjects": ["english", "history", "geography"]
}
student3={
    "name":"Bob",
    "age": 24,
    "subjects": ["computer science", "art", "music"]
}
#print(student1)
#print(student2)
#print(student3)

# modify student2 subjects 
#["subjects"]=["kiswahili", "CRE", "homescience"]
#print(student2)

student2.update({"subjects": ["kiswahili", "CRE", "homescience"]})
#print(student2)

# remove a subject from student1
#student1["subjects"]=["maths", "physics"]
#print(student1)

#student3["subjects"].remove("art")
#print(student3)
student3.pop("age")
print(student3)