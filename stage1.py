msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


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
        
          
