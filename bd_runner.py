from sqlite3 import OperationalError
import psycopg2, sys


from .Source.db_sous import *
from .Source.json_sous import * 


class Main:
    def __init__(self):
        try:
            self.connection = psycopg2.connect()
        except OperationalError as exjob:
            print("Error connection: ", exjob)
            sys.exit(1)
        print('connection successful!')

        
    def main(self):
        self.cur = self.connection.cursor()        

    def menu(self, a):
        print("""
                --MENU----------------
                1 - CREATE USER
                2 - CREATE ARTICLE
                3 - CREATE COMMENT
                4 - CONNECT db
                5 - exit
                anykey - restart menu
                ----------------------
            """)
        if a == 1:                          #Create User
            print("CREATE USER")

        if a == 2:                          #Create artile
            print("CREATE ARTICLE")
            self.cur.execute(article.__str__())

        elif a == 3:                        #Create comment
            print("CREATE COMMENT")

        elif a == 4:                        #Connect db
            print("CONNECT db")
            self.main()

        elif a == 5:                        #Quit
            print("QUIT")
            self.cur.close()
            self.connection.close()
            exit()
        
        elif a == 6:
            print("CREATE ARTICLE")         #Create article
            self.cur.execute()

        else:                               #Restart menu
            print("""
                --MENU----------------
                1 - CREATE USER
                2 - CREATE ARTICLE
                3 - CREATE COMMENT
                4 - CONNECT db
                5 - exit
                anykey - restart menu
                ----------------------
            """)
            self.menu(a =input("...> "))


if __name__ == "__main__":
    print("""
            --MENU----------------
            1 - CREATE USER
            2 - CREATE ARTICLE
            3 - CREATE COMMENT
            4 - CONNECT db
            5 - exit
            anykey - restart menu
            ----------------------
        """)
    #menu(a =input("...> "))



