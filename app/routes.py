from app import app

from flask import render_template, url_for, redirect

@app.route('/') # This is the main route
def hello_world():
    name = 'Jon Snow'

    characters = {
        'women': ['Arya', 'Daenarys'],
        'men': ['Jaime', 'Jon', 'Ned', 'Robert'],
    }
    return render_template('index.html', name = name, characters = characters)

@app.route('/profile/', methods = ["GET"])
def profile(name, gender):
    info = {}

    if gender == 'men':
        gender = 'man'
    else: 
        gender = 'woman'

    if name == 'Arya':
        info = {
            'profile_pic': 'https://placehold.it/250x250',
            'house': 'Stark',
            'home': 'Winterfell',
            'weapon': 'Needle',
        }
    elif name == 'Jaime':
        info = {
            'profile_pic': 'https://placehold.it/250x250',
            'house': 'Lannister',
            'home': 'Casterly Rock',
            'weapon': 'Sword',
        }

    return render_template('profile.html', name = name, info = info, gender = gender)