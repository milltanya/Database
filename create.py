import sqlite3


def create_database():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Route (
            id_route INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            number TEXT NOT NULL,
            begin DATE NOT NULL,
            end DATE
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Card (
            id_card INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            period INTEGER NOT NULL,
            payment INTEGER NOT NULL,
            max_number INTEGER,
            cost INTEGER NOT NULL,
            begin DATE NOT NULL,
            end DATE
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Concrete_card (
            id_card INTEGER PRIMARY KEY AUTOINCREMENT,
            card_type INTEGER NOT NULL REFERENCES Card(id_card),
            account INTEGER NOT NULL,
            begin DATE NOT NULL
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Trip  (
            card INTEGER NOT NULL REFERENCES Concrete_card(id_card),
            route INTEGER NOT NULL REFERENCES Route(id_route),
            moment DATE NOT NULL,
            PRIMARY KEY (card, moment)
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Station (
            id_station INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            coordinate_x DOUBLE NOT NULL,
            coordinate_y DOUBLE NOT NULL,
            UNIQUE (coordinate_x, coordinate_y)
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Route_Station (
            route INTEGER NOT NULL REFERENCES Transport (id_route),
            direction INTEGER NOT NULL,
            station INTEGER REFERENCES Station (id_station),
            next_station INTEGER REFERENCES Station (id_station),
            UNIQUE (route, direction, next_station),
            PRIMARY KEY (route, direction, station)
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Route_Shift (
            id_shift INTEGER PRIMARY KEY AUTOINCREMENT,
            begin TIME NOT NULL,
            end TIME NOT NULL,
            UNIQUE (begin, end)
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Route_Schedule (
            route INTEGER NOT NULL REFERENCES Transport (id_route),
            days TEXT NOT NULL,
            shift INTEGER NOT NULL REFERENCES Route_Shift (id_shift),
            interval TIME NOT NULL,
            begin DATE NOT NULL,
            end DATE,
            PRIMARY KEY (route, days, shift, begin)
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Model (
            id_model INTEGER PRIMARY KEY AUTOINCREMENT,
            producer TEXT NOT NULL,
            model TEXT NOT NULL,
            type TEXT NOT NULL,
            seat INTEGER NOT NULL,
            capacity INTEGER NOT NULL,
            description TEXT
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Vehicle (
            id_vehicle INTEGER PRIMARY KEY AUTOINCREMENT,
            model INTEGER NOT NULL REFERENCES Model (id_Model),
            date_manufacture INTEGER NOT NULL,
            number TEXT NOT NULL UNIQUE,
            begin DATE NOT NULL,
            end DATE
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Driver (
            id_driver INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            experience INTEGER NOT NULL,
            birthday DATE NOT NULL,
            begin DATE NOT NULL,
            end DATE
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Driver_Shift (
            id_shift INTEGER PRIMARY KEY AUTOINCREMENT,
            begin TIME NOT NULL,
            end TIME NOT NULL,
            UNIQUE (begin, end)
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Driver_Schedule (
            day DATE NOT NULL,
            shift INTEGER NOT NULL REFERENCES Driver_Shift (id_shift),
            driver INTEGER NOT NULL REFERENCES Driver (id_driver),
            vehicle INTEGER NOT NULL REFERENCES Vehicle (id_vehicle),
            route INTEGER NOT NULL REFERENCES Transport (id_route),
            UNIQUE (day, shift, vehicle),
            PRIMARY KEY (day, shift, driver)
        );
    ''')
    conn.commit()
    conn.close()


create_database()
