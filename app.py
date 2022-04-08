from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, URL

from api_service import ApiService


class SearchForm(FlaskForm):
    url = URLField('field', validators=[DataRequired(), URL("Enter valid URL")])
    submit = SubmitField('Search')


app = Flask(__name__)
app.config.from_object('default_settings')


@app.route('/search', methods=['POST'])
def search():
    api_service = ApiService(request.form.get('url'))
    return render_template("detail.html", data=api_service.search())


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('search'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
