from db import db
from datetime import datetime

from sqlalchemy.orm import backref

class Event(db.Model):
	"""
	event table
	"""

	__tablename__ = "event"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	description = db.Column(db.String(100), nullable = True)
	organizer_id = db.Column(db.Integer, db.ForeignKey("organizer.id", onupdate = "CASCADE", ondelete = "CASCADE"))
	event_type_id = db.Column(db.Integer, db.ForeignKey("event_type.id", onupdate = "CASCADE", ondelete = "CASCADE"))
	event_venue_id = db.Column(db.Integer, db.ForeignKey("event_venue.id", onupdate = "CASCADE", ondelete = "CASCADE"))
	start_date = db.Column(db.DateTime(), nullable = False)
	end_date = db.Column(db.DateTime(), nullable = False)
	deleted = db.Column(db.Boolean, default = 0)
	created = db.Column(db.DateTime(), default = datetime.now)
	updated = db.Column(db.DateTime(), onupdate = datetime.now)

	organizer = db.relationship('Organizer', backref = backref("event", uselist = False))
	venue = db.relationship('EventVenue', backref = backref("event", uselist = False))
	type = db.relationship('EventType', backref = backref("event", uselist = False))


	def __repr__(self):
		return "Event: " + format(self)

class EventType(db.Model):
	"""
	Event Type Table
	"""

	__tablename__ = "event_type"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique = True)
	description = db.Column(db.String(100), nullable = True)
	created = db.Column(db.DateTime(), default = datetime.now)
	updated = db.Column(db.DateTime(), onupdate = datetime.now)

	def __repr__(self):
		return "EventType: " + format(self)

class EventVenue(db.Model):
	"""
	Event Venue Table
	"""

	__tablename__ = "event_venue"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	address1 = db.Column(db.String(50))
	address2 = db.Column(db.String(50))
	landmark = db.Column(db.String(50))
	city = db.Column(db.String(20))
	pin_code = db.Column(db.String(10))
	created = db.Column(db.DateTime(), default = datetime.now)
	updated = db.Column(db.DateTime(), onupdate = datetime.now)

	def __repr__(self):
		return "EventVenue: " + format(self)

class Organizer(db.Model):
	"""
	Event organizer Table
	"""

	__tablename__ = "organizer"

	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	phone_number = db.Column(db.String(20))
	created = db.Column(db.DateTime(), default = datetime.now)
	updated = db.Column(db.DateTime(), onupdate = datetime.now)

	def __repr__(self):
		return "Organizer: " + format(self)