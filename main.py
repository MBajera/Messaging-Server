from create_db import db_creation, db_tables_creation
from message_support import message_support
from models import User, Messages
from user_support import user_support

base = input("Welcome in Messaging Serwer!\n You want to create new DB or use existing one? \n"
             "Write 'new' to create new DB or 'existing' to use existing DB: ")
if base == 'new':
    db_created = False
    while not db_created:
        db_name = input("Enter database name: ")
        db_created = db_creation(db_name)
        if not db_created:
            print("DB creation failed. There is already a database with the given name. Try again.")
        else:
            print(f"Congratulations! DB '{db_name}' created!")
    db_tables_creation(db_name)
    User.db_name = db_name
    Messages.db_name = db_name
elif base == 'existing':
    existing_base_name = input("Write base name: ")
    User.db_name = existing_base_name
    Messages.db_name = existing_base_name


while True:
    decision = int(input("""Write number of fuction you want to choose:
    1 - User support
    2 - Message support
    3 - Exit
    """))
    if decision == 3:
        break
    elif decision == 1:
        user_support()
    elif decision == 2:
        message_support()

print("Bye!")