from flask import Flask , g , request , jsonify
from database import get_db , connect_db
from functools import wraps #for create an auth method

app = Flask(__name__)

api_username = 'admin'
api_password = 'password'

def protected(f): #f is the function with the decorator applied (ex @protected \ def get_members())
    @wraps(f) #It takes the function and decore it
    def decorated(*args,**kwargs): #*args , **kwargs = arguments of the function 
        auth = request.authorization #it request the credentials inserted for the auth
        if auth and auth.username == api_username and auth.password == api_password:
            return f(*args,**kwargs) #if True return the function with his args
        return "Authentication failed!", 401 #401 is the status code (UNAUTHORIZED)
    return decorated

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()

@app.route('/member', methods=["GET"])
@protected #decorator applied
def get_members():
    db = get_db()

    cur = db.execute("SELECT id,name,email,level FROM members")
    members_data = cur.fetchall()

    member_list = list()

    for i in members_data:
        member = {
            "id" : i['id'],
            "name" : i['name'],
            "email" : i['email'],
            "level" : i['level']
        }
        member_list.append(member)

    return jsonify({ "member list" : member_list})

@app.route("/member/<int:id>", methods=["GET"])
@protected
def get_member(id):
    db = get_db()

    cur = db.execute("SELECT id,name,email,level FROM members WHERE id = ?",[id])
    member_data = cur.fetchone()

    member = {
            "id" : member_data['id'],
            "name" : member_data['name'],
            "email" : member_data['email'],
            "level" : member_data['level']
            }
    return member

@app.route("/member" , methods=["POST"])
@protected
def add_member():
    new_member = request.get_json()
    db = get_db()

    check_cur = db.execute("SELECT id,name,email,level FROM members")
    check_members = check_cur.fetchall()

    name = new_member["name"]
    email = new_member["email"]
    level = new_member["level"]

    for i in check_members:
        if name == i["name"] or email == i["email"]:
            return "An user with that credentials alredy exists!"

    db.execute("INSERT INTO members (name,email,level) VALUES (?,?,?)",[name,email,level])
    db.commit()

    cur = db.execute("SELECT id,name,email,level FROM members WHERE name = ?",[name])
    curr_member = cur.fetchone()

    return jsonify({ 'id' : curr_member['id'] , 'name' : curr_member['name'], 'email' : curr_member['email'], 'level' : curr_member['level']})

@app.route("/member/<int:id>", methods=["PUT","PATCH"])
@protected
def update_member(id):
    db = get_db()

    updated_member_data = request.get_json()

    check_cur = db.execute("SELECT id,name,email,level FROM members")
    check_members = check_cur.fetchall()

    name = updated_member_data["name"]
    email = updated_member_data["email"]
    level = updated_member_data["level"]

    for i in check_members:
        if name == i["name"] or email == i["email"]:
            return "Can't update, an user with that credentials alredy exists!"

    db.execute("UPDATE members SET name = ?, email = ?, level = ? WHERE id = ?",[name,email,level,id])
    db.commit()

    cur = db.execute("SELECT id,name,email,level FROM members WHERE id = ?",[id])
    member_data = cur.fetchone()

    member = {
            "id" : member_data['id'],
            "name" : member_data['name'],
            "email" : member_data['email'],
            "level" : member_data['level']
            }
    
    return jsonify({"Updated_Member": member})

@app.route("/member/<int:id>" , methods=["DELETE"])
@protected
def delete_member(id):
    db = get_db()
    db.execute("DELETE FROM members WHERE id = ?",[id])
    db.commit()

    return "User {} successfully eliminated!".format(id)

if __name__ == '__main__':
    app.run(debug=True)