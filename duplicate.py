Class={"student1":{"Name":"anay","age":13,"contactno":9786457890},
       "student2":{"Name":"rahul","age":14,"contactno":9786451234}}
student={"Name":"vinay", "age":17, "rollno":23}
print(Class)
print(student)

results={}
for key,value in Class.items():
    if value not in results.values():
        results[key]=value
print("After removing duplicates:",results)

