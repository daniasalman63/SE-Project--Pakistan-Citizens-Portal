# The Citizen’s Portal - Project Overview

Welcome to The Citizen’s Portal, a web application developed by the Goal Diggers team to mimic citizens' engagement with the government. This project focuses on creating a secure and trustworthy platform that facilitates various functionalities to ensure a seamless interaction between citizens and the government.

## Project Team

- Ayesha Shaikh
- Dania Salman
- Haniya Arif Khan
- Shayan Qadri

## Goals and Objectives

1. **Secure and Trustworthy Election System:**
   - Implementing a robust system to ensure the integrity and accuracy of the voting process.

2. **Efficient Complaint Center:**
   - Addressing and resolving user issues or concerns through an online complaint center.

3. **Timely Updates:**
   - Providing users with timely and relevant updates on government developments and news.

4. **Intuitive User Interface:**
   - Developing an intuitive and user-friendly interface for easy navigation and accessibility.

5. **Confidentiality and Data Protection:**
   - Ensuring the confidentiality and protection of sensitive user data through robust security measures.

## Implemented Pages and Features

1. **Login and Registration:**
   - Creating a login and registration system that validates and registers users.

2. **Home Page:**
   - Central hub for users to access various features and information.

3. **Voting Page:**
   - Secure and transparent election system mimicking a ballot casting system.

4. **Contacts Page:**
   - Important contacts and helplines for citizens to access vital information.

## Technical Solution Overview

The Citizen’s Portal is built using the following technologies:

- **Backend:**
  - Python
  - Django

- **Frontend:**
  - Django/CSS/HTML

The combination of Django, CSS, and HTML is employed to create an interactive and appealing interface. Django is utilized for backend development, data management, and API creation.

For detailed sprint progress and testing information, refer to the respective sprint documents in the project repository.

## Follow the given instructions to run the project:

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [Django](https://www.djangoproject.com/) (install using `pip install django`)
- [Virtualenv](https://pypi.org/project/virtualenv/) (optional but recommended)

### Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/daniasalman63/SE-Project--Pakistan-Citizens-Portal
    ```

2. Navigate to the project directory:

    ```bash
    cd SE-Project--Pakistan-Citizens-Portal
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    virtualenv venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a superuser (admin) account:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up your admin account.

### Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to access the application.

To access the Django admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser account you created.
