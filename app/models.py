from app import db

from datetime import datetime

class Event(db.Model):
	"""
	event table
	"""

	__tablename__ = "event"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	created = db.Column(db.Date(), default = datetime.utcnow)
	updated = db.Column(db.Date(), onupdate = datetime.utcnow)

	def __repr__(self):
		return "Event: " + format(self)

class EventType(db.Model):
	"""
	Event Type Table
	"""

	__tablename__ = "event_type"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	created = db.Column(db.Date(), default = datetime.utcnow)
	updated = db.Column(db.Date(), onupdate = datetime.utcnow)

	def __repr__(self):
		return "EventType: " + format(self)

class EventVenue(db.Model):
	"""
	Event Venue Table
	"""

	__tablename__ = "event_venue"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	created = db.Column(db.Date(), default = datetime.utcnow)
	updated = db.Column(db.Date(), onupdate = datetime.utcnow)

	def __repr__(self):
		return "EventType: " + format(self)

def initdb():
	print "inside main models"
	db.create_all()