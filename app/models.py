from app import db

class Event(db.Model):
	"""
	event table
	"""

	__tablename__ = "event"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)

	def __repr__(self):
		return "Event: " + format(self)