from . import bp as main_bp

from flask import render_template

@main_bp.route('/')
def index():
    pen={
        'animals':['Snapper','Groupers', 'Sharks', 'Tiger fish', ' Rock fish', 'Cat fish', 'Sting Ray']
    }
    return render_template('index.jinja', pen=pen, title='Home')


