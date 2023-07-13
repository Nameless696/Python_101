try:
   for w in range(1,10,1):
    print(w)("hello")
    if w == 3:
     break 
 
    print("program has ended")
    print()
except:
    print("something is wrong")
    
try:  
 for i in range(1,20,1):
    print(i)
    if i == 9:
     continue
 print("Program has ended") 
except:
    print("something went wrong")

