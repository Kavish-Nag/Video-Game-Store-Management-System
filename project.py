import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
D1={}
money={}

def home():
     print("                     ==============================")
     print("                                  MENU")
     print("                     ==============================")
     print("","1. LOGIN","\n","2. New User? Sign Up","\n","3. Exit")
     ch=int(input("Enter Choice:"))
     if ch==1:
          login()
     elif ch==2:
          new_user()
     else:
          exit()
          
def buy():
     print("Verify user to proceed")
     name=input("Enter name")
     if name in D1:
          print("","1. Console","\n","2. Games ","\n","3. Home")
          prod=int(input("Enter choice:"))
          if prod==1:
               df_console=pd.read_csv("console.csv")
               print(df_console)
               print("Which one would you like to buy")
               b=int(input("Enter index:"))
               if b >= 0 and b < len(df_console):
                    pur = df_console.loc[b, "Price (in Rs)"]
                    df_console.loc[b, 'Qty'] -= 1
                    print(pur)
                    print(f"Total cost so far: Rs {pur}")
                    print("Successfully purchased!")
                    dff=pd.DataFrame({"User":[name],"Amt":[pur]})
                    dff.to_csv("money.csv",index= False,header=False,mode="a")
                    again()
               else:
                    print("Invalid index. Please enter a valid index.")
          elif prod==2:
               df_games=pd.read_csv("games.csv")
               print(df_games)
               print("Which one would you like to buy")
               b=int(input("Enter index:"))
               if b >= 0 and b < len(df_games):
                    pur = df_games.loc[b, "Price (in Rs)"]
                    df_games.loc[b, 'Qty'] -= 1
                    print(pur)
                    print(f"Total cost so far: Rs {pur}")
                    print("Successfully purchased!")
                    dff=pd.DataFrame({"User":[name],"Amt":[pur]})
                    dff.to_csv("money.csv",index= False,header=False,mode="a")                  
                    again()
               else:
                    print("Invalid index. Please enter a valid index.")
          elif prod==3:
               home()
          else:
               print("Out of range")
               buy()
     else:
          print("Verification Failed")
          home()
          
def login():
     print("                     ++++++++++++++++++++++++++++++")
     print("                                LOGIN PAGE")
     print("                     ++++++++++++++++++++++++++++++")
     n=input("Enter Name:")
     if n in D1.keys():
          ps=input("Enter password:")
          if D1[n]==ps:
               print("WELCOME",n)
               try1()
          else:
               print("Incorrect password")
     else:
          print("You haven't registered")
          
def try1():
     print("                     ==============================")
     print("                                  MENU")
     print("                     ==============================")
     print("","1. Buy a product.","\n","2. Log out")
     select=int(input("Enter choice:"))
     if select==1:
          buy()
     else:
          home()

def again():
     print("Would u like to buy something else?")
     print("Y/N")
     en=input("")
     if en=="Y" or en=="y":
          buy()
     elif en=="n" or en=="N":
          print("Thank you for the purchase.")
     else:
          print("Not a valid choice")
          again()
          
def new_user():
     print("                     ++++++++++++++++++++++++++++++++++++++++")
     print("                                REGISTER YOURSELF")
     print("                     ++++++++++++++++++++++++++++++++++++++++")
     n=input("Enter Name:")
     ps=input("Set a password:")
     D1[n]=ps
     money[n]=0
     dflogin=pd.DataFrame({"User":[n],"Password":[ps]})
     dflogin.to_csv("login.csv",index= False,header=False,mode="a")
     try1()
     
def admin():
     print("                     ==============================")
     print("                                  MENU")
     print("                     ==============================")
     print("","1. View Employees.","\n","2. View products.","\n","3. Sales","\n","4. Exit")
     ec=int(input("Enter Choice:"))
     if ec==1:
          print("Employees")
          data=pd.read_csv("employees.csv")
          print(data)
          print("What graph do u want?")
          print("                     ++++++++++++++++++++++++++++++++++++++++")
          print("                                MENU")
          print("                     ++++++++++++++++++++++++++++++++++++++++")
          print("","1. Line graph","\n","2. Bar graph","\n","3. Pie graph","\n","4. Scatter graph")
          choice=int(input("Enter choice:"))
          NOE="Name of Employee"
          Salary=" Salary "
          x=data[NOE]
          y=data[Salary]
          plt.title("Employees Info")
          plt.xlabel("Name of Employee")
          plt.ylabel("Salary")
          if choice==1:
               plt.plot(x,y)  
          elif choice==2:
               plt.bar(x,y)
          elif choice==3:
               plt.axis("equal")
               plt.pie(y,labels=x)
          else:
               plt.scatter(x,y)   
          plt.show()
          admin()
     elif ec==2:
          prods()
     elif ec==3:
          moneh()
     else:
          exit()

