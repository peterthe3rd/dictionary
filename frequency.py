Class={"student1":5,"student2":4,"student3":9,"student4":9}
print(Class)
val=int(input("Enter the value you want to check: "))   
count=0
for i in Class:
    if Class[i]==val:
        count+=1
print(f"the value {val} occurs {count} times in the dictionary")