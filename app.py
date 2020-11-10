from flask import Flask, request, Response
import mariadb
import json
import dbcreds

animalslist = ["dog", "cat", "lion", "snake"]

app = Flask(__name__)


@app.route("/animals", methods=["GET", "POST", "PATCH", "DELETE"])
def animals():
    if request.method == "GET":
        return Response(json.dumps(animalslist, default=str), mimetype="application/json", status=200)

        # conn = None
        # cursor = None
        # try:
        #     conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
        #                            host=dbcreds.host, database=dbcreds.database, port=dbcreds.port)
        #     cursor = conn.cursor()
        #     cursor.execute("SELECT * FROM animals_list")
        #     animals_list = cursor.fetchall()
        #     if(cursor.rowcount == 1):
        #         for animal in animals_list:
        #             print(animal[1])
        #     elif(cursor.rowcount == 0):
        #         print("the array is empty")
        #     else:
        #         print("u have to check this please")

        # except mariadb.ProgrammingError:
        #     print("you need lesson")
        # except mariadb.OperationalError:
        #     print("there's a connection error")
        # # except:
        #     #print("this is lazy")
        # finally:
        #     if(cursor != None):
        #         cursor.close()
        #     if(conn != None):
        #         conn.rollback()
        #         conn.close()
        # return Response(json.dumps(animals_list, default=str), mimetype="application/json", status=200)

    elif request.method == "POST":
        # conn = None
        # cursor = None
        # try:
        #     conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
        #                            host=dbcreds.host, database=dbcreds.database, port=dbcreds.port)
        #     cursor = conn.cursor()

        #     cursor.execute(
        #         "INSERT INTO animals_list(id,name) VALUES (NULL,?)", [name])
        #     conn.commit()

        # except mariadb.ProgrammingError:
        #     print("you need lesson")
        # except mariadb.OperationalError:
        #     print("there's a connection error")
        # # except:
        #     #print("this is lazy")
        # finally:
        #     if(cursor != None):
        #         cursor.close()
        #     if(conn != None):
        #         conn.rollback()
        #         conn.close()
        animalslist.append("monkey")

        return Response("monkey  has been added", mimetype="text/html", status=200)
    elif request.method == "PATCH":
        animalslist.remove("dog")
        animalslist.append("bulldog")
        return Response("dog has changed to bulldog", mimetype="text/html", status=200)
    elif request.method == "DELETE":
        # conn = None
        # cursor = None
        # try:
        #     conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
        #                            host=dbcreds.host, database=dbcreds.database, port=dbcreds.port)
        #     cursor = conn.cursor()
        #     cursor.execute(
        #         "DELETE FROM animals_list WHERE name=?",[name])
        #     conn.commit()
        #     if(cursor.rowcount == 1):
        #         print("animal DELETED successful")
        #     elif(cursor.rowcount == 0):
        #         print("no matching animal")

        # except mariadb.ProgrammingError:
        #     print("you need lesson")
        # except mariadb.OperationalError:
        #     print("there's a connection error")
        # # except:
        #     #print("this is lazy")
        # finally:
        #     if(cursor != None):
        #         cursor.close()
        #     if(conn != None):
        #         conn.rollback()
        #         conn.close()
        animalslist.remove("lion")

    return Response("lion has been deleted", mimetype="text/html", status=200)
