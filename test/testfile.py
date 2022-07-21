count = 0
for i in range(100):
    
    if count % 3 == 0:
        if count % 5 == 0:
            print(f"{count} is foo boo")
        
        else:
            print(f"{count} is foo")
            
    if count % 5 == 0:
        print(f"{count} is boo")
    
    count += 1