stack=[]
def push(stack,ele):
    stack.insert(0,ele)

def spop(stack):
    if len(stack)==0:
        print('Stack is empty')
    else:
        stack.pop(-1)

def prints(stack):
    if stack==None:
        print('Stack is empty.')
    else:
        print(stack[-1],'-> Tos')
        for i in range(len(stack)-2,0,-1):
            print(stack[i])
        print(stack[0])

while(1):
    print('Available Options: ')
    print('1.Push.')
    print('2.Pop.')
    print('3.print.')
    print('4.Exit')
    choice=int(input('Enter your choice: '))
    if choice==1:
        t=int(input('Enter element to push: '))
        push(stack,t)
    elif choice==2:
        spop(stack)
        print('Tos element removed.')
    elif choice==3:
        prints(stack)
    elif choice==4:
        print('Exiting Code.')
        exit()
    else:
        print('Wrong Choice.')