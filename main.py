from flask import Flask
from flask import request
from sqlalchemy import create_engine
from CreateDB import Base
from sqlalchemy.orm import Session
from CreateDB import Page
from flask import render_template
app = Flask(__name__)


@app.route('/')
def load_html():
    html = open("website.html", 'r').read()
    return str(html)


@app.route('/search/')
def get_result():

    searchword = request.args.get('key_word', '')
    engine = create_engine("sqlite:///storage.db")
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    #all_urls = session.query(Page).all()

    pages = session.query(Page).filter(Page.title.like(
        "%" + searchword + "%")).all()

    return render_template('result.html', pages=pages)

    #return searchword

if __name__ == '__main__':
    app.debug = False
    app.run()
