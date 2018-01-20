from flask import request, jsonify
from datetime import datetime
from status import *

from app import app, __version__
from db import db
from dbutils import *
from schemas import event_schema, event_schema_list, event_type_schema, event_type_schema_list
from models import Event, Organizer, EventVenue, EventType
from properties import env, build_version, is_db_connected

"""
check the status of the application
"""
@app.route('/status')
def status():
	app.logger.info("checking application status")
	status_data = {
		'build_version': build_version,
		'env': env,
		'is_db_connected': is_db_connected()
	}

	return jsonify(status_data)

"""
Add event using json object

METHOD: POST
"""
@app.route('/event', methods = ['POST'])
def add_event():
	app.logger.info("saving event")
	request_data = request.get_json(silent = True)
	if not request_data:
		return bad_request('Invalid Request/Invalid json format')

	event_data, errors = event_schema.load(request_data)

	if errors:
		return bad_request(errors = errors)

	event_type_id = event_data['event_type_id']

	#find event_type
	event_type = EventType.query.get(event_type_id)

	if not event_type:
		return bad_request('Event type not found')

	organizer_data = event_data['organizer'];
	organizer = save_organizer(organizer_data)

	if not organizer:
		return internal_server_error()

	venue_data = event_data['venue']
	venue = save_venue(venue_data)

	if not venue:
		return internal_server_error()

	event = save_event(event_data, organizer.id, venue.id)
	if not event:
		return internal_server_error()

	app.logger.info("event saved successfully")

	return success(message = 'event saved successfully', data = event_schema.dump(event).data)

"""
Get all events without pagination

METHOD: GET
"""
@app.route('/event', methods = ['GET'])
def get_event():

	all_events = Event.query.filter_by(deleted = False).all()

	if not all_events:
		return not_found()

	result = event_schema_list.dump(all_events)

	return success(data = result.data)

"""
Get event by pagination

METHOD: GET
"""
@app.route('/event/page/<int:page_number>', methods = ['GET'])
def get_event_per_page(page_number):
	events = Event.query.filter_by(deleted = False).paginate(page = page_number, per_page = 10)

	if not events:
		return not_found()

	result = event_schema_list.dump(events.items)

	return success(data = result.data)

"""
Get event by event.id

METHOD: GET
"""
@app.route('/event/<int:event_id>', methods = ['GET'])
def get_event_by_id(event_id):
	event = Event.query.filter_by(deleted = False, id = event_id).all()
	if not event:
		return not_found()

	result = event_schema_list.dump(event)

	return success(data = result.data)

"""
Update event by given event.id

METHOD: PUT
"""
@app.route('/event/<int:event_id>', methods = ['PUT'])
def update_event(event_id):
	event = Event.query.filter_by(deleted = False, id = event_id).first()
	if not event:
		return not_found()

	request_data = request.get_json(silent = True)
	if not request_data:
		return bad_request()

	event_data, errors = event_schema.load(request_data)

	if errors:
		return bad_request(errors = errors)

	organizer_data = event_data['organizer']
	if organizer_data:
		event.organizer.first_name = organizer_data['first_name']
		event.organizer.last_name = organizer_data['last_name']
		event.organizer.email = organizer_data['email']
		event.organizer.phone_number = organizer_data['phone_number']

	venue_data = event_data['venue']
	if venue_data:
		event.venue.name = venue_data['name']
		event.venue.address1 = venue_data['address1']
		event.venue.address2 = venue_data['address2']
		event.venue.landmark = venue_data['landmark']
		event.venue.city = venue_data['city']
		event.venue.pin_code = venue_data['pin_code']

	event.name = event_data['name']
	event.description = event_data['description']
	event.start_date = event_data['start_date']
	event.end_date = event_data['end_date']
	event.event_type_id = event_data['event_type_id']

	db.session.commit()

	return success(message = 'Event updated successfully', data = event_schema.dump(event).data)

"""
Delete event by given event.id

METHOD: DELETE
"""
@app.route('/event/<int:event_id>', methods = ['DELETE'])
def delete_event(event_id):
	event = Event.query.filter_by(deleted = False, id = event_id).first()
	if not event:
		return not_found()

	event.deleted = True
	db.session.commit()

	return success(message = 'Event deleted successfully')

"""
Add event type using json

METHOD: POST
"""
@app.route('/event/type', methods = ['POST'])
def add_event_type():
	app.logger.info("saving event type")
	request_data = request.get_json(silent = True)
	if not request_data:
		return bad_request('Invalid request')

	event_type_data, errors = event_type_schema.load(request_data)

	if errors:
		return bad_request()

	event_type = save_event_type(event_type_data)

	db.session.commit()

	return success(message = 'Event type created successfully', data = event_type_data)

"""
Get event type list

METHOD: GET
"""
@app.route('/event/type', methods = ['GET'])
def get_event_type():
	app.logger.info("getting event type")
	event_types = EventType.query.all()
	result = event_type_schema_list.dump(event_types)
	return success(data = result.data)