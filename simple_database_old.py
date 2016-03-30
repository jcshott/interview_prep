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

def _set(var, val, database):
    # set var = val in database
    database[var] = val

def get(var, database):
    # print the var from database
    return database.get(var, "NULL")

def unset(var, database):
    del database[var]

def num_equal(val, database):
    count = 0
    
    for value in database.values():
        if value == val:
            count +=1
    return count

def loop(database):
    # get thing
    thing = raw_input()

    # parse thing
    commands = thing.split(" ") #list
    
    # do stuff with the thing
    command = commands[0]
    if command == "GET":
        print get(commands[1], database)
    if command == "SET":
        _set(commands[1], commands[2], database)
    if command == "UNSET":
        unset(commands[1], database)
    if command == "NUMEQUALTO":
        print num_equal(commands[1], database)

    if command == "END":
        return False
    
    return True

    
def main():
    my_db = {}

    running = True
    while running:
        running = loop(my_db)
            
        
def test():
    testdb = {}
    _set("A", 1, testdb)
    assert 1 == get("A", testdb)
        
        
if __name__ == "__main__":
    main()
    # test()
            