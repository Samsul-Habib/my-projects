import bottle
import mysql.connector

import socket    #this module searches the local IP address of machine
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# connect() for UDP doesn't send packets
s.connect(('10.0.0.0', 0))
bbb=s.getsockname()[0]

# Database connection parameters
database_config = {
    'host': 'localhost',        # usually 'localhost'
    'user': 'root',
    'password': 'qlc#tbb',
    'database': 'mess_data'
}

# Connect to the database
try:
    connection = mysql.connector.connect(**database_config)
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

app = bottle.Bottle()
cursor = connection.cursor()

@app.route('/')
def index():
    return bottle.template('index')

@app.route('/submit', method='POST')
def submit():
    month = bottle.request.forms.get('month')
    boarder_name = bottle.request.forms.get('boarder_name')
    room_rent = bottle.request.forms.get('room_rent')
    electric_bill = bottle.request.forms.get('electric_bill')

    # Prepare and execute the SQL statement
    insert_statement = f"update {month} set room_rent={room_rent},Electricity_bill={electric_bill} where Name='{boarder_name}'"

    try:
        cursor.execute(insert_statement)
        connection.commit()
        return "Data inserted successfully."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
        return f"Error: {err}"

if __name__ == '__main__':
    bottle.run(app, host=bbb, port=8080)
