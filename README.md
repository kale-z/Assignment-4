# Django Practice [ 4 ]
This is my fourth Django practice intending to simulate a university's courses registration system. 


<br>

## Getting Started
This project includes the following functions:

- Add a Teacher
- Add a Course
- Add a Student
- Enroll a Student
- Display all Teachers
- Display all Courses
- Display all Students
- Display all Enrolled Students


<br>

## Screenshots
Below an example of how the interface of a form looks like:

  <img src="/screenshots/add-teacher.png">


And this is how it's displayed:

  <img src="/screenshots/teachers-list.png">


## Usage
To run this project after cloning, run the following command first for migration
```
python manage.py migrate
```

Then, running the local server
```
python manage.py runserver
```
After running the localhost, all what's left is heading to form pages and fill them. Then, finally, going to each displaying page related to each form.

_Note: after running the project locally, you may need to add the URL's slug manually from ```urls.py``` as the homepage was not set_
