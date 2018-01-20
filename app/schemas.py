from marshmallow import Schema, fields, ValidationError

from app import app
from models import Event, EventVenue, EventType, Organizer

def validate_empty(data):
	if not data:
		raise ValidationError('Cannot be empty')

class BaseSchema(Schema):
	pass

class EventSchema(BaseSchema):
	id = fields.Integer(dump_only = True)
	name = fields.Str(required = True, validate = validate_empty)
	description = fields.Str(missing = None)
	event_type_id = fields.Integer(required = True)
	start_date = fields.DateTime('%Y-%m-%d %H:%M:%S', required = True)
	end_date = fields.DateTime('%Y-%m-%d %H:%M:%S', required = True)
	organizer = fields.Nested('OrganizerSchema', required = True)
	venue = fields.Nested('EventVenueSchema', required = True)
	type = fields.Nested('EventTypeSchema', dump_only = True)

class EventVenueSchema(BaseSchema):
	id = fields.Integer(dump_only = True)
	name = fields.Str(required = True, validate = validate_empty)
	address1 = fields.Str(required = True, validate = validate_empty)
	address2 = fields.Str(missing = None)
	landmark = fields.Str(missing = None)
	city = fields.Str(required = True, validate = validate_empty)
	pin_code = fields.Str(required = False, missing = None)

class EventTypeSchema(BaseSchema):
	id = fields.Integer(dump_only = True)
	name = fields.Str(required = True, validate = validate_empty)
	description = fields.Str(required = True, missing = None)

class OrganizerSchema(BaseSchema):
	id = fields.Integer(dump_only = True)
	first_name = fields.Str(required = True, validate = validate_empty)
	last_name = fields.Str(missing = None)
	email = fields.Str(required = True, validate = validate_empty)
	phone_number = fields.Str(missing = None)

event_schema = EventSchema()
event_schema_list = EventSchema(many = True)
event_type_schema = EventTypeSchema()
event_type_schema_list = EventTypeSchema(many = True)