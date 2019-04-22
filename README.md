# event-api
Flask Event Management Rest Api

### Installation

```
bash install.sh
```

### run
```
bash build.sh <env>
<env: prod | dev>
```

### Api
Api documentation

#### Create Event Type
```
http://localhost:5000/event/type
METHOD: POST
```

###### Request Body
```
{
    "name": "Meetup Event",
    "description": "Friends get together"
}
```

###### Response Body
```
{
    "status": 200,
    "message": "Event type created successfully",
    "data": {
        "description": "Friends get together",
        "name": "Meetup Event"
    }
}
```


#### Get Event Type
```
http://localhost:5000/event/type
METHOD: GET
```

###### Response Body
```
{
    "status": 200,
    "message": "success",
    "data": [
        {
            "description": "technical event type",
            "name": "Technical Event",
            "id": 1
        },
        {
            "description": "Friends get together",
            "name": "Meetup Event",
            "id": 2
        }
    ]
}
```

#### Create Event
```
http://localhost:5000/event
METHOD: POST
```

###### Request Body
```
{
    "name": "Traffic Awarness",
    "description": "Awarness about how to follow traffic signal and rules",
    "event_type_id": 1,
    "start_date": "2018-12-12 04:00:00",
    "end_date": "2018-12-20 04:00:00",
    "organizer": {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@example.com",
        "phone_number": "1234567890"
    },
    "venue": {
        "name": "LK Mahal",
        "address1": "12, Sivaji Nagar",
        "address2": "",
        "landmark": "Near PVR",
        "city": "Bengaluru",
        "pin_code": "500034"
    }
}
```

###### Response Body
```
{
    "status": 200,
    "message": "event saved successfully",
    "data": {
        "description": "Awarness about how to follow traffic signal and rules",
        "end_date": "2018-12-20 04:00:00",
        "venue": {
            "city": "Bengaluru",
            "name": "LK Mahal",
            "address1": "12, Sivaji Nagar",
            "address2": "",
            "landmark": "Near PVR",
            "id": 11,
            "pin_code": "500034"
        },
        "id": 11,
        "event_type_id": 1,
        "organizer": {
            "phone_number": "1234567890",
            "first_name": "John",
            "last_name": "Smith",
            "id": 11,
            "email": "john@example.com"
        },
        "type": {
            "description": "technical event type",
            "name": "Technical Event",
            "id": 1
        },
        "start_date": "2018-12-12 04:00:00",
        "name": "Traffic Awarness"
    }
}
```


#### Update Event
```
http://localhost:5000/event/<int:event_id>
METHOD: PUT
```

###### Request Body
```
{
    "name": "Traffic Awarness",
    "description": "Awarness about how to follow traffic signal and rules",
    "event_type_id": 1,
    "start_date": "2018-12-15 04:00:00",
    "end_date": "2018-12-20 04:00:00",
    "organizer": {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@example.com",
        "phone_number": "1234567890"
    },
    "venue": {
        "name": "LK Mahal",
        "address1": "12, Sivaji Nagar",
        "address2": "",
        "landmark": "Near PVR",
        "city": "Bengaluru",
        "pin_code": "500034"
    }
}
```

###### Response Body
```
{
    "status": 200,
    "message": "Event updated successfully",
    "data": {
        "description": "Awarness about how to follow traffic signal and rules",
        "end_date": "2018-12-20 04:00:00",
        "venue": {
            "city": "Bengaluru",
            "name": "LK Mahal",
            "address1": "12, Sivaji Nagar",
            "address2": "",
            "landmark": "Near PVR",
            "id": 11,
            "pin_code": "500034"
        },
        "id": 11,
        "event_type_id": 1,
        "organizer": {
            "phone_number": "1234567890",
            "first_name": "John",
            "last_name": "Smith",
            "id": 11,
            "email": "john@example.com"
        },
        "type": {
            "description": "technical event type",
            "name": "Technical Event",
            "id": 1
        },
        "start_date": "2018-12-15 04:00:00",
        "name": "Traffic Awarness"
    }
}
```


#### Delete Event
```
http://localhost:5000/event/<int:event_id>
METHOD: DELETE
```

###### Response Body
```
{
    "status": 200,
    "message": "Event deleted successfully",
    "data": []
}
```


#### Get All Events
```
http://localhost:5000/event
METHOD: GET
```

###### Response Body
```
{
    "status": 200,
    "message": "success",
    "data": [
        {
            "description": null,
            "end_date": "2018-11-12 04:00:00",
            "venue": {
                "city": "",
                "name": "",
                "address1": "",
                "address2": "",
                "landmark": "",
                "id": 3,
                "pin_code": null
            },
            "id": 3,
            "event_type_id": 1,
            "organizer": {
                "phone_number": "",
                "first_name": "",
                "last_name": "",
                "id": 3,
                "email": ""
            },
            "type": {
                "description": "technical event type",
                "name": "Technical Event",
                "id": 1
            },
            "start_date": "2018-10-12 04:00:00",
            "name": "event name"
        }
    ]
}
```

#### Get Event By Id
```
http://localhost:5000/event/<int:event_id>
METHOD: GET
```

###### Response Body
```
{
    "status": 200,
    "message": "success",
    "data": [
        {
            "description": "Awarness about how to follow traffic signal and rules",
            "end_date": "2018-12-20 04:00:00",
            "venue": {
                "city": "Bengaluru",
                "name": "LK Mahal",
                "address1": "12, Sivaji Nagar",
                "address2": "",
                "landmark": "Near PVR",
                "id": 11,
                "pin_code": "500034"
            },
            "id": 11,
            "event_type_id": 1,
            "organizer": {
                "phone_number": "1234567890",
                "first_name": "John",
                "last_name": "Smith",
                "id": 11,
                "email": "john@example.com"
            },
            "type": {
                "description": "technical event type",
                "name": "Technical Event",
                "id": 1
            },
            "start_date": "2018-12-15 04:00:00",
            "name": "Traffic Awarness"
        }
    ]
}
```

#### Get Event - Pagination
10 results per page

```
http://localhost:5000/event/page/<int:page_number>
METHOD: GET
```

###### Response Body
```
{
    "status": 200,
    "message": "success",
    "data": [
        {
            "description": "Awarness about how to follow traffic signal and rules",
            "end_date": "2018-12-20 04:00:00",
            "venue": {
                "city": "Bengaluru",
                "name": "LK Mahal",
                "address1": "12, Sivaji Nagar",
                "address2": "",
                "landmark": "Near PVR",
                "id": 11,
                "pin_code": "500034"
            },
            "id": 11,
            "event_type_id": 1,
            "organizer": {
                "phone_number": "1234567890",
                "first_name": "John",
                "last_name": "Smith",
                "id": 11,
                "email": "john@example.com"
            },
            "type": {
                "description": "technical event type",
                "name": "Technical Event",
                "id": 1
            },
            "start_date": "2018-12-15 04:00:00",
            "name": "Traffic Awarness"
        }
    ]
}

##### test
```
