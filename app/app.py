__author__ = 'phrayezzen'

import sqlite3 as lite
"""
sqlite3 differences
con just connects to database with same thread option off
change con row factory (not built in mdb.cursors.DictCursor)
replace all %s with ?
"""

con = lite.connect("test.db", check_same_thread=False)
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

con.row_factory = make_dicts
cur = con.cursor()

def get_contacts():
    with con:
        cur.execute("""SELECT * FROM contact""")
        rows = {"result": cur.fetchall()}
        return rows

def add_contact(f):
    with con:
        cur.execute("""INSERT INTO contact (firstName, lastName, phone, address, city, state, zip)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (f['first'], f['last'], f['phone'], f['address'], f['city'], f['state'], f['zip']))
        con.commit()
        cur.execute("""SELECT * FROM contact WHERE contactId = ?""", (str(cur.lastrowid),))
        contact = {"result": [cur.fetchone()]}
        return contact

def delete_contact(contact_id):
    with con:
        cur.execute("""DELETE FROM contact WHERE contactId = ?""", (str(contact_id),))

# add_contact({
#     'first':'Xilin',
#     'last':'Liu',
#     'phone':'9107280992',
#     'address':'1601 Rice Boulevard',
#     'city':'Houston',
#     'state':'TX',
#     'zip':'77005'
#     })

# print get_contacts()

# delete_contact(NUMBER)