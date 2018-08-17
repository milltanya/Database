import sqlite3
import random


def fill_route():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    f = open("Виды транспорта.txt", 'r')
    transport = []
    for line in f:
        transport.append(line.strip())
    f.close()
    cur.execute('''
        INSERT OR IGNORE INTO Route (type, number, begin)
        VALUES ("bus", "32", "2012-04-13")
    ''')
    cur.execute('''
        INSERT OR IGNORE INTO Route (type, number, begin)
        VALUES ("bus", "1", "2012-04-13")
    ''')
    cur.execute('''
        INSERT OR IGNORE INTO Route (type, number, begin)
        VALUES ("bus", "68", "2012-04-13")
    ''')
    letters = ['e', 't', '', '', '', '']
    for i in range(100):
        type = random.choice(transport)
        number = '1'
        while number in ['32', '68', '1']:
            number = str(random.randint(1, 99)) + random.choice(letters)
        cur.execute('''
            INSERT OR IGNORE INTO Route (type, number, begin, end)
            VALUES ("{}", "{}", "2005-06-28", {})
        '''.format(type, number, random.choice(['"2013-04-28"', 'NULL'])))
    conn.commit()
    conn.close()


def fill_card():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin, end) VALUES ("Troyka", 365, 0, NULL, 30, "2006-03-04", "2012-03-03")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Troyka", 2000, 0, NULL, 35, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Socialka student", 30, 400, 60, 0, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Yediniy 1", 365, 55, 1, 0, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Yediniy 2", 365, 110, 2, 0, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Socialka pensioner", 30, 0, NULL, 0, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Socialka shkolnik", 30, 300, 60, 0, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Yediniy nedelya", 7, 800, NULL, 0, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Socialka mnogodetniy", 365, 0, NULL, 0, "2012-03-04")''')
    cur.execute('''INSERT INTO Card (name, period, payment, max_number, cost, begin) VALUES ("Rebenok", 365, 0, NULL, 0, "2012-03-04")''')
    conn.commit()
    conn.close()


def fill_concrete_card():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    card_types = cur.execute('''
        SELECT id_card, cost
        FROM Card
    ''').fetchall()
    for i in range(100):
        type = random.choice(card_types)
        account = 0
        if type[1] != 0:
            account = random.randint(0, 1000)
        cur.execute('''
            INSERT OR IGNORE INTO Concrete_Card (card_type, account, begin)
            VALUES ({}, {}, "2018-04-28")
        '''.format(str(type[0]), str(account)))
    conn.commit()
    conn.close()


def fill_trip():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    routes = cur.execute('''
        SELECT id_route
        FROM Route
    ''').fetchall()[:10]
    cards = cur.execute('''
        SELECT id_card
        FROM Concrete_Card
    ''').fetchall()[:10]
    for i in range(1000):
        route = random.choice(routes)[0]
        card = random.choice(cards)[0]
        moment = "2018-05-" + str(10 + random.randint(0, 9)) + " " + str(random.randint(10, 13)) + ":" + str(random.randint(10, 59))
        cur.execute('''
            INSERT OR IGNORE INTO Trip (card, route, moment)
            VALUES ({}, {}, "{}")
        '''.format(str(card), str(route), moment))
    conn.commit()
    conn.close()


def fill_station():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Timiryazevskaya", 0, 1)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Timiryazevskaya", 2, 3)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Timiryazevskaya", 4, 5)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Sadoviy", 6, 7)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Sadoviy", 8, 9)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Vokzal", 10, 11)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Leninskii prospekt", 12, 13)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Leninskii prospekt", 14, 15)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Tverskaya", 16, 17)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Tverskaya", 18, 19)''')
    cur.execute('''INSERT OR IGNORE INTO Station (name, coordinate_x, coordinate_y) VALUES ("Ostankino", 20, 21)''')
    conn.commit()
    conn.close()


def fill_route_station():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Route_Station (route, direction, next_station) VALUES (2, 0, 4)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (2, 0, 4, 1)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (2, 0, 1, 7)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (2, 0, 7, 6)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station) VALUES (2, 0, 6)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, next_station) VALUES (2, 1, 6)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (2, 1, 6, 8)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (2, 1, 8, 2)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (2, 1, 2, 5)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station) VALUES (2, 1, 5)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, next_station) VALUES (3, 0, 4)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (3, 0, 4, 10)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (3, 0, 10, 11)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (3, 0, 11, 6)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station) VALUES (3, 0, 6)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, next_station) VALUES (3, 1, 6)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (3, 1, 6, 9)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station, next_station) VALUES (3, 1, 9, 5)''')
    cur.execute('''INSERT INTO Route_Station (route, direction, station) VALUES (3, 1, 5)''')
    conn.commit()
    conn.close()


def fill_route_shift():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Route_Shift (begin, end) VALUES ("05:00", "08:00")''')
    cur.execute('''INSERT INTO Route_Shift (begin, end) VALUES ("08:00", "11:00")''')
    cur.execute('''INSERT INTO Route_Shift (begin, end) VALUES ("11:00", "14:00")''')
    cur.execute('''INSERT INTO Route_Shift (begin, end) VALUES ("14:00", "17:00")''')
    cur.execute('''INSERT INTO Route_Shift (begin, end) VALUES ("17:00", "20:00")''')
    cur.execute('''INSERT INTO Route_Shift (begin, end) VALUES ("20:00", "01:00")''')
    conn.commit()
    conn.close()


