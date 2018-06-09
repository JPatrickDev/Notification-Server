# Notification Server
A Python HTTP-based Notification Server. Designed to be used as a backend for
a notification system. 

## Usage
Full documentation is coming soon.

Server runs on port 8181

/notifications/add (POST) - Add a new notification. Sample JSON payload:

    {
        "type" : "message/email",
        "from" : "John Smith",
        "content" : "Hello World!"
    }
    
Return: The ID of the new notification:

    {
	    "id": "tlKdEYLpguDfK4xdzIpJh1rHNL8psS6S",
	    "success": "true"
    }
    
    

/notifications/remove (POST) - Remove a notification. Sample JSON payload:

    {
        "id" : "tlKdEYLpguDfK4xdzIpJh1rHNL8psS6S"
    }

Return: The success of the operation

    {
	    "success": "true"
    }


/notifications/list (GET) - Return a JSON array of all the current notifications.

/notifications/clear (GET) - Clears all the current notifications.

### TODO:
NotificationClients that can receive push notifications when a new notification is added
