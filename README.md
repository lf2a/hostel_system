# Hostel System

## Home
![image home](doc/home-new.jpg)

## User
### user info
![image info](doc/user-info-new.png)

### user update info
![image update info](doc/update-user-info-new.png)

### delete user
![image delete user](doc/delete-user-new.png)

## Bedrooms
![image bedrooms](doc/bedrooms-new.png)

### bedroom info
![image bedroom](doc/bedroom-new.jpg)

## Bookings
![image bookings](doc/bookings-new.png)

### Booking Delete
![image delete](doc/booking-delete-new.png)

# Rest API

## Core

### Get/Create access token
| Endpoint | Method | Auth | Body (JSON) |
|:---:|:---:|:---:|:---:|
| `/get-token/` | POST | No | `username` (email), `password` |

##### Description
>Endpoint to log in and receive the access token, providing username (email) and password

##### Output:
```json
{
  "token": "dac9c44bf18f1d370d67bb6177dea7a83b37e105"
}
```
