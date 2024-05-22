class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def insertathead(head,ele):
    t=Node(ele)
    if head==None:
        head=t
        return head
    t.next=head
    head=t
    return head

def insertattail(head,ele):
    t=Node(ele)
    if head==None:
        head=t
        return head
    temp=head
    while(temp.next!=None):
        temp=temp.next
    temp.next=t
    return head

def insertatpos(head,pos,ele):
    t=Node(ele)
    if head==None:
        head=t
        return head
    temp=head
    for i in range(pos-2):
        temp=temp.next
    if temp.next==None:
        temp.next=t
        return head
    t.next=temp.next.next
    temp.next=t
    return head

def delattail(head):
    if head==None or head.next==None:
        head=None
        return head
    temp=head
    while(temp.next.next!=None):
        temp=temp.next
    temp.next=None
    return head

def delathead(head):
    if head==None or head.next==None:
        head=None
        return head
    head=head.next
    return head

def delatpos(head,pos):
    if head==None or head.next==None:
        head=None
        return head
    temp=head
    for i in range(pos-2):
        temp=temp.next
    temp.next=temp.next.next
    return head

def printll(head):
    if head==None:
        print('Linked list is empty.')
        return None
    temp=head
    while(temp!=None):
        print(temp.data,'->',end='')
        temp=temp.next
    print('None')

head=None
c=0
while(1):
    print('Available Operations:')
    print('1.Insert.')
    print('2.Delete.')
    print('3.Print.')
    print('4.Exit.')
    choice=int(input('Enter your choice: '))
    if c==0 and choice==2:
        print('No elements left in Linked List.')
    elif choice==1:
        print('Available options:')
        print('1.Insertion at Beginning.')
        print('2.Insertion at Position.')
        print('3.Insertion at end.')
        o=int(input('Enter the required option: '))
        if o==1:
            ele=int(input('Enter the element to insert: '))
            head = insertathead(head,ele)
            c+=1
        elif o==2:
            ele=int(input('Enter the element to insert: '))
            pos=int(input('Enter position to insert element: '))
            if pos<1 or pos>(c+1):
                print('Invalid position.')
            else:
                head = insertatpos(head,pos,ele)
                c+=1
        elif o==3:
            ele=int(input('Enter element to insert: '))
            head = insertattail(head,ele)
            c+=1
        else:
            print('Invalid option.')
    elif choice==2:
        if c==0:
            print('Linked List is already empty.')
        else:
            print('Available options:')
            print('1.Deletion at Beginning.')
            print('2.Deletion at Position.')
            print('3.Deletion at end.')
            o = int(input('Enter the required option: '))
            if o == 1:
                head = delathead(head)
                c -= 1
            elif o == 2:
                pos = int(input('Enter position to delete element: '))
                if pos < 1 or pos > (c):
                    print('Invalid position.')
                else:
                    head = delatpos(head, pos)
                    c -= 1
            elif o == 3:
                head = insertattail(head)
                c -= 1
            else:
                print('Invalid option.')
    elif choice==3:
        printll(head)
    elif choice==4:
        print('Ending session.')
        exit()
    else:
        print('Invalid Choice.')