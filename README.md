apptime
=======
Apptime web service gives  you control over the usage of family devices

Build Status
------------
[ ![Codeship Status for piohhmy/apptime](https://www.codeship.io/projects/8e5f1f50-402f-0131-177a-7a95864a21a3/status?branch=master)](https://www.codeship.io/projects/10526)

API Reference
-----------
### GET /apptime/user/\<username\>/apps/usage
Response:
```json
{ "usage": [
                       {"category": "Game", "apps" : [
                              {"name": "Super Mario Brothers", "weekly_time": 10},
                              {"name": "Candy Crush", "weekly_time": 230} ]
                       },
                       {"category": "Social", "apps" : [
                              {"name": "Facebook", "weekly_time": 45},
                              {"name": "Twitter", "weekly_time": 10},
                              {"name": "Snapchat", "weekly_time": 40},
                               ]
                       }
                       ]
        } 
```
### POST /apptime/user/\<username\>/apps/usage
Response:
```json
{}
```
### POST /apptime/device
```json
{"id":"61de5f49-c5b8-4afe-ae52-6496d3044770"}
```
### GET /apptime/user/\<username\>/devices
```json
{"devices":[{"device_name": "Galaxy Nexus",  "id": "123"}]}
```
### GET /apptime/users
```json
{"users":[{"name": "Tommy"}, {"name": "Sandy"}]}
```