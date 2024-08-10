import csv
from flask import Flask, request, redirect, render_template
app = Flask(__name__)
print(__name__)

#@app.route('/<username>/<int:post_id>')
#def home_func(username=None, post_id=None):
#	return render_template('index.html', name=username, post_id=post_id	)


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/')
def home_func():
	return render_template('index.html')

def write_to_file(data):
	with open('db.txt', mode='a') as database:
		email = data["email"]
		name = data["name"]
		message = data["message"]
		file = database.write(f'\n{email},{name},{message}')

def write_to_csv(data):
	with open('db.csv', mode='a', newline='') as db:
		email = data["email"]
		name = data["name"]
		message = data["message"]
		csv_writer = csv.writer(db, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,name,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return data
		except:
			return 'did not save to database'
	else:
		return 'something went wrong...'

#redirect('/thankyou.html')

#@app.route('/favicon.ico')
#def favicon():
#	return render_template('about.html')
