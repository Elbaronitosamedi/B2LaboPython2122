from flask import Flask,render_template,request,session,redirect
import sqlite3 
 
app = Flask(__name__)
app.config['SECRET_KEY'] = "Yes"
 
	
@app.route('/', methods=['GET','POST'])		
def index():
    conn = sqlite3.connect('pokedex.db')
    conn.row_factory = sqlite3.Row
    pokemons = conn.execute('SELECT * FROM pokemon').fetchall()
    captured = conn.execute("select poke_id FROM pokedex where user_id = ?",str(session['id'])).fetchall()
            
    if  request.method == 'POST':
        if "add" in request.form : 
            poke_id = request.form.get("poke_id","test") 
            conn.execute("""insert if not exist into pokedex(
            user_id, poke_id)
            values (?, ?)""",(session['id'], poke_id))
            print("add", poke_id ,"from" , session['id'])
            conn.commit()
        elif "remove" in request.form : 
            poke_id = request.form.get("poke_id","test") 
            conn.execute("""delete from pokedex where
            user_id = ? and poke_id = ?""",(session['id'], poke_id))
            conn.commit()
            print("remove" , poke_id)
    return render_template('index.html', data=pokemons, captured = captured)




 
@app.route('/login', methods=['GET','POST'])
def login():
    conn = sqlite3.connect('pokedex.db')
    cursor = conn.cursor()
    if  request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        data = conn.execute("""select id from users where name = 
            ? and password = ?""",(username, password))
        id = None
        for datas in data :
            id = datas
        if id is not None :
            session['user'] = username
            session['id'] = id[0]
            print(session['id'])
            return redirect('/')
        else :
            print("bad password")
    return render_template('login.html')




	
@app.route('/register', methods=['GET','POST'])
def register():
    conn = sqlite3.connect('pokedex.db')
    cursor = conn.cursor()
    if  request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        conn.execute("""insert into users(
            name, password)
            values (?, ?)""",(username, password))
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('register.html')
    
if __name__ == "__main__":
    app.run(debug=True)