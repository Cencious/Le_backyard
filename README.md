### 
* Le_backyard


## Author: 
* Kakan Innoncencia

## Description
Le_backyard is an  application which enables a user to connect with those around their neighbourhood.A user is able to sign in and see what is going on around their neighbourhood and also post updates.


## Technology Used
The following languages have been used on this project:

* Heroku
* Python3
* Django4
* PostgreSQL


## User Stories
These are the behaviors/features that the application implements for use by a user.

Users would like to:
* Sign in with the application to start using.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete hoods,posts,businesses
* Delete hoods,posts,businesses
* Manage the application.


## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets directed to the home page  | User join Le_backyard homepage |  
If user has no account, they click on `Register` | User Register  | User is redirected to the profile set up page |
|Click `Join Hood` |You'll be able to get in to that hood| 
| Click `add post` | You'll be able to add a post in that hood| 
| Click `add business` | You'll be able to add a business in that hood| 


## SetUp / Installation Requirements
## Prerequisites
* python3
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/Cencious/Le_backyard.git
        $ cd el_Backyard

## Running the Application
* Creating the virtual environment

        $ python3 -m venv --without-pip (name of the virtual environment)
        $ source virtual/bin/activate
       

* To run the application, in your terminal:

        $ python3 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3 manage.py test


## License

MIT License

Copyright (c) Year Kakan Innoncencia/Le_backyard

