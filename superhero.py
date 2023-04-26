import sqlite3

def show_all(conn):
    cursor = conn.cursor()
    cursor.execute('select * from superheroes')
    superheroes = cursor.fetchall()
 
    for hero in superheroes:
        print_details(hero)

def find_hero(conn):
    cursor = conn.cursor()
    chosen = input("Which superhero would you like to see? ").title()
    cursor.execute('select * from superheroes where hero_name=?;', (chosen, ))
    hero = cursor.fetchall()[0]
    print_details(hero)

def print_details(hero):
    print(hero[1].upper())
    print(f"They have the power of {hero[2]}.")
    print(hero[3])
    print()

    


with sqlite3.connect('superhero.db') as conn:
    show_all(conn)
    find_hero(conn)
    
