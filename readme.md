# GIIS city-tour backend

# GIIS city-tour frontend
GIIS, Group 3, Universität Münster, Winter-term 2023-2024
Okemwa, Rump, Niebl

related: [frontend](https://github.com/niebl/giis_citytour_frontend)

## Description
This is the backend of an application intended for GPS-guided city tours on a mobile device. It was developed as coursework for the 'Geoinformation in Society'-course at the University Münster in the winter term of 2023.

This application requires a working [frontend](https://github.com/niebl/giis_citytour_backend) in order to be enjoyable.

## Installation
clone the repository
```bash
git clone https://github.com/niebl/giis_citytour_backend.git
```

Two .env files are needed. one for the database and one for the backend. 

copy both `.env_example` files and rename them `.env`. 

Populate them with the parameters of your choice. Keep in mind the following things:
 - database-`.env` contains login parameters for pgadmin. these are optional.
 - backend-`.env` requires the database-user name and password that will be created in the next step

enter the `database/init.sql` file. at it's end there is a boilerplate comment to create a user for the backend server to use.

uncomment this and replace `{'password'}` with a password of your choice.

**Alternatively** you may copy the boilerplate comment and run it in pgadmin or the postgres terminal to create the user.

In the root directory, to start the backend server:
- run `pip install -r requirements.txt`
- add the directory ./media and populate it with the media files to be served
- run `python index.py`

## License
This software is released under the MIT-license
[license details](license.txt)
