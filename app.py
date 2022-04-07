from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import validators, SearchField, SubmitField


class SearchForm(FlaskForm):
    name = SearchField('field', [validators.Length(min=4, max=25)])
    submit = SubmitField('Search')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


@app.route('/search', methods=['POST'])
def search():
    return render_template("detail.html")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('search'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
