#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

from app import db

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    web_link = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    talent_required = db.Column(db.Boolean, nullable=False, default=False)
    talent_description = db.Column(db.String())

    # Implement relationship of Venue to Show
    shows = db.relationship('Show', backref='venue')


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    web_link = db.Column(db.String(120))
    venue_required = db.Column(db.Boolean, nullable=False, default=False)
    venue_description = db.Column(db.String())

    # Implement relationship of Artist to Show
    shows = db.relationship('Show', backref='artist')


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
   __tablename__ = 'Show'
   id = db.Column(db.Integer, primary_key=True)
   artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
   venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
   date_time = db.Column(db.String(60), nullable=False)