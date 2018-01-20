from flask import jsonify

SUCCESS                     = 200

BAD_REQUEST                 = 400

NOT_FOUND                   = 404

INTERNAL_SERVER_ERROR       = 500

def not_found(message = 'No record found'):
	return jsonify({
		'status': NOT_FOUND,
		'message': message
	}), NOT_FOUND

def bad_request(message = 'Invalid Request', errors = []):
	return jsonify({
		'status': BAD_REQUEST,
		'message': message,
		'errors': errors
	}), BAD_REQUEST

def success(message = 'success', data = []):
	return jsonify({
		'status': SUCCESS,
		'message': message,
		'data': data
	}), SUCCESS

def internal_server_error(message = 'Internal server error'):
	return jsonify({
		'status': INTERNAL_SERVER_ERROR,
		'message': message
	}), INTERNAL_SERVER_ERROR