# event-api
Flask Event Management Rest Api

### Installation

```
virtualenv venv

pip install -r requirements.txt

Rename secret.py.template inside app directory to secret.py and edit configurations
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

```

###### Response Body
```

```


#### Update Event
```
http://localhost:5000/event
METHOD: PUT
```

###### Request Body
```

```

###### Response Body
```

```


#### Delete Event
```
http://localhost:5000/event
METHOD: DELETE
```

###### Request Body
```

```

###### Response Body
```

```


#### Get Event
```
http://localhost:5000/event
METHOD: GET
```

###### Request Body
```

```

###### Response Body
```

```
