from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "groot"
app.config["MYSQL_DB"] = "company"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/employee", methods=["GET"])
def get_actors():
    data = data_fetch("""select * from employee""")
    return make_response(jsonify(data), 200)


@app.route("/employee/<int:id>", methods=["GET"])
def get_actor_by_id(id):
    data = data_fetch("""SELECT * FROM actor where actor_id = {}""".format(id))
    return make_response(jsonify(data), 200)


@app.route("/actors/<int:id>/movies", methods=["GET"])
def get_movies_by_actor(id):
    data = data_fetch(
        """
        SELECT film.title, film.release_year 
        FROM actor 
        INNER JOIN film_actor
        ON actor.actor_id = film_actor.actor_id 
        INNER JOIN film
        ON film_actor.film_id = film.film_id 
        WHERE actor.actor_id = {}
    """.format(
            id
        )
    )
    return make_response(
        jsonify({"actor_id": id, "count": len(data), "movies": data}), 200
    )


@app.route("/employee", methods=["POST"])
def add_actor():
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["Fname"]
    minit_name = info["Minit"]
    last_name = info["Lname"]
    bdate = info["Bdate"]
    address = info["Address"]
    sex = info["Sex"]
    salary = info["Salary"]
    super_ssn = info["Super_ssn"]
    dl_id = info["DL_id"]
    cur.execute(
        """ INSERT INTO employee (Fname, Minit,Lname,Bdate,Address,Sex,Salary,Super_ssn,DL_id) VALUE (%s, %s,%s,%s,%s,%s,%s,%s,%s)""",
        (first_name, last_name,minit_name,bdate,address,sex,salary,super_ssn,dl_id),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor added successfully", "rows_affected": rows_affected}
        ),
        201,
    )

@app.route("/employee/<int:ssn>", methods=["PUT"])
def update_employee(ssn):
    cur = mysql.connection.cursor()
    info = request.get_json()

    first_name = info.get("Fname")
    minit_name = info.get("Minit")
    last_name = info.get("Lname")
    dl_id = info.get("DL_id")
    fields = []
    values = []

    if first_name:
        fields.append("Fname = %s")
        values.append(first_name)
    if minit_name:
        fields.append("Minit = %s")
        values.append(minit_name)
    if last_name:
        fields.append("Lname = %s")
        values.append(last_name)
    if dl_id:
        fields.append("DL_id = %s")
        values.append(dl_id)

    if not fields:
        return make_response(
            jsonify({"message": "No fields provided to update"}),
            400,
        )
    values.append(ssn)
    update_statement = f"UPDATE employee SET {', '.join(fields)} WHERE SSN = %s"
    
    try:
        cur.execute(update_statement, tuple(values))
        mysql.connection.commit()
        rows_affected = cur.rowcount
    except Exception as e:
        return make_response(
            jsonify({"message": "Error updating employee", "error": str(e)}),
            500,
        )
    finally:
        cur.close()

    if rows_affected == 0:
        return make_response(
            jsonify({"message": "No employee found with the provided SSN"}),
            404,
        )

    return make_response(
        jsonify({"message": "Employee updated successfully", "rows_affected": rows_affected}),
        200,
    )



@app.route("/employee/<int:ssn>", methods=["DELETE"])
def delete_actor(ssn):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM actor where actor_id = %s """, (ssn,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )

@app.route("/employee/format", methods=["GET"])
def get_params():
    fmt = request.args.get('id')
    foo = request.args.get('aaaa')
    return make_response(jsonify({"format":fmt, "foo":foo}),200)

if __name__ == "__main__":
    app.run(debug=True)