from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from .forms import UpdateProfile
from flask_login import login_required
from .. import db,photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title )
@main.route('/comic')
@login_required
def comic():
  
    return render_template('comic.html')

@main.route('/motivation')
@login_required
def motivation():
  
    return render_template('motivation.html')

@main.route('/novels')
@login_required
def novels():
  
    return render_template('novels.html')

@main.route('/spiritual')
@login_required
def spiritual():
  
    return render_template('spiritual.html')

@main.route('/fashionentertainment')
@login_required
def fashionentertainment():
  
    return render_template('fashionentertainment.html')


@main.route('/health')
@login_required
def health():
    
    return render_template('health.html')

@main.route('/aboutus')
@login_required
def aboutus():

    '''
    View root page function that returns the about us page and its data
    '''

    title = 'About US'

    return render_template('aboutus.html', title = title )


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.preferences = form.preferences.data
        user.location = form.location.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))