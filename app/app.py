__author__ = 'phrayezzen'

from flask import Flask, request, jsonify
import sqlite3 as lite
"""
sqlite3 differences
con just connects to database with same thread option off
change con row factory (not built in mdb.cursors.DictCursor)
replace all %s with ?
"""

app = Flask(__name__)
con = lite.connect("test.db", check_same_thread=False)
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))
con.row_factory = make_dicts
cur = con.cursor()

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/getContacts")
def get_contacts():
    with con:
        cur.execute("""SELECT * FROM contact""")
        rows = {"result": cur.fetchall()}
        return jsonify(rows)
    return jsonify({})

@app.route("/addContact", methods = ["POST"])
def add_contact():
    f = request.form
    with con:
        cur.execute("""INSERT INTO contact (firstName, lastName, phone, address, city, state, zip)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (f['first'], f['last'], f['phone'], f['address'], f['city'], f['state'], f['zip']))
        con.commit()
        cur.execute("""SELECT * FROM contact WHERE contactId = ?""", (str(cur.lastrowid),))
        contact = {"result": [cur.fetchone()]}
        return jsonify(contact)
    return jsonify({})

@app.route("/deleteContact/<int:contact_id>")
def delete_contact(contact_id):
    with con:
        cur.execute("""DELETE FROM contact WHERE contactId = ?""", (str(contact_id),))
    return "deleted " + str(contact_id)

if __name__ == "__main__":
    app.run(debug=True)