def fill_route_schedule():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    routes = cur.execute('''
        SELECT id_route
        FROM Route
    ''').fetchall()
    shifts = cur.execute('''
        SELECT id_shift
        FROM Route_Shift
    ''').fetchall()
    for item1 in routes:
        route = item1[0]
        for item in shifts:
            shift = item[0]
            days = 'weekdays'
            interval = '00:' + str(random.randint(3, 20)).rjust(2, "0")
            begin = "2015-08-23"
            cur.execute('''
                INSERT OR IGNORE INTO Route_Schedule (route, days, shift, interval, begin)
                VALUES ({}, "{}", {}, "{}", "{}")
            '''.format(str(route), days, str(shift), interval, begin))
            days = 'weekend'
            interval = '00:0' + str(random.randint(0, 9))
            begin = "2015-08-23"
            cur.execute('''
                INSERT OR IGNORE INTO Route_Schedule (route, days, shift, interval, begin)
                VALUES ({}, "{}", {}, "{}", "{}")
            '''.format(str(route), days, str(shift), interval, begin))
    conn.commit()
    conn.close()


def fill_model():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    producers = ['Mercedes-Benz', 'MAN', 'IVECO', 'Ikarbus', 'UAZ']
    f = open("Виды транспорта.txt", 'r')
    transport = []
    for line in f:
        transport.append(line.strip())
    f.close()
    for i in range(100):
        producer = random.choice(producers)
        model = str(random.randint(100, 999) * 10)
        type = random.choice(transport)
        seat = random.randint(35, 50)
        capacity = seat*2 + random.randint(0, 10)
        cur.execute('''
            INSERT OR IGNORE INTO Model (producer, model, type, seat, capacity)
            VALUES ("{}", "{}", "{}", {}, {})
        '''.format(producer, model, type, str(seat), str(capacity)))
    conn.commit()
    conn.close()


def fill_vehicle():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    models = cur.execute('''
        SELECT id_model
        FROM Model
    ''').fetchall()
    letters = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X']
    for i in range (100):
        model = random.choice(models)[0]
        date = random.randint(1960, 2017)
        number = random.choice(letters) + random.choice(letters) + \
                 str(random.randint(0, 999)) + random.choice(letters) + \
                 " " + str(random.randint(0, 99))
        begin = str(random.randint(1950, 2017)) + "-" + str(random.randint(1, 12)).rjust(2, "0") + "-" + str(random.randint(1, 28)).rjust(2, "0")
        cur.execute('''
            INSERT OR IGNORE INTO Vehicle (model, date_manufacture, number, begin)
            VALUES ({}, {}, "{}", "{}")
        '''.format(str(model), str(date), number, begin))
    conn.commit()
    conn.close()


def fill_driver():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    f = open("Фамилии.txt", 'r')
    surnames = []
    for line in f:
        surnames.append(line.strip())
    f.close()
    f = open("Имена.txt", 'r')
    names = []
    for line in f:
        names.append(line.strip())
    f.close()
    f = open("Виды транспорта.txt", 'r')
    transport = []
    for line in f:
        transport.append(line.strip())
    f.close()
    for i in range(100):
        name = random.choice(names) + ' ' + random.choice(surnames)
        type = random.choice(transport)
        experience = random.randint(0, 40)
        year = random.randint(1950, 1990)
        birthday = str(year) + "-" + str(random.randint(1, 12)).rjust(2, "0") + "-" + str(
            random.randint(1, 28)).rjust(2, "0")
        begin = str(random.randint(year + 20, 2017)) + "-" + str(random.randint(1, 12)).rjust(2, "0") + "-" + str(
            random.randint(1, 28)).rjust(2, "0")
        cur.execute('''
        INSERT OR IGNORE INTO Driver (name, type, experience, birthday, begin)
        VALUES ("{}", "{}", "{}", "{}", "{}")
        '''.format(name, type, experience, birthday, begin))
    conn.commit()
    conn.close()


def fill_driver_shift():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO Driver_Shift (begin, end) VALUES ("00:00", "06:00")''')
    cur.execute('''INSERT OR IGNORE INTO Driver_Shift (begin, end) VALUES ("06:00", "12:00")''')
    cur.execute('''INSERT OR IGNORE INTO Driver_Shift (begin, end) VALUES ("12:00", "18:00")''')
    cur.execute('''INSERT OR IGNORE INTO Driver_Shift (begin, end) VALUES ("18:00", "00:00")''')
    conn.commit()
    conn.close()


def fill_driver_schedule():
    conn = sqlite3.connect('Transport.db')
    cur = conn.cursor()
    routes = cur.execute('''
        SELECT id_route, type
        FROM Route
    ''').fetchall()
    shifts = cur.execute('''
        SELECT id_shift
        FROM Driver_Shift
    ''').fetchall()
    for i in range(1000):
        route = random.choice(routes)
        vehicles = cur.execute('''
            SELECT id_vehicle
            FROM Vehicle
            JOIN Model
            ON Vehicle.model = id_model
            WHERE type = "{}"
        '''.format(route[1])).fetchall()
        drivers = cur.execute('''
            SELECT id_driver
            FROM Driver
            WHERE type = "{}"
        '''.format(route[1])).fetchall()
        vehicle = random.choice(vehicles)[0]
        driver = random.choice(drivers)[0]
        shift = random.choice(shifts)[0]
        day = "2018-" + str(random.randint(4, 6)).rjust(2, "0") + "-" + str(
            random.randint(1, 30)).rjust(2, "0")
        cur.execute('''
            INSERT OR IGNORE INTO Driver_Schedule (day, shift, driver, vehicle, route)
            VALUES ("{}", {}, {}, {}, {})
        '''.format(day, shift, driver, vehicle, route[0]))
    conn.commit()
    conn.close()
