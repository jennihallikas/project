import mysql.connector

connection = mysql.connector.connect(
         host='mysql.metropolia.fi',
         port= 3306,
         database='jenniheh',
         user='jenniheh',
         password='1234',
         autocommit=True
)

print("THIS IS A FLIGHT GAME ")
print("HERE ARE THE RULES:")
print("1. YOU WILL HAVE TO CHOOSE A DESTINATION WHERE YOU WANT TO GO")
print("2. YOU WILL BE GIVEN OPTIONS OF THE CONNECTING AIRPORTS TO YOUR DESTINATION")
print("3. THERE IS A LIMITED TIME SET FOR YOU TO REACH THE DESTINATION ")
print("4. YOUR GOAL IS TO CHOOSE CORRECT CONNECTING AIRPORT AND REACH THE DESTINATION WITHIN THE TIME LIMIT")
print("5. IF YOU REACH WITHIN THE TIME LIMIT THAT IS SET, YOU WIN!!!")
print("--------------- LET'S  BEGIN ----------------\n\n")


def dest(airport):
    sql = "SELECT country, airport FROM all_locations"
    sql += " WHERE country='" + airport + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"your final destination is {row[0]} and the airport is {row[1]}")
    return


airport = input("please enter the destination you want to visit: ")
dest(airport)


def connecting():
    countries =[]
    sql = "SELECT country, connecting_airports FROM connections"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            countries.append(row[0])
            countries. append(row[1])
            print(f" {row[1]} in  {row[0]}")
    return countries


print("\n The list of connecting airports are: ")
connecting()






