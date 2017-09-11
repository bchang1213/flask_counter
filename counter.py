from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 's3cr37$%328@!$%'

@app.route("/")
def index():
	if "count" in session:
		session['count'] += 1
	else:
		session['count'] = 1
	return	render_template("index.html", count = session["count"])

app.run(debug=True)