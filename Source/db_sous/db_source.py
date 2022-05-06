def id_serial_fields():
    return "id serial PRIMARY KEY"

def varchar_fields(name):
    return '{0} varchar'.format(name)

def text_fields(name):
    pass

def integer_fields(name):
    return "{0} integer".format(name)


class RootTable:
    def __init__(self, **data):
        self.data = data

    def call(self):
        print('------------------------\n', self.data.items())
        for key, value in self.data.items():
            print("{} is {}".format(key, value))
        return 1
        
test = RootTable(FirstName="lolja", LastName="dauther", Age=16, PhoneNumber=88005553535)
test.call()

class ArticleTable(RootTable):
    def __init__(self, name, **data):
        RootTable.__init__(self, **data)
        self.name = name
        self.id = id_serial_fields()
        self.title = varchar_fields("title")
        self.veiws = integer_fields("views")

    def __str__(self):
        return "CREATE TABLE {0} ({1}, {2}, {3})".format(article.name, article.id, article.title, article.veiws)

article = ArticleTable(str(input("Table name: ")))

#print("CREATE TABLE {0} ({1}, {2}, {3})".format(article.name, article.id, article.title, article.veiws))

'''
def InputInTable(name ,*num, **data):
    nameTable = name
    mass = [data]
    val = [num]

    return "INSERT INTO {nameTable}, ({mass}) VALUES ({val})".format(nameTable, mass, val)
'''
#nameTable =  ArticleTable.__class__.__name__