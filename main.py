from unittest import result
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instantiate database 
db = SQLAlchemy(app)

#define db table
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(20))
    comment =  db.Column(db.String(200))

@app.route('/')
def index():
    results = Comments.query.all()
    return render_template('index.html', results=results)


@app.route('/signin')
def signin():
    return render_template('signin.html')


#add info to database
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


    