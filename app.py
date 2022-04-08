from typing import Any, Union

from flask import Flask, render_template, request, redirect, url_for, logging
from flask_wtf import FlaskForm
from werkzeug import Response
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, URL

from api_service import ApiService
from logger import config


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
def search() -> Union[Response, str]:
    api_service = ApiService(request.form.get('url'))
    return render_template("detail.html", data=api_service.search())


@app.route('/', methods=['GET', 'POST'])
def home() -> Union[Response, str]:
    form = SearchForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('search'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