def prods():
     print("","1. Console","\n","2. Games ","\n","3. Back")
     hm=int(input("Enter Choice:"))
     if hm==1:
          df_console=pd.read_csv("console.csv")
          print(df_console)
          print("What graph do u want?")
          print("                     ++++++++++++++++++++++++++++++++++++++++")
          print("                                MENU")
          print("                     ++++++++++++++++++++++++++++++++++++++++")
          print("","1. Line graph","\n","2. Bar graph","\n","3. Pie graph","\n","4. Scatter graph")
          choice=int(input("Enter choice:"))
          NOP="Name of Product"
          price="Price (in Rs)"
          x=df_console[NOP]
          y=df_console[price]
          plt.title("Price chart for consoles")
          plt.xlabel("Name of Product")
          plt.ylabel("Price(in RS)")
          if choice==1:
               plt.plot(x,y)
          elif choice==2:
               plt.bar(x,y)
          elif choice==3:
               plt.axis("equal")
               plt.pie(y,labels=x)
          else:
               plt.scatter(x,y)
          plt.show()
          prods()
     elif hm==2:
          df_games=pd.read_csv("games.csv")
          print(df_games)
          print("                     ++++++++++++++++++++++++++++++++++++++++")
          print("                                MENU")
          print("                     ++++++++++++++++++++++++++++++++++++++++")
          print("What graph do u want?")
          print("","1. Line graph","\n","2. Bar graph","\n","3. Pie graph","\n","4. Scatter graph")
          choice=int(input("Enter choice:"))
          NOP= "Name of Product"
          price="Price (in Rs)"
          x=df_games[NOP]
          y=df_games[price]
          plt.title("Price chart for games")
          plt.xlabel("Name of Product")
          plt.ylabel("Price(in RS)")
          if choice==1:
               plt.plot(x,y)
          elif choice==2:
               plt.bar(x,y)
          elif choice==3:
               plt.axis("equal")
               plt.pie(y,labels=x) 
          else:
               plt.scatter(x,y) 
          plt.show()
          prods()
     else:
          admin()
             
def moneh():
     dff=pd.read_csv("money.csv")
     print(dff)
     print("                     ++++++++++++++++++++++++++++++++++++++++")
     print("                                MENU")
     print("                     ++++++++++++++++++++++++++++++++++++++++")
     print("What graph do u want?")
     print("","1. Line graph","\n","2. Bar graph","\n","3. Pie graph","\n","4. Scatter graph")
     choice=int(input("Enter choice:"))
     U= "User"
     Amt="Amt"
     x=dff[U]
     y=dff[Amt]
     plt.xlabel('X-axis')
     plt.ylabel('Y-axis')
     plt.title('Plot from Dictionary Values')
     if choice==1:
          plt.plot(x,y)    
     elif choice==2:
          plt.bar(x,y) 
     elif choice==3:
          plt.axis("equal")
          plt.pie(y,labels=x)
     else:
          plt.scatter(x,y) 
     plt.show()
     admin()
          
while True:
     df2=pd.read_csv("login.csv")
     bd=df2.set_index("User").T.to_dict("records")
     bd1=bd[0]
     D1.update(bd1)
     print("                     ++++++++++++++++++++++++++++++++++++++++")
     print("                                Welcome")
     print("                     ++++++++++++++++++++++++++++++++++++++++")
     print("","1. User","\n","2.Admin","\n","3.Employee")
     a=int(input("Enter Choice:"))
     if a==1:
          home()
     elif a==2:
          n=input("Enter Name:")
          if n=="Admin":
               ps=input("Enter password:")
               if ps=="admin":
                    print("WELCOME",n)
                    admin()
               else:
                    print("Incorrect password")
          else:
               print("Invalid User")
     elif a==3:
          em=input("Enter Name:")
          data=pd.read_csv("employees.csv")
          df=pd.DataFrame(data)
          result= em in df.values
          if result == True:
               print("                     ++++++++++++++++++++++++++++++++++++++++")
               print("                                Welcome",em)
               print("                     ++++++++++++++++++++++++++++++++++++++++")
               print("                     ==============================")
               print("                                  MENU")
               print("                     ==============================")
               print("","1. View your info","\n","2.View products","\n","3.Exit")
               b=int(input("Enter Choice:"))
               if b==1:
                    
                    df.set_index("Name of Employee",inplace=True)
                    print(df.loc[em])
               elif b==2:
                    print("","1. Console","\n","2. Games")
                    c=int(input("Enter choice:"))
                    if c==1:
                         df_console=pd.read_csv("console.csv")
                         print(df_console)
                    else:
                         df_games=pd.read_csv("games.csv")
                         print(df_games)
               else:
                    exit()     
          else:
               print("Not registered")
     else:
          exit()

          
