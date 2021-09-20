from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    pitches = [{'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvote': 3, 'downvote': 1, 
    },
    {'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvote': 3, 'downvote': 1, 
    },
   {'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvote': 3, 'downvote': 1
    },
   {'title':'Detergent','category': 'product pitch','text': 'The best detergent in Kenya', 'upvote': 3, 'downvote': 1,
    }]


    '''
    View root page function that returns the index page and its data
    '''
    

    return render_template('index.html', pitches=pitches)