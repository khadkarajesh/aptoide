import logging.config
from typing import Any, Union

import requests
import werkzeug.wrappers.response
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, URL

from logger import config
from parser import parse


def create_app() -> Any:
    flask_app = Flask(__name__)
    flask_app.config.from_object('default_settings')
    return flask_app


logging.config.dictConfig(config)
app = create_app()


class SearchForm(FlaskForm):
    url = URLField('field', validators=[DataRequired(), URL("Enter valid URL")])
    submit = SubmitField('Search')


@app.route('/search', methods=['POST'])
def search() -> str:
    url: Any = request.form.get('url')
    response: requests.Response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return render_template("detail.html", data=parse(soup=soup))


@app.route('/', methods=['GET', 'POST'])
def home() -> Union[str, werkzeug.wrappers.response.Response]:
    form = SearchForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('search'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
