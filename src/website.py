from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Character_DB, Server_DB, Group_DB

app = Flask(__name__)

engine = create_engine('sqlite:///db.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/charaters/')
def charaters():
    charaters = session.query(Character_DB).order_by(Character_DB.name)
    return render_template('charaters.html', charaters=charaters)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)