# One Minute Pitch

## Built By [Hannah Waruguru](https://github.com/HWaruguru/)

## Description
One Minute Pitch is an application that allows users to submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* see the pitches other people have posted.
* vote on the pitch they liked and give it a downvote or upvote.
* be signed in for me to leave a comment
* receive a welcoming email once I sign up.
* view the pitches I have created in my profile page.
* comment on the different pitches and leave feedback.
* submit a pitch in any category.
* view the different categories.

## SetUp / Installation Requirements
### Prerequisites
* python
* flask
* postgres
* sqlalchemy
* bootstrap

### Cloning
* In your terminal:
        
        $ git clone https://github.com/HWaruguru/One-Minute-Pitch.git
        $ cd One-Minute-Pitch

## Running the Application
* To run the application:

        -> python -m venv virtual
        -> source ./virtual/bin/activate
        -> pip install -r requirements.txt
        -> Set environment variables
            export MAIL_USERNAME=""
            export MAIL_PASSWORD=""
            export ENV="development"
            export DATABASE_URL=""
            export SECRET_KEY=""
        -> After creating your local postgresql database run the migrations upgrade command below to apply migrations to your db,
        -> python manage.py db upgrade
        -> python manage.py server
        
## Testing the Application
* To run the tests:

        $ python manage.py test
        
        
## Technologies Used
* Python3.9

## License
MIT &copy;2021 [Hannah Waruguru](https://github.com/HWaruguru/)

