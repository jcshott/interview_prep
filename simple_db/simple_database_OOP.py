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
import sys

class Database(object):

    def __init__(self):
        self.db = {} # holds current db
        self.transaction_hist = [self.db] # holds transactions, cleared (except base) on commit

    def get(self, var):
        # get var from db - search from most recent transaction back to base db. 
        # if not found, return NULL
        return self.transaction_hist[-1].get(var, "NULL")
        # for i in xrange(len(self.transaction_hist), 0, -1):
        #     if var in self.transaction_hist[i-1]:
        #         return self.transaction_hist[i-1][var]

        # return "NULL"

    def _set(self, var, val):
        # set var = val in most recent database, either a transaction one or the base

        self.transaction_hist[-1][var] = val


    def unset(self, var):

        for i in xrange(len(self.transaction_hist), 0, -1):
            if var in self.transaction_hist[i-1]:
                del self.transaction_hist[i-1][var]
                break

    def num_equal(self, val):
        # return num in most recent transaction (or base if no transaction hist)
        count = 0
        
        for value in self.transaction_hist[-1].values():
            if value == val:
                count +=1

        return count

    def transaction(self):
        # add a new db-dict to the transaction history for rollback/commit record
        new_db = self.transaction_hist[-1].copy()
        
        self.transaction_hist.append(new_db)

    def rollback(self):
        # remove last temp db
        if len(self.transaction_hist) > 1:
            self.transaction_hist.pop()
        else:
            print "NO TRANSACTION"
    
    def commit(self):
        # integrate changes from transaction history into base db
        # if multiple transactions change same key/var in db, the most recent transaction wins
        if len(self.transaction_hist) == 1:
            print "NO TRANSACTION"
        else:
            for transaction in self.transaction_hist[1:]:
                for key, val in transaction.items():
                    self.db[key] = val
            self.transaction_hist = [self.db]


def process_commands(command_lst, db):
        command = command_lst[0].lower()
        # do stuff
        if command == "get":
            print db.get(command_lst[1])
        if command == "set":
            db._set(command_lst[1], command_lst[2])
        if command == "unset":
            db.unset(command_lst[1])
        if command == "numequalto":
            print db.num_equal(command_lst[1])
        if command == "begin":
            db.transaction()
        if command == "rollback":
            db.rollback()
        if command == "commit":
            db.commit()
        if command == "end":
            return False
        # if command == "end":
        #     return False
            

def main(user, file_name=None):
    my_db = Database()

    # user makes inputs in terminal
    if user == "interactive":
        while True:
            # get thing
            user_input = raw_input()

            # parse thing
            command_lst = user_input.split(" ") #list
            
            # do stuff with the thing
            command = command_lst[0].lower()
            
            if command == "end":
                return False
            
            process_commands(command_lst, my_db)
    
    # file input of commands
    else:
        while True:
        # gets all commands in given file
            file_commands_lst = [line.rstrip() for line in open(file_name)]
            for item in file_commands_lst:
                command_lst = item.split(" ")

                command = command_lst[0].lower()

                if command == "end":
                    return False
                    # sys.exit()

                process_commands(command_lst, my_db)
        
def test():
    testdb = Database()
    
    # basic set & get
    testdb._set("A", 10)
    assert 10 == testdb.get("A")

    # num_equal
    testdb._set("B", 20)
    testdb._set("C", 20)
    assert 2 == testdb.num_equal(20)

    # transaction & rollback
    testdb.transaction()
    testdb._set("D", 40)
    assert 40 == testdb.get("D") 

    testdb.rollback()
    assert "NULL" == testdb.get("D")    

    # transaction & commit
    testdb.transaction()
    testdb._set("F", 500)
    testdb.commit()
    assert 500 == testdb.db["F"]

if __name__ == "__main__":
    # main - if no file input with commands given, then program waits for user input
    if len(sys.argv) == 1:
        main("interactive")
    
    else:
        # run in test mode
        if sys.argv[1] == "test":
            test()
        # file input can list several files with commands
        else:
            for f_name in sys.argv[1:]:
                main("file", f_name)
            