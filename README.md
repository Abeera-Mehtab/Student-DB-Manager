# Flask Student Management System

**Project Description:** A comprehensive Flask-based CRUD application for managing student records with enhanced security, validation, and professional UI design.

## Features

- User authentication system with admin controls
- Comprehensive student information management
- Dual validation (client-side and server-side)
- Responsive design with Bootstrap 3.5
- SQLite database with SQLAlchemy ORM
- Docker containerization for easy deployment

## Prerequisites

- Docker installed on your system
- WSL 2 (for Windows users)
- Python 3.11+ (if running without Docker)

## Building the Docker Container

1. Navigate to project directory: 
cd /path/to/FlaskApp

2. Build the Docker image: 
docker build -t student-db .

## Running the Docker Container

1. Run the container with port mapping: 
docker run -p 5000:5000 student-db

2. Access the application: 
	- Open web browser and navigate to http://localhost:5000
	- Register admin account and start managing student records

## Container Management

- Stop the container: Ctrl+C in terminal
- Run in background: docker run -d -p 5000:5000 student-db
- View running containers: docker ps
- Stop background container: docker stop <container_id>

## Development Setup (without Docker)

1. Install dependencies: 
pip install -r requirements.txt

2. Run the application: 
python app.py

## Application Structure

- app.py - Main application file with routes and security
- forms.py - WTForms implementation for data validation
- templates/ - HTML templates with Bootstrap styling
- static/ - CSS and JavaScript files
- requirements.txt - Python dependencies

## Default Admin Credentials

- Create admin account through registration page
- Use secure credentials for production deployment
