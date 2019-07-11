from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm, OrderForm
from ..models import Review




# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title )

@main.route('/fashionentertainment')
def fashionentertainment():
  
    return render_template('fashionentertainment.html')


@main.route('/health')
def health():
    
    return render_template('health.html')



    
   
    
    


