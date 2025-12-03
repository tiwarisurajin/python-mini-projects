print("                  ************CALCULATOR*************")


while True  :
        result = float(input('Number : '))
        
        while True :
                
                op= input("+,-,*,/  or = for result : ")

                if  op == '=' :
                        print("RESULT :",result)
                        break
                num= float(input('Number : '))
                
                if op == '+':
                         result += num
                elif op == '-' :
                         result -= num
                elif op == '*' :
                         result *= num
                elif op == '/' and num == 0 :
                        print("You can't divide by zero")
                        break
                        
                else :
                        print('error ')


        repeat=input("To calculate again press c: " )
        if repeat.lower() != 'c' :
                break
        

                
                
            
