passed = input("Enter True or False = ")

if passed == 'True':
   result = 'You can go futher in you study!'
   
elif passed == 'False': 
    result = 'You have failed the Exam!'
    
else:
    print("Given input is wrong!")  
    result = None
        
if result is not None:
   print(result)
    
     