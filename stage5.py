msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3='Yeah... division by zero. Smart move...'

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


memory=0 


message=["Are you sure? It is only one digit! (y / n)"

, "Don't be silly! It's just one number! Add to the memory? (y / n)"

,"Last chance! Do you really want to embarrass yourself? (y / n)"
]


def demo(result):
 
  if is_one_digit(result):
    mgs_index=0 #0
    print(message[mgs_index])
    answer=input()
    while mgs_index<2 and answer=='y':
      mgs_index+=1
      print(message[mgs_index])
      answer=input()
    else:
      if answer=='n':
        return False
  else:
    return True #no













memory=0
def is_one_digit(v):
  if (v>-10) and (v<10) and v==int(v):
    output=True
  else:
    output=False
  return output


def check(v1,v2,v3):
  msg=""
  while True:
      if is_one_digit(v1) and is_one_digit(v2):
          msg+=msg_6    
      if (v1==1 or v2==1) and v3=="*":
            msg+=msg_7 #"" ... very lazy""
      if (v1==v2) and v3=="/":
            msg+=" ... lazy" #"" ... lazy""
            
      if (v1==0 or v2== 0) and (v3=="*" or v3=='+' or v3=='-'):
          msg+=msg_8 #  " ... very, very lazy"
   
      if msg !="":
          msg=msg_9+msg # "You are"
          print(msg)
      break
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

    #need to replace this 
    # result=memory_save(result)
    if demo(result):
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
            if y=="M":
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
                check(x,y,oper)
                result=x+y
                print(x+y)
              elif oper=='-':
                check(x,y,oper)
                result=(x-y)
                print(x-y)
              elif oper=='*':
                  check(x,y,oper)
                  result=(x*y)
                  print(x*y)
              else:
                  try:
                    # if str(x)=='M' and str(y)=='M':
                    #     x=1
                    #     y=1
                    #     result=x/y
                    #     print(x/y)
                    if x==y:
                        check(x,y,oper)
                    result=x/y
                    print(x/y)
                  except ZeroDivisionError:
                    print(msg_3)
                    mainfunction(True)
                    break
     
            mg4(result)
    else:
      if flag==False:
        exit()


mainfunction(True)