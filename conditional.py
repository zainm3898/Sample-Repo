# from ast import And
# from pickle import FALSE


condition = False
login = True

if condition and login:
    print("admin page")
elif condition == False and login == True:
    print("Login is true but coondotion is false")
else:
    print("both are not true")
