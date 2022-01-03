usr=["jeffdie",]
ERR1 = "ERROR: Username Already Taken \n\n\n (Error code:1)"
usrin=False
acgr="Access Granted"
while not usrin:
    print('please input a username or type "NewName" to add a new account')
    e=input()
    if(e=="NewName"):
        usrin=True
        addacc()
    else:
        try:
            for x in usr:
                if (x==e):
                    print(acgr)


def addacc():
    global usr, ERR1
    print("please input new username, no spaces allowed")
    usre = input()
    for x in usr:
        if not (x=usre):
            usr.append(usre)
            print(acgr)
            break
        else:
            print(ERR1)
