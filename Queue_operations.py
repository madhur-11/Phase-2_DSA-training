class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def enqueue(head,ele):
    t=Node(ele)
    if head==None:
        head=t
        return head
    temp=head
    while(temp.next!=None):
        temp=temp.next
    temp.next=t
    return head

def dequeue(head):
    if head==None or head.next==None:
        head=None
        return head
    head=head.next
    return head

def printq(head):
    if head==None:
        print('Queue is empty.')
        return None
    temp=head
    while(temp!=None):
        print(temp.data,'->',end='')
        temp=temp.next
    print('None')

head=None
while(1):
    print('Available Options: ')
    print('1.Enqueue.')
    print('2.Dequeue.')
    print('3.print.')
    print('4.Exit')
    choice=int(input('Enter your choice: '))
    if choice==1:
        t=int(input('Enter element to insert: '))
        head=enqueue(head,t)
    elif choice==2:
        head=dequeue(head)
        print('Last element removed.')
    elif choice==3:
        printq(head)
    elif choice==4:
        print('Exiting Code.')
        exit()
    else:
        print('Wrong Choice.')