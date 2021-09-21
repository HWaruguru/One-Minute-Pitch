from . import main
from flask import render_template

# Views
@main.route('/')
def index():

    pitches = [{'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvotes': 3, 'downvotes': 1, 
    },
    {'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvotes': 3, 'downvotes': 1, 
    },
   {'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvotes': 3, 'downvotes': 1
    },
   {'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvotes': 3, 'downvotes': 1,
    }]


    '''
    View root page function that returns the index page and its data
    '''
    

    return render_template('index.html', pitches=pitches)