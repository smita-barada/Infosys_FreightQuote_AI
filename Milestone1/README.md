# Milestone 1 - User Authentication Module

## Project Description
This milestone focuses on building the foundational User Authentication Module for the Infosys FreightQuote AI application. It secures the application and ensures only authorized users can access the core freight quoting features. 

## Features Built
- *User Signup & Login:* Secure account creation and authenticated access controls.
- *Session Management:* Using JSON Web Tokens (JWT) to maintain user login states securely.
- *Secure Setup Integration:* Configured backend security variables, environment paths, and ngrok for secure public tunneling.
- *OTP Verification:* Email-based OTP delivery using Gmail App Passwords for secondary verification.

## Tech Stack Used
| Component       | Technology Used        |
|-----------------|------------------------|
| Frontend        | Streamlit + Plotly     |
| Backend         | SQLite + Python (bcrypt, jwt) |
| Authentication  | JWT, OTP via Email     |
| Deployment      | Ngrok Tunnel           |

## How to Run the Notebook
1. Open the provided Jupyter Notebook (.ipynb file) in Google Colab or your local machine.
2. Ensure you add your required environment keys (ngrok tokens, Gmail App Password) to your Colab Secrets.
3. Run all setup cells sequentially to launch the backend server.
4. Access the public web interface using the generated ngrok URL link.

## Screenshots
(Screenshots of the functioning authentication pages will be added below)

# 🔑LOGIN PAGE : This page allows registered users to sign in using their email/username and password. It also provides quick links to create a new account or recover a forgotten password.
<img width="1873" height="905" alt="Screenshot 2026-07-07 133544" src="https://github.com/user-attachments/assets/dec2bdda-83b7-41b3-955a-0effdd507de5" />
<img width="1908" height="901" alt="Screenshot 2026-07-07 133644" src="https://github.com/user-attachments/assets/0da3efdd-28c2-490e-b19d-0bf686a4f772" />

# 📝CREATE ACCOUNT PAGE:This page lets new users register by entering a unique username, email, password, and security question/answer. It ensures secure account creation before accessing the portal.
<img width="1902" height="905" alt="Screenshot 2026-07-07 134536" src="https://github.com/user-attachments/assets/0daac99f-816c-484d-9e88-19f68e01d2f6" />

# 📊DASHBOARD: After successful login, users are redirected to the dashboard. It displays system metrics such as documents indexed, queries run, efficiency percentage, and performance index. It also includes analytics tools for monitoring server load and other metrics.
<img width="1908" height="912" alt="Screenshot 2026-07-07 134623" src="https://github.com/user-attachments/assets/d0e19b9c-fa6b-495f-80a0-2a8c7816cf7a" />

# 🔒Forget Password – (Choose Recovery Method)

***This page allows users to recover their account by selecting one of two options:***
**Use Security Question** → Answer the question set during account creation.
**Send Email OTP** → Receive a 6‑digit verification code in the registered email inbox.*****
<img width="1893" height="908" alt="Screenshot 2026-07-07 134657" src="https://github.com/user-attachments/assets/383e47b8-7709-48d1-97f0-7939805d042b" />

🔒 **Password Recovery** – Security Question
This page helps users reset their password by answering their pre‑set security question. Once verified, they can create a new password to regain access.
<img width="1902" height="912" alt="Screenshot 2026-07-07 134903" src="https://github.com/user-attachments/assets/bc2518a8-d383-457b-846a-615f3c411002" />

🔒 **Password Recovery** – OTP via Email
This page allows users to reset their password using a 6‑digit OTP sent to their registered email. After entering the OTP, they can set a new password securely.
<img width="1912" height="910" alt="Screenshot 2026-07-07 135103" src="https://github.com/user-attachments/assets/6a7e81fb-edad-4653-b319-131b5b394710" />




