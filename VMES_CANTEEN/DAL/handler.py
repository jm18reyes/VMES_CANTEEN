import sqlite3
from datetime import datetime

class DataHandler(object):
    username = ""
    glob_table =""
    def __init__(self, db_file):
        self.dh = sqlite3.connect(db_file)
        self.c = self.dh.cursor()

    def AuthUser(self, user):
        print("--")
        print(user)
        DataHandler.username = user
        self.c.execute("SELECT ID FROM users WHERE username=?", (user,))
        id = self.c.fetchone()
        print(id)
        if id is None:
            return False
        else:
            return True

    def AuthPass(self):
        self.c.execute("SELECT pass FROM users WHERE username=?", (DataHandler.username,))
        password, = self.c.fetchone()
        self.c.execute("SELECT job FROM users WHERE username=?", (DataHandler.username,))
        jobPosition, = self.c.fetchone()
        return password, jobPosition

    def getMenu(self, table):
        DataHandler.glob_table = table
        self.sql = "SELECT menu, price, id FROM "+ table
        self.c.execute(self.sql)
        results = self.c.fetchall()
        return results

    def AddUser(self,newUser,passWord,job):
        self.c.execute("INSERT INTO users (username, pass, job) VALUES (?, ?, ?)",(newUser,passWord,job))
        self.dh.commit()

    def getAllUsers(self):
        self.sql = "SELECT ID, username, pass, job FROM users"
        self.c.execute(self.sql)
        results = self.c.fetchall()
        return results

    def deleteUser(self,id):
        self.strn = str(id)
        self.sql = "DELETE FROM users WHERE ID="+self.strn
        print("sql",self.sql)
        self.c.execute(self.sql)
        self.dh.commit()

    def deleteFood(self,mealTime,id):
        print(mealTime)
        self.mealTime = str(mealTime)
        self.id = str(id)
        self.sql = "DELETE FROM "+self.mealTime+" WHERE ID = "+self.id
        self.c.execute(self.sql)
        self.dh.commit()

    def updateUser(self,id,newPass,newType):
        self.strn1 = str(id)
        self.strn2 = str(newPass)
        self.strn3 = str(newType)
        self.c.execute("UPDATE users SET pass=?,job=? WHERE ID =?",(self.strn2,self.strn3,self.strn1))
        self.dh.commit()

    def updateMenu(self,mealTime,food,price,Status):
        self.c.execute("UPDATE "+mealTime+" SET price=?,status=? WHERE menu =?",(price,Status,food))
        self.dh.commit()

    def AddMenu(self,mealTime,food,price):
        print(mealTime)
        self.c.execute("INSERT INTO "+mealTime+" (menu, price) VALUES (?, ?)",(food, price))
        self.dh.commit()

    def saveOrder(self,Food,Price,randomNum):
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y-%H:%M-")+str(randomNum)
        self.c.execute("INSERT INTO orderedItems (food, price, dTime) VALUES (?, ?, ?)",(Food, Price, self.dt_string))
        self.dh.commit()

    def getLatestOrder(self):
        #pass
        self.c.execute("SELECT dTime FROM orderedItems ORDER BY id DESC LIMIT 1;")
        self.latestTime, = self.c.fetchone()
        print(str(self.latestTime))
        self.c.execute("SELECT food, price FROM orderedItems WHERE dTime = "+'"'+str(self.latestTime)+'"')
        results = self.c.fetchall()
        return results

    def getAllOrders(self):
        self.c.execute("SELECT food, price, dTime FROM orderedItems")
        results = self.c.fetchall()
        return results

    def deleteSoldItems(self):
        self.c.execute("DELETE FROM orderedItems")
        self.dh.commit()

