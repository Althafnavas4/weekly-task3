user_dtls=[]
lib=[]

def register():
    if len(user_dtls)==0:
        id=100
    else:
        id=user_dtls[-1]['id']+1
    print(id)

    email=str(input("enter the email :"))
    f1=0
    for i in user_dtls:
        if i['email']==email:
            f1=1
            register()
    if f1==0:
    
            name=str(input("enter the name :"))
            phone=int(input("enter the  phone number:"))
            username=email
            password=input('enter the password:')
            user_dtls.append({'name':name,'id':id,'phone':phone,'email':email,'password':password,'books':[]})

def login():
    uname=input('enter username:')
    passw=input('enter password:')
    f=0
    if uname=='admin' and passw=='admin':
        f=1
    user=''
    for i in user_dtls:
        if uname==i['email'] and passw==i['password']:
            f=2
            user=i
    return f,user
def add_shoes():
    if len(lib)==0:
        id=1
    else:
        id=lib[-1]['id']+1
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            add_shoes()
    
   
    name=str(input("enter the name :"))
    price=int(input("enter the  price:"))
    stock=int(input('enter the stock:'))
    size=int(input('enter size'))
    lib.append({'name':name,'price':price,'stock':stock,'size':size,'id':id})
def view_shoes():
    print(lib)
def ubdate_shoes():
    id=int(input('enter id :'))                                                         
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            price=int(input('enter price :'))                                   
            stock=str(input('enter stock :'))
            i['price']=price
            i['stock']=stock
    if f1==0:
        print('invalid id')
    
def delete():
    id=int(input('enter id :'))
    f1=0
    for i in lib:
        if i['id']==id:
            f1=1
            lib.remove(i)

    if f1==0:
        print('invalid id')


def  view_user():
    for i in user_dtls:
        print('name',i['name'])
        print('id',i['id'])
        print('email',i['email'])
        print('phone',i['phone'])
            
def view_profile(user):
    print(user)
    
def ubdate_profile(user):
    name=str(input("enter the name :"))
    phone=int(input("enter phone no :"))
    user['name']=name
    user['phone']=phone
def view_shoes():
    print(lib)
def buy_shoes(user):
    id=int(input('enter the id:'))
    f=0
    for i in lib:
        if i ['id']==id:
            f=1
            i['stock']-=1
            user['shoess'].append(id)
            print('shoes added')
        if f==0:
            print('invlid')









while True:
    print('''
1.register
2.login
3.exit
''')
    choice=int(input('enter your choice:'))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                1.add shoes
                2.view shoes
                3.ubdate shoes
                4.delete
                5.view user
                6.exit
                ''')
                sub_choice=int(input("enter the choice :"))
                if sub_choice==1:
                    add_shoes()
                elif sub_choice==2:
                    view_shoes()
                elif sub_choice==3:
                    ubdate_book()
                elif sub_choice==4:
                    delete()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break
                else:
                    print('invalid')



            
        elif f==2:
            while True:
                print('''
                1.view profile
                2.ubdate profile
                3.view shoes
                4.buy shoes
        
               
                6.exit
                ''')
                sub_ch=int(input('enter the choice:'))
                if sub_ch==1:
                    view_profile(user)
                elif sub_ch==2:
                    ubdate_profile(user)
                elif sub_ch==3:
                    view_shoes()
                elif sub_ch==4:
                    buy_shoes(user)
          
                

                elif sub_ch==6:
                    break
                else:
                    print('invalid')
                


            
        elif f==0:
            print('invalid username or password')

    elif choice==3:
        break
    else:
        print('invalid')