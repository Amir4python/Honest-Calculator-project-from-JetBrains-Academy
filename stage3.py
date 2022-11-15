'''# write your code here



def dosomething(x,y,oper):
        try:
            x=float(x)
            y=float(y)
        except ValueError:
            print(msg_1)
            return False
        if oper not in ['+','-','*','/']:
            print(msg_2)
            return False
        else: return True

while True:
    
        print(msg_0)   
        calc=input().split(" ")
        # print(calc,type(calc))
        x,oper,y=calc[0],calc[1],calc[2]
        if dosomething(x,y,oper):
            break
        
          
'''
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3='Yeah... division by zero. Smart move...'

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"



memory=0
def mg5():
  print(msg_5)
  answer=input()
  if answer=='y':
   mainfunction(True)
  elif answer=='n':
    mainfunction(False)
   

def mg4(result):
  global memory
  print(msg_4)
  answer=input()
  if answer=='y':
    memory=result
    mg5()
  elif answer!='y':
    if answer=='n':
      mg5()
    else:
      mg4(result)
  
def mainfunction(flag):
    global memory
    while flag:
            result=0
            print(msg_0)   
            calc=input().split(" ")
            # print(calc,type(calc))
            x,oper,y=calc[0],calc[1],calc[2]
    
            if x=="M":
                x=memory
            elif y=="M":
                y=memory
        
            try:
              x=float(x)
              y=float(y)
            except ValueError:
              print(msg_1)
           
            if oper not in ['+','-','*','/']:
              print(msg_2)
            else: 
              
              if oper=='+':
                result=x+y
                print(x+y)
              elif oper=='-':
                result=(x-y)
                print(x-y)
              elif oper=='*':
                  result=(x*y)
                  print(x*y)
              else:
                  try:
                      result=x/y
                      print(x/y)
                  except ZeroDivisionError:
                    print(msg_3)
                    break
     
            mg4(result)
    else:
      if flag==False:
        exit()


mainfunction(True)