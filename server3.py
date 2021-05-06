# pip install flask (if not installed in directory)
# py -3 -m venv venv
# venv\Scripts\activate

# set FLASK_APP=server3.py
# set FLASK_ENV=development
# python -m flask run


from flask import Flask, render_template, url_for, send_from_directory, request, redirect
from jinja2 import Template
import csv


app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='', encoding='utf8') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'somethong went wrong!'
    
# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/components.html')
# def about1():
#     return render_template('components.html')

# @app.route('/contact.html')
# def about2():
#     return render_template('contact.html')

# @app.route('/work.html')
# def about3():
#     return render_template('work.html')

# @app.route('/works.html')
# def about4():
#     return render_template('works.html')

# if __name__ == '__main__':
#     app.run(debug=True)


