# the_quiz_app

A robust backend for a quiz application built with Django and Django REST Framework.
This project provides APIs for creating, managing, and taking quizzes. It supports quiz creation, question management, and score tracking.

## Features

* Quiz Management: Create, update, and delete quizzes.

* Question Management: Add multiple-choice questions to quizzes.

* Score Tracking: Track user scores for each quiz.

* RESTful APIs: Built with Django REST Framework for easy integration with frontend apps.

* Admin Panel: Django admin interface for managing quizzes and users.

## Setup/Installation Requirements

* Follow these steps to set up the project locally:
* Clone the repository:
  * git clone https://github.com/edosatk/the_quiz_app.git
* cd django-quiz-app-backend
* Set up a virtual environment:
 * python -m venv venv
 * source venv/bin/activate  
* Install dependencies:
 * pip install -r requirements.txt
* Set up the database:
 * Update the DATABASES setting in settings.py if you're not using SQLite.
* Run migrations:
  * python manage.py migrate
* Create a superuser (for admin access):
  * python manage.py createsuperuser
* Run the development server:
 * python manage.py runserver
* Access the admin panel:
 * Visit http://127.0.0.1:8000/admin/ and log in with your superuser credentials.


## Contact Information

gendabusen@gmail.com_
