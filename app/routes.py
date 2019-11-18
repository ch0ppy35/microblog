from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mike'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Denver!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Mr. Robot is so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
