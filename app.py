from flask import Flask, request
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
# app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

# cors  = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#   return response



@app.route("/signup_member", methods=["POST", "GET"])
def signup_member():
    # obj = request.get_json()
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                sql = "INSERT INTO Members (Email_ID, Password, First_Name, Middle_Name, Last_Name, Zip_Code, City, State_Name, Phone_Number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (obj['Email_ID'], obj['Password'], obj['First_Name'], obj['Middle_Name'], obj['Last_Name'], obj['Zip'], obj['City'], obj['State'], obj['Phone'])
                cursor.execute(sql, val)
                connection.commit()
                
                return "Success account Created", 200
            except Error as e:
                print(e)
                return "Email Exits", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


@app.route("/login_member", methods=["POST", "GET"])
def login_member():
    obj = request.json
    print(obj)
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user = 'root',
                                            password = 'Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                sql = "SELECT * FROM Members WHERE Email_ID = %s AND Password = %s"
                val = (obj['Email_ID'], obj['Password'])
                cursor.execute(sql, val)
                result = cursor.fetchall()
                
                if result:
                    list = []
                    result = result[0]
                    for row in result:
                        list.append(row)
                    return list, 200
                else:
                    return "Invalid Credentials", 400
            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/signup_librarian", methods=["POST", "GET"])
def signup_librarian():
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                sql = "INSERT INTO Librarian (Email_ID, Password, Name, Salary, Phone_Number) VALUES (%s, %s, %s, %s, %s)"
                val = (obj['Email_ID'], obj['Password'], obj['Name'], obj['Salary'], obj['Phone_Number'])
                cursor.execute(sql, val)
                connection.commit()
                
                return "Success", 201
            except Error as e:
                print(e)
                return "Email Exits", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/login_librarian", methods=["POST", "GET"])
def login_librarian():
    obj = request.json
    print(obj)
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                sql = "SELECT * FROM Librarian WHERE Email_ID = %s AND Password = %s"
                val = (obj['Email_ID'], obj['Password'])
                cursor.execute(sql, val)
                result = cursor.fetchall()
                if result:
                    result = result[0]
                    list = []
                    for row in result:
                        list.append(row)
                    return list, 200
                else:
                    return "Invalid Credentials", 400
                
            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/get_document", methods=["POST", "GET"])
def get_document():
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                if(obj['type'] == "Book"):
                    sql = "SELECT * FROM Books WHERE Book_Title LIKE %s OR Author LIKE %s;"
                    val = ('%'+obj['input']+'%', '%'+obj['input']+'%')
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    if result:
                        result = result[0]
                        list = []
                        for row in result:
                            list.append(row)
                        return list, 200
                    else:
                        return "No Books", 400
                elif(obj['type'] == "Magazines"):
                    sql = "SELECT * FROM Magazines WHERE Mgz_Title LIKE %s OR Publisher LIKE %s;"
                    val = ('%'+obj['input']+'%', '%'+obj['input']+'%')
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    if result:
                        result = result[0]
                        list = []
                        for row in result:
                            list.append(row)
                        return list, 200
                    else:
                        return "No Magazines", 400
                elif(obj['type'] == "Journal_Articles"):
                    sql = "SELECT * FROM Journal_Articles WHERE Jrnl_Title LIKE %s OR Author LIKE %s;"
                    val = ('%'+obj['input']+'%', '%'+obj['input']+'%')
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    if result:
                        result = result[0]
                        list = []
                        for row in result:
                            list.append(row)
                        return list, 200
                    else:
                        return "No Journals", 400
                else:
                    sql = "SELECT * FROM Books WHERE Book_Title LIKE %s OR Author LIKE %s;"
                    val = ('%'+obj['input']+'%', '%'+obj['input']+'%')
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    list = []
                    if result:
                        result = result[0]
                        for row in result:
                            list.append(row)
                    sql = "SELECT * FROM Magazines WHERE Mgz_Title LIKE %s OR Publisher LIKE %s;"
                    val = ('%'+obj['input']+'%', '%'+obj['input']+'%')
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    if result:
                        result = result[0]
                        for row in result:
                            list.append(row)
                    sql = "SELECT * FROM Journal_Articles WHERE Jrnl_Title LIKE %s OR Author LIKE %s;"
                    val = ('%'+obj['input']+'%', '%'+obj['input']+'%')
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    if result:
                        result = result[0]
                        for row in result:
                            list.append(row)
                    if list:
                        return list, 200
                    else:
                        return "No Documents", 400

            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/document_lending", methods=["POST", "GET"])
