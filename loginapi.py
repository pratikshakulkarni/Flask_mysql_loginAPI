from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		userDetails = request.form
		name = userDetails['uname']
		pass1 = userDetails['upass']
		cur = mysql.connection.cursor()
		res = cur.execute("select * from users")
		userDetails = cur.fetchall()
		for u in userDetails:
			cu = u[0];
			cp = u[1];
			if name == cu:
				if pass1 == cp:
					return '<h1>success</h1>'
				else :
					return '<h1>pass is wrong</h1>'
			else:
				return '<h1>user not found</h1>'
		cur.close()
	return render_template('index.html')

app.run(debug=True);