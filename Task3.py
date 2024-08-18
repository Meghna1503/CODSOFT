import random
Symbols=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o",
         "P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z",
         "1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")"]
print("<<-Welcome__To__Password__Generator->>")
len_password = int(input("Enter the length of your password:"))
Generate_Password = ""
for i in range(1, len_password+1):
    char = random.choice(Symbols)
    Generate_Password = Generate_Password+char
print(Generate_Password)