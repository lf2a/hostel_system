# Hostel System

## Home
![image home](doc/home.png)

## User
### user info
![image info](doc/user-info.png)

### user update info
![image update info](doc/update-user-info.png)

### delete user
![image delete user](doc/delete-user.png)

## Notifications
![image notifications](doc/notifications.png)

### notification
![image notification](doc/notification.png)

## Bedrooms
![image bedrooms](doc/bedrooms.png)

### bedroom info
![image bedroom](doc/bedroom.png)

## Bookings
![image bookings](doc/bookings.png)

### Booking update
![image update](doc/booking-update.png)

### Booking Delete
![image delete](doc/docbooking-delete.png)

## About
![about](doc/about.png)

# Rest API


### Bedroom
| Method | Routes | Is Authenticated | Header | Body |
|-|-|-|-|-|
| `GET` | `/api/bedroom` | no | no | no |


### Client
| Method | Routes | Is Authenticated | Header | Body |
|-|-|-|-|-|
| `GET` | `/api/client` | yes | `Authorization: Token <token>` | no |
| `GET` | `/api/client/<id>` | yes | `Authorization: Token <token>` | no |
| `PUT` | `/api/client/<id>` | yes | `Authorization: Token <token>` | `username, first_name, last_name, email, phone1, phone2` |
| `DELETE` | `/api/client/<id>` | yes | `Authorization: Token <token>` | no |


### Notification
| Method | Routes | Is Authenticated | Header | Body |
|-|-|-|-|-|
| `GET` | `/api/notification` | yes | ``Authorization: Token <token>`` | no |
| `GET` | `/api/notification/<id>` | yes | `Authorization: Token <token>` | no |


### Booking
| Method | Routes | Is Authenticated | Header | Body |
|-|-|-|-|-|
| `GET` | `/api/booking` | yes | `Authorization: Token <token>` | no |


## URLs
| Method | Routes | Is Authenticated | Header | Body |
|-|-|-|-|-|
| `POST` | `/token` | no | no | `username, password` |
| `POST` | `/rest-auth/login` | no | no | `username, password` |
