# https://www.thumbtack.com/challenges/simple-database

# dict - variables = key, value

## Description:
## Take input of commands and update database accordingly
## [take things and do stuff to database]
## 

# SET function - would add a key, val pair to the database

# GET - get the val from db givn a key

# unset  - del the key/val from db

# numequalto - find all vals == to given val and print list of keys

# END - exit program

#Things you can do:
 #   set, get, unset, numequalto, end
    
#Stuff it does:
 #   to database - dictionary
    
# 

class Database(object):

    def __init__(self):
        self.db = {}
        self.transaction_hist = [self.db]

    def get(self, var):
        # print the var from database
        
        for i in xrange(len(self.transaction_hist), 0, -1):
            if var in self.transaction_hist[i-1]:
                return self.transaction_hist[i-1][var]

        return "NULL"

    def _set(self, var, val):
        # set var = val in most recent database, either a transaction one or the base

        self.transaction_hist[-1][var] = val


    def unset(self, var):

        for i in xrange(len(self.transaction_hist), 0, -1):
            if var in self.transaction_hist[i-1]:
                del transaction_hist[i-1][var]

    def num_equal(self, val):
        count = 0
        
        for value in self.transaction_hist[-1].values():
            if value == val:
                count +=1

        return count

    def transaction(self):
        # add a new db to the transaction history that is equal to 
        new_db = {}

        # if len(self.transaction_hist) > 0:
        #     new_db = self.transaction_hist[-1]
        
        # else:
        #     new_db = self.db
        
        self.transaction_hist.append(new_db)
        print self.transaction_hist

    def rollback(self):
        # remove last temp db
        if len(self.transaction_hist) > 1:
            self.transaction_hist.pop()
        else:
            print "NO TRANSACTION"
        print self.transaction_hist
        print self.db
    
    def commit(self):
        # integrate changes from transaction history into base db
        if len(self.transaction_hist) == 1:
            print "NO TRANSACTION"
        else:
            for x in xrange(len(self.transaction_hist)-1, 0, -1):
                print self.transaction_hist[x]
                for key, val in self.transaction_hist[x].items():
                    self.db[key] = val
                    self.transaction_hist.pop()


def main():
    my_db = Database()

    while True:
        # get thing
        thing = raw_input()

        # parse thing
        command_lst = thing.split(" ") #list
        
        # do stuff with the thing
        command = command_lst[0]
        
        if command == "GET":
            print my_db.get(command_lst[1])
        
        if command == "SET":
            my_db._set(command_lst[1], command_lst[2])
        if command == "UNSET":
            my_db.unset(command_lst[1])
        if command == "NUMEQUALTO":
            print my_db.num_equal(command_lst[1])
        
        if command == "BEGIN":
            my_db.transaction()
        
        if command == "ROLLBACK":
            my_db.rollback()

        if command == "COMMIT":
            my_db.commit()

        if command == "END":
            return False
            
        
def test():
    testdb = {}
    _set("A", 1, testdb)
    assert 1 == get("A", testdb)
        
        
if __name__ == "__main__":
    main()
    # test()
            