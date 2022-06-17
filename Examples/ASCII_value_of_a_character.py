K = input("Please enter a character: ")    
    
print ("The ASCII value of '" + K + "' is ", ord(K))  

print ("Please enter the String: ", end = "")  
string = input()  
string_length = len(string)  
for K in string:  
    ASCII = ord(K)  
    print (K, "\t", ASCII)  
    
    
K = 21    
J = 123  
R = 76  
print ("The character value of 'K' ASCII value is: ", chr(K))    
print ("The character value of 'J' ASCII value is: ", chr(J))    
print ("The character value of 'R' ASCII value is: ", chr(R))  