def document_lending():
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                if(obj['type']=="book"):
                    sql = "SELECT Num_Copies FROM Books WHERE Book_ID = %s;"
                    val = (obj['id'],)
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    result = result[0][0]
                    if(obj['borrow_or_return']=="borrow"):
                        result = result - 1
                        sql = "UPDATE Books SET Num_Copies = %s WHERE Book_ID = %s;"
                        val = (result, obj['id'])
                        cursor.execute(sql, val)
                        connection.commit()
                    else:
                        result = result + 1
                        sql = "UPDATE Books SET Num_Copies = %s WHERE Book_ID = %s;"
                        val = (result, obj['id'])
                        cursor.execute(sql, val)
                        connection.commit()
                elif(obj['type']=="Magazine"):
                    sql = "SELECT Num_Copies FROM Magazines WHERE Mgz_ID = %s;"
                    val = (obj['Mgz_ID'],)
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    result = result[0][0]
                    if(obj['borrow_or_return']=="borrow"):
                        result = result - 1
                        sql = "UPDATE Magazines SET Num_Copies = %s WHERE Mgz_ID = %s;"
                        val = (result, obj['Mgz_ID'])
                        cursor.execute(sql, val)
                        connection.commit()
                    else:
                        result = result + 1
                        sql = "UPDATE Magazines SET Num_Copies = %s WHERE Mgz_ID = %s;"
                        val = (result, obj['Mgz_ID'])
                        cursor.execute(sql, val)
                        connection.commit()
                else:
                    sql = "SELECT Num_Copies FROM Journal_Articles WHERE Jrnl_ID = %s;"
                    val = (obj['Jrnl_ID'],)
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    result = result[0][0]
                    if(obj['borrow_or_return']=="borrow"):
                        result = result - 1
                        sql = "UPDATE Journal_Articles SET Num_Copies = %s WHERE Jrnl_ID = %s;"
                        val = (result, obj['Jrnl_ID'])
                        cursor.execute(sql, val)
                        connection.commit()
                    else:
                        result = result + 1
                        sql = "UPDATE Journal_Articles SET Num_Copies = %s WHERE Jrnl_ID = %s;"
                        val = (result, obj['Jrnl_ID'])
                        cursor.execute(sql, val)
                        connection.commit()
                
                return "Success", 201
            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/borrow_history", methods=["POST", "GET"])
def borrow_history():
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                sql = "SELECT * FROM Borrows WHERE User_ID = %s and current_status = 'borrowed';"
                val = (obj['User_ID'],)
                cursor.execute(sql, val)
                result = cursor.fetchall()
                if result:
                    result = result[0]
                    list = []
                    for row in result:
                        list.append(row)
                    return list, 200
                else:
                    return "No History", 400
            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/return_document", methods=["POST", "GET"])
def return_document():
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                sql = "UPDATE Borrows SET current_status = 'returned' WHERE Borrow_ID = %s;"
                val = (obj['Borrow_ID'],)
                cursor.execute(sql, val)
                connection.commit()
                return "Success", 201
            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/add_document", methods=["POST", "GET"])
def add_document():
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                if(obj['type']=="Book"):
                    sql = "INSERT INTO Books ( Book_Title, Edition, Author, Publisher, Year_Published, Section, Num_Copies) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                    val = (obj['Book_Title'], obj['Edition'], obj['Author'], obj['Publisher'], obj['Year_Published'], obj['Section'], obj['Num_Copies'])
                    cursor.execute(sql, val)
                    connection.commit()
                elif(obj['type']=="Magazine"):
                    sql = "INSERT INTO Magazines (Mgz_Title, Category, Section, Publisher, Num_Copies) VALUES (%s, %s, %s, %s, %s);"
                    val = (obj['Mgz_Title'], obj['Category'], obj['Section'], obj['Publisher'], obj['Num_Copies'])
                    cursor.execute(sql, val)
                    connection.commit()
                else:
                    sql = "INSERT INTO Journal_Articles (Jrnl_Title, Year_Published, Section, Author, Num_Copies) VALUES (%s, %s, %s, %s);"
                    val = (obj['Jrnl_Title'], obj['Year_Published'], obj['Section'], obj['Author'], obj['Num_Copies'])
                    cursor.execute(sql, val)
                    connection.commit()
                return "Success", 201
            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@app.route("/delete_document", methods=["POST", "GET"])
def delete_document():
    obj = request.json
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='harsha_db',
                                            user='root',
                                            password='Chinnu@13')
        if connection.is_connected():
            cursor = connection.cursor()
            try:
                if(obj['type']=="Book"):
                    sql = "DELETE FROM Books WHERE Book_ID = %s;"
                    val = (obj['Book_ID'],)
                    cursor.execute(sql, val)
                    connection.commit()
                elif(obj['type']=="Magazine"):
                    sql = "DELETE FROM Magazines WHERE Mgz_ID = %s;"
                    val = (obj['Mgz_ID'],)
                    cursor.execute(sql, val)
                    connection.commit()
                else:
                    sql = "DELETE FROM Journal_Articles WHERE Jrnl_ID = %s;"
                    val = (obj['Jrnl_ID'],)
                    cursor.execute(sql, val)
                    connection.commit()
                return "Success", 201
            except Error as e:
                print(e)
                return "Error", 400
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
