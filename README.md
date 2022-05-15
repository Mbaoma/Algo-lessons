- Create a virtual environemnt
```bash
$ python3 -m venv venv
```
- Activate the virtual environment
```bash
$ source venv/bin/activate
```

- Install requirements
```bash
$ pip install -r requirements.txt
```

- Put env variables in the .env file
FLASK_APP=main.py
FLASK_ENV=development
DEBUG=True

- Download the [MySQLdb](https://sourceforge.net/projects/mysql-python/postdownload)

- Create a free MySQL [account](https://www.freemysqlhosting.net/). 
You would use the details of your account to fill in the values of lines ```app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'```

- To initiate the database, open up a terminal and run the following:
```bash
$ python
>>> from main import db
>>> db.create_all()
db
<SQLAlchemy engine=mysql://sql11492238:***@sql11.freemysqlhosting.net/sql11492238?charset=utf8>
```

- Get a graphical view on [phpMyadmin](https://www.phpmyadmin.co/)
<img width="1160" alt="image" src="https://user-images.githubusercontent.com/49791498/168457395-10c0f1b5-872e-4ec8-b923-fc7e2e2c5c9e.png">


- Run the application
```bash
$ flask run
```

<img width="1160" alt="image" src="https://user-images.githubusercontent.com/49791498/168457839-b36585d2-95cf-49d1-989d-531391e00213.png">