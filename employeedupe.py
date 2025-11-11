staff={"emp1":{"name":"john","post":"manager"},
        "emp2":{"name":"doe","post":"developer"},
        "emp3":{"name":"joe","post":"designer"},
        "emp4":{"name":"john","post":"manager"},
          }
results={}
print(staff)
for key,value in staff.items():
    if value not in results.values():
        results[key]=value
print("After removing duplicates:",results)