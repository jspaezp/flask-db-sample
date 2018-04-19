from flask import jsonify, render_template, request
from db_example import app

# DUMMY database

database = {'Opt1': [1, 2, 3, 4, 5],
            'Opt2': [10, 20, 30, 40]}


@app.context_processor
def inject_database():
    """ Exposes the database file so it can be read in the html templates """
    return dict(database=database)


@app.route('/')
def base():
    """ Exposes the base html after rendering the template """
    return render_template('base.html', database=database)


@app.route('/secondoptions', methods=['POST'])
def secondoptions():
    firstoption = request.form.get('firstoptions')
    return jsonify(options=database[firstoption])
