# Milestone 1: User Authentication Module

## Project Name

Intelligent Freight Quote Generation System

## Overview

This milestone focuses on building the user authentication module for the Intelligent Freight Quote Generation System. The purpose of this module is to provide secure user registration, login, password recovery, session handling, and admin access.

The application is built using Streamlit and runs in Google Colab. A public web link is generated using ngrok so the application can be opened and tested in a browser.

---

## Features Built

### Landing Page
The landing page introduces the Intelligent Freight Quote Generation System and provides navigation to user login, signup, and admin login.

### Login Page
The login page allows any registered user to login using either username or email and password.

### Signup Page
The signup page allows a new user to create an account by entering username, email, password, confirm password, security question, and security answer.

### Forgot Password Page
The forgot password page provides two recovery methods:

1. Security Question Method
2. Email OTP Method

Both methods allow the user to verify their identity and reset the password.

### User Dashboard
After successful login, the user is redirected to the dashboard. The dashboard displays username, email, JWT session status, recent login, notification, and logout option.

### Admin Login
A separate admin login page is created for administrator access.

### Admin Dashboard
The admin dashboard displays registered users in a table. It shows username, email, created date, and recent login. Passwords are never displayed.

---
## Screenshots
1.Landing page-
<img width="1911" height="912" alt="Landing page 01" src="https://github.com/user-attachments/assets/4456c44a-8a3d-4a4d-9b97-cc6f69d68825" />
2.User Login page-
<img width="1912" height="915" alt="User Login Page 01" src="https://github.com/user-attachments/assets/86e2a6cc-03db-4aad-85a5-1554b5a06178" />
3.Sign Up page-
<img width="1912" height="912" alt="SignUp Page 01" src="https://github.com/user-attachments/assets/ecd70deb-9dd0-4958-8e44-489182e28af8" />
4.Forgot Password: via Security question-
<img width="1908" height="910" alt="Forgot Password- via Security Question 01" src="https://github.com/user-attachments/assets/e3d9c865-0f59-4c29-89a3-596c1e5d72b8" />
5.Forgot Password: via OTP Email-
<img width="1907" height="907" alt="Via OTP Email 01" src="https://github.com/user-attachments/assets/73b0f8c5-6f22-4e96-82cc-fdeb0c247bbb" />
<img width="1513" height="742" alt="OTP email(Inbox Page) 01" src="https://github.com/user-attachments/assets/06328b19-d9b6-43f7-9c72-bb0e11d323d9" />
6.User Dashboard-
<img width="1908" height="905" alt="User Dashboard 01" src="https://github.com/user-attachments/assets/11bbca20-b79f-4028-b159-70105bc86036" />
7.Admin Login Page-
<img width="1907" height="910" alt="Admin Login 01" src="https://github.com/user-attachments/assets/36092a9f-b2ad-46eb-9914-9ba4c9e492d7" />
8.Admin Dashboard-
<img width="1902" height="911" alt="Admin Dashboard 01" src="https://github.com/user-attachments/assets/2a035bea-8bcd-44b0-a075-cec11ca5eaff" />

----

## Tech Stack Used

- Python
- Streamlit
- SQLite
- bcrypt
- PyJWT
- pyngrok
- Gmail SMTP
- Google Colab

---

## Architecture

The application follows a simple modular structure.

```text
Google Colab Notebook
        |
        |-- Streamlit UI
        |     |-- Landing Page
        |     |-- Signup Page
        |     |-- Login Page
        |     |-- Forgot Password Page
        |     |-- User Dashboard
        |     |-- Admin Login
        |     |-- Admin Dashboard
        |
        |-- SQLite Database
        |     |-- users table
        |     |-- password_history table
        |
        |-- Security Layer
              |-- bcrypt password hashing
              |-- JWT session token
              |-- Email OTP
              |-- Security question verification
              
------
## Database Design
-users table
-Stores user account details.
-email
-username
-password_hash
-security_question
-security_answer_hash
-created_at
-recent_login   
----

## password_history table
Stores previous password hashes to prevent password reuse.
-id
-email
-password_hash
-set_at
----

## Security Features
-Passwords are hashed using bcrypt.
-Security answers are also hashed.
-JWT is used for session handling.
-Passwords are never shown in the admin dashboard.
-OTP is sent to the registered email.
-Sensitive details are stored in Colab Secrets.
-Admin login is separate from normal user login.
----

## Validation Rules
Email Validation
~The email must follow a valid format like: ab@cd.ef
---

## Password Validation
Password must contain:
-Minimum 8 characters
-At least one uppercase letter
-At least one lowercase letter
-At least one number
-At least one special symbol
Example:
Welcome@123
---

## How to Run the Notebook
1.Open the notebook in Google Colab.
2.Install the required libraries.
!pip -q install streamlit pyngrok bcrypt PyJWT
3.Add the following values in Colab Secrets:
-NGROK_AUTHTOKEN
-JWT_SECRET
-EMAIL_ADDRESS
-EMAIL_PASSWORD
4.Run the notebook cells from top to bottom.
5.Start the Streamlit app.
6.Open the public ngrok URL generated by the notebook.
---

##Colab Secrets
The following secrets are used:
1.NGROK_AUTHTOKEN
2.JWT_SECRET
3.EMAIL_ADDRESS
4.EMAIL_PASSWORD
*EMAIL_PASSWORD should be a Gmail App Password, not the normal Gmail password*











