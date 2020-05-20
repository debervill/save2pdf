import app_config
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(app_config)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		req = request.form
		sendedEmail = req.get("email")
		sendedLink = req.get("link")
		
		
	return render_template('index.html')


if __name__ == "__main__":
	app.jinja_env.auto_reload = True
	app.run(debug=True, host='0.0.0.0')
