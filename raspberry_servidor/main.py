from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/configurar", methods=["POST"])
def hello():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True, port=5000)