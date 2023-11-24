
e=True

import os as o
try:
    o.mkdir(("C://Python1"))
    
except:
     print("")



while(e==True):
    b=input("\n\n\n\nTo Open previous activity path type: c\nTo read type :r\nTo Overwrite type :w\nTo Append type :a\nTo Create a new file type w+\nTo delete a file type: x\nTo Exit press 1")
    if(b=="r"):
       a=input("Enter file path")
       c=open(a,b)
       print(c.read())
       p=c.name
       c.close()
       a=open("C://Python1//Previous","w")
       a.write(p)
       a.close()
        
    elif(b=="w"):
       a=input("Enter file path") 
       c=open(a,b)
       d=input("Enter Data to overwrite")
       c.write(d)
       p=c.name
       c.close()
       a=open("C://Python1//Previous","w")
       a.write(p)
       a.close()
        
    elif(b=="w+"):
        d=input("Enter file name")
        d="C://Python1//"+d
        c=open(d,"w")
        p=c.name
        d=input("Enter data to be inserted")
        c.write(d)
        c.close()
        print("File path  =",c.name)
        a=open("C://Python1//Previous","w")
        a.write(p)
        a.close()
        
    elif(b=="a"):
       a=input("Enter file path")
       c=open(a,b)
       p=c.name
       d=input("Enter data to append in your file")
       c.write(d)
       c.close()
       a=open("C://Python1//Previous","w")
       a.write(p)
       a.close()
        
    elif(b=="1"):
       e=False
    elif(b=="c"):
         try:
            c=open("C://Python1//Previous","r")
            print("Last Activity File Path :=",c.read())       
            c.close()
         except:   
            print("No Previous Actions Spotted")
            c=open("C://Python1//Previous","w")
            c.close()
    elif(b=="x"):
       a=input("Enter file path")
       o.unlink(a)
       print("File deleted sucessfully")
       
       
    else:
       print("Invalid Entry")
    

   





































#Sanidhya Vashishth





#Sanidhya Vashishth



#Sanidhya Vashishth

#Sanidhya Vashishth





#Sanidhya Vashishth

#Sanidhya Vashishth

































