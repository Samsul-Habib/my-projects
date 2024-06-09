import mysql.connector

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "qlc#tbb",
    "database": "mess_data",
}
month=input("Which Month?")
name=input("enter name of the boarder:")
room_rent=int(input("enter room rent:"))
e_bill=int(input("enter Electricity_bill:"))
# Establish a connection to the database
connection = mysql.connector.connect(**db_config)

# Create a cursor object
cursor = connection.cursor()

# Example INSERT query
insert_query = f"update {month} set room_rent={room_rent},Electricity_bill={e_bill} where Name='{name}'"

# Example data to be inserted
data_to_insert = ("H",1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200)

# Execute the query with the provided data
#cursor.execute(insert_query, data_to_insert)
cursor.execute(insert_query)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
