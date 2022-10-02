# Infinite calculator made by Rajat
# The blue color displays inputs for numbers and answers
# The red color displays inputs for operators
# It can perform the four basic functions (+, -, /, *) with their respective symbols as inputs


from colorama import Fore

a=float(input(Fore.BLUE+">>> "))



    
while(True):
        oper=input(Fore.LIGHTRED_EX+">> ")
        b=float(input(Fore.BLUE+">>> "))
        
        if oper=="+":
            s=a+b
            print("=", s)
            a=s
            continue
            
            

        elif oper=="-":
            d=a-b
            print("=",d)
            a=d
            continue
            
            

        elif oper=="*":
            p=a*b
            print("=",p)
            a=p
            continue
            

        elif oper=="/":
            pr=a/b
            print("=", pr)
            a=pr
            continue
            
            


