from db import db

from schemas import event_schema, event_schema_list, event_type_schema, event_type_schema_list
from models import Event, Organizer, EventVenue, EventType

def save_organizer(data):
	organizer = Organizer(
		first_name = data['first_name'],
		last_name = data['last_name'],
		email = data['email'],
		phone_number = data['phone_number']
	)
	db.session.add(organizer)
	db.session.commit()

	return organizer

def save_venue(data):
	venue = EventVenue(
		name = data['name'],
		address1 = data['address1'],
		address2 = data['address2'],
		landmark = data['landmark'],
		city = data['city'],
		pin_code = data['pin_code']
	)

	db.session.add(venue)
	db.session.commit()

	return venue

def save_event(data, organizer_id, event_venue_id):
	event = Event(
		name = data['name'],
		description = data['description'],
		organizer_id = organizer_id,
		event_type_id = data['event_type_id'],
		event_venue_id = event_venue_id,
		start_date = data['start_date'],
		end_date = data['end_date']
	)

	db.session.add(event)
	db.session.commit()

	return event

def save_event_type(data):
	event_type = EventType(
		name = data['name'],
		description = data['description']
	)

	db.session.add(event_type)
	db.session.commit()

	return event_type