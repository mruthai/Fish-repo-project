from . import bp as social_bp
from app.blueprints.social.models import User, Livestock
from app.forms import LivestockForm, SearchForm
from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
import requests

user_search= []
#route for social login
@social_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    nett = user_match.collections
    return render_template('user.jinja', user=user_match, nett=nett, title='Profile')  

#route for collecting animals
@social_bp.route('/collectanimals', methods=['GET', 'POST'])
@login_required
def collectanimals():
    form = SearchForm()
    search= form.search.data
    if form.validate_on_submit():
        user_search.clear()
        col = requests.get(f'https://www.fishwatch.gov/api/species/{search}')
        data = col.json()
        user_search.append(data[0]['Species Name'])
        return render_template('collectanimals.jinja',form=form, data=data, title='Collect Animals')
    print(user_search)
    return render_template('collectanimals.jinja', form=form, title='Collect Animals')

@social_bp.route('/species', methods=['GET', 'POST'])
def collected():
    # print('working??')
    form = SearchForm()
    species= user_search[0]
    colcard = Livestock(species=species, user_id=current_user.id)
    colcard.commit()
    # print('again?')
    return render_template('collectanimals.jinja', form=form, title='Collect Animals')

@social_bp.route('/species/<species>,<username>', methods=['GET', 'POST'])
def seefish(species,username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    nett = user_match.collections
    # print(nett)
    col = requests.get(f'https://www.fishwatch.gov/api/species/{species}')
    data = col.json()
    return render_template('user.jinja', data=data, user=user_match, nett=nett, title='Profile')



@social_bp.route('/livestock', methods=['GET', 'POST'])
@login_required
def livestock():
    form = LivestockForm()
    if form.validate_on_submit():
        classifications = form.classifications.data
        species = form.species.data
        breed = form.breed.data
        l = Livestock(classifications=classifications, species=species, breed=breed)
        l.commit()
        flash('Your livestock has been added!')
        return redirect(url_for('social.user', username=current_user.username))
    return render_template('livestock.jinja', form=form, title='Livestock') 

