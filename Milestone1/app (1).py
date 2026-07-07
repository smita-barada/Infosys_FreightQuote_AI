import os
import time
import datetime
import sqlite3
import jwt
import bcrypt
import smtplib
import secrets
import streamlit as st
import plotly.graph_objects as go
from email.utils import formatdate, make_msgid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import database as db

db.init_db()

# --- Configurations ---
JWT_SECRET = os.getenv("JWT_SECRET", "super-secret-infosys-key-2026")
SENDER_EMAIL = os.getenv("EMAIL_ADDRESS", "springboardportal@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
OTP_EXPIRY_MINUTES = 5

ADMIN_EMAIL = "admin@portal.com"
ADMIN_PASSWORD = "AdminPassword@2026"

# White Theme Palette
COLORS = {
    "bg_main": "#ffffff",       # White background
    "bg_sidebar": "#f9f9f9",    # Light sidebar
    "bg_card": "#f0f0f0",       # Light grey cards
    "bg_card_alt": "#eaeaea",   # Slightly darker grey
    "text_main": "#000000",     # Black text
    "text_heading": "#111111",  # Dark headings
    "text_muted": "#555555",    # Muted grey text
    "accent": "#0066cc",        # Blue accent
    "accent_hover": "#3399ff",  # Lighter blue on hover
    "accent_text": "#ffffff",   # White text on accent buttons
    "border": "#cccccc",        # Light grey borders
    "border_light": "#dddddd",  # Very light borders
    "success": "#28a745",       # Green success
    "danger": "#dc3545"         # Red error
}



st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, .stApp {{
        background: {COLORS['bg_main']} !important;
        font-family: 'Inter', sans-serif !important;
        color: {COLORS['text_main']} !important;
    }}

    footer, div[data-testid="stDecoration"] {{
        visibility: hidden !important;
        display: none !important;
    }}
    header {{
        background: transparent !important;
        z-index: 999999 !important;
    }}

    /* Native Sidebar collapsed toggle button */
    button[kind="header"], div[data-testid="stSidebarCollapsedControl"] button {{
        visibility: visible !important;
        display: flex !important;
        opacity: 1 !important;
        background-color: {COLORS['accent']} !important;
        border: 2px solid {COLORS['border']} !important;
        border-radius: 8px !important;
        padding: 6px !important;
        margin: 8px !important;
        box-shadow: 3px 3px 0px #06b6d4 !important; /* Cyan Shadow */
    }}
    button[kind="header"] svg, div[data-testid="stSidebarCollapsedControl"] svg {{
        fill: {COLORS['text_heading']} !important;
        color: {COLORS['text_heading']} !important;
        stroke: {COLORS['text_heading']} !important;
    }}

    .block-container {{
        padding: 2rem 2.5rem !important;
        max-width: 1200px;
    }}

    h1, h2, h3, h4, h5 {{
        font-family: 'Poppins', sans-serif !important;
        color: {COLORS['text_heading']} !important;
        font-weight: 700 !important;
    }}

    label p {{
        font-weight: 600 !important;
        color: {COLORS['text_heading']} !important;
    }}

    /* Input Fields styling */
    div[data-baseweb="base-input"], div[data-baseweb="select"] > div {{
        background-color: transparent !important;
        border: none !important;
    }}
    div[data-baseweb="input"], div[data-baseweb="select"] {{
        background-color: {COLORS['bg_card_alt']} !important;
        border: 2px solid {COLORS['border']} !important;
        border-radius: 10px !important;
        padding: 2px 4px !important;
        transition: all 0.2s ease;
    }}
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {{
        border-color: #06b6d4 !important; /* Cyan border on focus */
        box-shadow: 4px 4px 0px {COLORS['border']} !important;
    }}
    input, div[data-baseweb="select"] span {{
        color: {COLORS['text_main']} !important;
        -webkit-text-fill-color: {COLORS['text_main']} !important;
        font-weight: 500 !important;
    }}

    /* Button Neo-Brutalist Cyberpunk styling */
    div[data-testid="stButton"] button {{
        background-color: {COLORS['accent']} !important;
        color: {COLORS['accent_text']} !important;
        border: 2px solid {COLORS['border']} !important;
        border-radius: 10px !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        height: 48px !important;
        min-height: 48px !important;
        box-shadow: 4px 4px 0px #06b6d4 !important; /* Neon Cyan shadow */
        width: 100%;
        transition: all 0.15s ease !important;
    }}
    div[data-testid="stButton"] button:hover {{
        background-color: {COLORS['accent_hover']} !important;
        transform: translate(-2px, -2px) !important;
        box-shadow: 6px 6px 0px #06b6d4 !important;
        color: {COLORS['accent_text']} !important;
    }}
    div[data-testid="stButton"] button:active {{
        transform: translate(2px, 2px) !important;
        box-shadow: 2px 2px 0px #06b6d4 !important;
    }}

    section[data-testid="stSidebar"] {{
        background: {COLORS['bg_sidebar']} !important;
        border-right: 2px solid {COLORS['border']} !important;
    }}

    /* Neo-Brutalist Cyberpunk card structure */
    .nb-card {{
        background-color: {COLORS['bg_card']} !important;
        border: 2px solid {COLORS['border']} !important;
        border-radius: 14px !important;
        padding: 24px !important;
        box-shadow: 6px 6px 0px {COLORS['accent']} !important; /* Neon Purple shadow */
        margin-bottom: 20px !important;
    }}

    .nb-alert {{
        border: 2px solid {COLORS['border']};
        border-radius: 8px;
        padding: 12px;
        font-weight: 500;
        margin-bottom: 15px;
    }}
</style>
""", unsafe_allow_html=True)

def validate_email_format(email):
    if '@' not in email: return False
    parts = email.split('@')
    if len(parts) != 2: return False
    local, domain = parts[0], parts[1]
    local_letters = sum(1 for c in local if c.isalpha())
    if local_letters < 2: return False
    if '.' not in domain: return False
    dot_idx = domain.rfind('.')
    domain_p1, domain_p2 = domain[:dot_idx], domain[dot_idx+1:]
    return sum(1 for c in domain_p1 if c.isalpha()) >= 2 and sum(1 for c in domain_p2 if c.isalpha()) >= 2

def validate_password_strength(password):
    if len(password) < 8: return False, "Password must be at least 8 characters long."
    if not any(c.isupper() for c in password): return False, "Password must contain at least one uppercase letter."
    if not any(c.islower() for c in password): return False, "Password must contain at least one lowercase letter."
    if not any(c.isdigit() for c in password): return False, "Password must contain at least one number."
    special_chars = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|~`"
    if not any(c in special_chars for c in password): return False, "Password must contain at least one special symbol."
    return True, ""

def make_jwt(email, is_admin=False):
    payload = {
        "email": email, "role": "admin" if is_admin else "user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2), "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def verify_jwt(token):
    try: return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except: return None

def generate_otp():
    return f"{secrets.randbelow(900000) + 100000}"

def make_otp_token(email, otp):
    otp_hash = bcrypt.hashpw(otp.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    payload = {
        "sub": email, "otp_hash": otp_hash, "type": "password_reset_otp",
        "iat": datetime.datetime.utcnow(), "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=OTP_EXPIRY_MINUTES)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def verify_otp_token(token, input_otp, email):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        if payload.get("sub") != email or payload.get("type") != "password_reset_otp":
            return False, "Security token mismatch."
        stored_hash = payload.get("otp_hash")
        if bcrypt.checkpw(input_otp.encode('utf-8'), stored_hash.encode('utf-8')):
            return True, "Valid"
        return False, "Invalid 6-digit OTP code."
    except jwt.ExpiredSignatureError:
        return False, f"This OTP code expired after {OTP_EXPIRY_MINUTES} minutes. Please request a new one."
    except:
        return False, "Invalid or expired verification token."

def send_otp_email(to_email, otp):
    if not EMAIL_PASSWORD or not SENDER_EMAIL:
        return False, "SMTP email credentials not set. Please add EMAIL_ADDRESS and EMAIL_PASSWORD to Colab Secrets."
    msg = MIMEMultipart('alternative')
    msg['From'] = f"Infosys Portal Support <{SENDER_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = "Infosys Portal - Password Reset Verification Code"
    msg['Date'] = formatdate(localtime=True)
    msg['Message-ID'] = make_msgid()
    msg['Reply-To'] = SENDER_EMAIL

    text_body = f"Your verification code is: {otp}\nExpires in {OTP_EXPIRY_MINUTES} minutes.\n"
    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; text-align: center; background-color: #09090b; color: #ffffff; padding: 20px;">
        <div style="max-width: 400px; margin: 0 auto; background-color: #18181b; border: 2px solid #ffffff; border-radius: 12px; padding: 30px; box-shadow: 5px 5px 0px #a855f7;">
            <h2 style="color: #ffffff; margin-bottom: 5px;">⚡ Verification Code</h2>
            <p style="color: #a1a1aa;">Your password reset code is:</p>
            <h1 style="background: #a855f7; color: #ffffff; padding: 15px 25px; display: inline-block; border: 2px solid #ffffff; border-radius: 8px; box-shadow: 4px 4px 0px #06b6d4; letter-spacing: 4px;">{otp}</h1>
            <p style="color: #a1a1aa; font-size: 13px;">Valid for <b>{OTP_EXPIRY_MINUTES} minutes</b>.</p>
        </div>
        <p style="color:#555; font-size:11px; margin-top:20px;">
           © 2026 Infosys Springboard
       </p>

    </body>
    </html>
    """
    msg.attach(MIMEText(text_body, 'plain'))
    msg.attach(MIMEText(html_body, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        return True, "Email sent."
    except Exception as e:
        return False, str(e)

# --- Session state init ---
for k, v in [("token", None), ("page", "Login"), ("reset_email", None), ("reset_mode", None), ("temp_otp_token", None), ("forgot_step", 1)]:
    if k not in st.session_state: st.session_state[k] = v

def navigate(to_page):
    st.session_state.page = to_page
    st.rerun()

def render_auth_header(title, subtitle="Secure Authentication Portal"):
    st.markdown(f"""
    <div style="text-align:center; padding:1rem 0;">
        <div style="font-size:48px; margin-bottom:10px;">⚡</div>
        <h1 style="font-size:2.4rem !important; margin:0; letter-spacing:-1px;">Infosys Portal</h1>
        <p style="color:{COLORS['text_muted']}; font-size:14px; margin-top:5px;">{subtitle}</p>
    </div>
    <div style="text-align:center; margin-bottom:1.5rem;">
        <span style="font-size:1.1rem; font-weight:800; color:{COLORS['text_heading']}; border-bottom: 3px solid {COLORS['accent']}; padding-bottom: 2px;">{title}</span>
    </div>
    """, unsafe_allow_html=True)

# --- Pages Layout ---
if not st.session_state.token:
    if st.session_state.page not in ["Login", "Signup", "Forgot"]:
        st.session_state.page = "Login"
    _, center_col, _ = st.columns([1, 1.4, 1])
    with center_col:
        st.markdown('<div class="nb-card">', unsafe_allow_html=True)

        if st.session_state.page == "Login":
            render_auth_header("Sign in to your account", "Welcome back! Enter credentials below")
            email = st.text_input("Username or Email address", placeholder="you@infosys.com").lower().strip()
            password = st.text_input("Password", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Sign In →", use_container_width=True):
                if not email or not password: st.error("⚠️ All fields are mandatory.")
                else:
                    is_limited, time_left = db.is_rate_limited(email)
                    if is_limited: st.error(f"❌ Account locked out. Try again in {time_left} seconds.")
                    else:
                        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
                            db.reset_login_attempts(email)
                            st.session_state.token = make_jwt(email, is_admin=True)
                            st.success("✅ Admin login successful!")
                            time.sleep(1)
                            navigate("Dashboard")
                        elif db.authenticate_user(email, password):
                            st.session_state.token = make_jwt(email, is_admin=False)
                            st.success("✅ Signed in!")
                            time.sleep(1)
                            navigate("Dashboard")
                        else: st.error("❌ Invalid credentials.")
            st.markdown("<hr style='border:1px dashed #3f3f46;'>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            if col1.button("Create Account", use_container_width=True): navigate("Signup")
            if col2.button("Forgot Password?", use_container_width=True): st.session_state.forgot_step = 1; navigate("Forgot")

        elif st.session_state.page == "Signup":
            render_auth_header("Create your Account", "Join the Infosys Springboard Portal")
            username = st.text_input("Unique Username", placeholder="e.g. JaneDoe")
            email = st.text_input("Email address", placeholder="you@infosys.com").lower().strip()
            password = st.text_input("Password", type="password", placeholder="Min. 8 characters")
            confirm_pwd = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
            sq = st.selectbox("Security Question", ["What is your pet name?", "What is your mother's maiden name?", "What is your favourite city?"])
            sa = st.text_input("Your Security Answer")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Register & Login →", use_container_width=True):
                if not username or not email or not password or not confirm_pwd or not sa: st.error("⚠️ All fields are mandatory.")
                elif not validate_email_format(email): st.error("❌ Email format invalid.")
                elif password != confirm_pwd: st.error("❌ Passwords do not match.")
                else:
                    pwd_ok, err_msg = validate_password_strength(password)
                    if not pwd_ok: st.error(f"❌ {err_msg}")
                    elif db.check_user_exists(email): st.error("❌ Email already registered.")
                    elif db.check_username_exists(username): st.error("❌ Username already taken.")
                    else:
                        if db.register_user(email, username, password, sq, sa):
                            st.session_state.token = make_jwt(email, is_admin=False)
                            st.success("🎉 Account created!")
                            time.sleep(1.5)
                            navigate("Dashboard")
                        else: st.error("❌ Database insertion error.")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("← Back to Sign In", use_container_width=True): navigate("Login")

        elif st.session_state.page == "Forgot":
            render_auth_header("Reset Password", "Recover access to your account")
            if st.session_state.forgot_step == 1:
                email = st.text_input("Enter Registered Email", placeholder="you@infosys.com").lower().strip()
                st.markdown("<br>", unsafe_allow_html=True)
                col_sq, col_otp = st.columns(2)
                if col_sq.button("Use Security Question", use_container_width=True):
                    if not email: st.error("⚠️ Please enter your email.")
                    elif not db.check_user_exists(email): st.error("❌ Email not registered.")
                    else:
                        user_info = db.get_user_by_email(email)
                        st.session_state.reset_email = email
                        st.session_state.reset_mode = "sq"
                        st.session_state.forgot_step = 2
                        st.session_state.sq_question = user_info[1]
                        st.rerun()
                if col_otp.button("Send Email OTP", use_container_width=True):
                    if not email: st.error("⚠️ Please enter your email.")
                    elif not db.check_user_exists(email): st.error("❌ Email not registered.")
                    elif not SENDER_EMAIL or not EMAIL_PASSWORD: st.error("❌ Config error: Missing sender details.")
                    else:
                        otp_code = generate_otp()
                        with st.spinner("Sending 6-digit OTP..."):
                            sent, msg = send_otp_email(email, otp_code)
                        if sent:
                            st.session_state.reset_email = email
                            st.session_state.reset_mode = "otp"
                            st.session_state.temp_otp_token = make_otp_token(email, otp_code)
                            st.session_state.forgot_step = 2
                            st.success("✅ OTP Sent! Check your inbox.")
                            time.sleep(1.5)
                            st.rerun()
                        else: st.error(f"❌ SMTP Error: {msg}")
            elif st.session_state.forgot_step == 2:
                st.write(f"💼 Recovering Account: **{st.session_state.reset_email}**")
                is_identity_verified = False
                if st.session_state.reset_mode == "sq":
                    st.info(f"❓ **Security Question:** {st.session_state.sq_question}")
                    user_answer = st.text_input("Your Security Answer").lower().strip()
                else:
                    st.info("📧 Check your email inbox for the 6-digit code.")
                    otp_input = st.text_input("6-Digit Verification Code", max_chars=6)
                new_pwd = st.text_input("New Password", type="password")
                confirm_npwd = st.text_input("Confirm New Password", type="password")
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Reset Password →", use_container_width=True):
                    if not new_pwd or not confirm_npwd: st.error("⚠️ Please fill in passwords.")
                    elif new_pwd != confirm_npwd: st.error("❌ Passwords do not match.")
                    else:
                        pwd_ok, err_msg = validate_password_strength(new_pwd)
                        if not pwd_ok: st.error(f"❌ {err_msg}")
                        elif db.check_password_reused(st.session_state.reset_email, new_pwd): st.error("❌ You cannot reuse a previous password.")
                        else:
                            if st.session_state.reset_mode == "sq":
                                user_info = db.get_user_by_email(st.session_state.reset_email)
                                if db.check_hash(user_answer, user_info[2]): is_identity_verified = True
                                else: st.error("❌ Incorrect security answer.")
                            else:
                                verified, otp_msg = verify_otp_token(st.session_state.temp_otp_token, otp_input, st.session_state.reset_email)
                                if verified: is_identity_verified = True
                                else: st.error(f"❌ {otp_msg}")
                            if is_identity_verified:
                                db.update_password(st.session_state.reset_email, new_pwd)
                                db.reset_login_attempts(st.session_state.reset_email)
                                st.success("🎉 Password updated! Redirecting...")
                                time.sleep(1.5)
                                st.session_state.reset_email, st.session_state.reset_mode, st.session_state.temp_otp_token, st.session_state.forgot_step = None, None, None, 1
                                navigate("Login")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("← Cancel & Back to Login", use_container_width=True):
                st.session_state.reset_email, st.session_state.reset_mode, st.session_state.temp_otp_token, st.session_state.forgot_step = None, None, None, 1
                navigate("Login")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    payload = verify_jwt(st.session_state.token)
    if not payload:
        st.session_state.token, st.session_state.page = None, "Login"
        st.error("Session expired.")
        time.sleep(1.5)
        st.rerun()
    email = payload["email"]
    role = payload["role"]
    username = "Administrator" if role == "admin" else db.get_user_by_email(email)[0]

    with st.sidebar:
        st.markdown(f"""
        <div style="padding:16px 8px; text-align:center;">
            <div style="font-size:36px; margin-bottom:5px;">⚡</div>
            <div style="font-weight:800; font-size:18px; color:{COLORS['text_heading']};">Infosys Portal</div>
            <div style="font-size:11px; background:{COLORS['accent']}; color:{COLORS['text_heading']}; font-weight:700; padding:2px 8px; border-radius:30px; display:inline-block; border: 2px solid {COLORS['border']}; margin-top: 5px;">
                {"🛡️ SYSTEM ADMIN" if role=="admin" else "👤 USER CONTROL"}
            </div>
        </div>
        <hr style="border: 1px dashed {COLORS['border']}; margin: 15px 0;">
        """, unsafe_allow_html=True)
        st.write(f"Logged in as: **{username}**")
        if st.button("Logout 🚪", use_container_width=True):
            st.session_state.token, st.session_state.page = None, "Login"
            st.rerun()

    if role == "admin":
        st.markdown(f"""
        <div style="background:{COLORS['text_heading']}; border: 3px solid {COLORS['border']}; border-radius:16px; padding:24px 32px; display:flex; justify-content:space-between; align-items:center; margin-bottom:24px; box-shadow: 5px 5px 0px {COLORS['accent']};">
            <div>
                <h1 style="color:{COLORS['accent']} !important; margin:0; font-size:24px !important;">🛡️ ADMIN CENTER</h1>
                <div style="color:{COLORS['text_muted']}; font-size:13px; font-weight:500;">Registered Accounts Management</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        users_list = db.get_all_users()
        total_accounts = len(users_list)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="nb-card" style="text-align:center;">👥 <h2>{total_accounts}</h2>Total Users</div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="nb-card" style="text-align:center;">🔒 <h2>Active</h2>System Shield</div>', unsafe_allow_html=True)

        st.markdown("### 📋 Registered User Database")
        with st.container():

            search = st.text_input("🔍 Search accounts...", "").lower().strip()
            filtered = [u for u in users_list if search in u[0].lower() or search in u[1].lower()]
            if not filtered: st.info("No matching accounts.")
            else:
                for idx, u in enumerate(filtered):
                    col_det, col_act = st.columns([5, 1.2])
                    col_det.markdown(f"**{u[0]}** | `{u[1]}` | Created: {u[2]}")
                    if col_act.button("Delete User", key=f"del_{idx}_{u[1]}"):
                        db.delete_user(u[1])
                        st.success(f"Deleted user {u[0]}!")
                        time.sleep(1)
                        st.rerun()
    else:
        st.markdown(f"""
        <div style="background:{COLORS['text_heading']}; border: 3px solid {COLORS['border']}; border-radius:16px; padding:24px 32px; display:flex; justify-content:space-between; align-items:center; margin-bottom:24px; box-shadow: 5px 5px 0px {COLORS['accent']};">
            <div>
                <h1 style="color:{COLORS['accent']} !important; margin:0; font-size:24px !important;">⚡ USER DASHBOARD</h1>
                <div style="color:{COLORS['text_muted']}; font-size:13px;">Welcome back to your workspace</div>
            </div>
            <div style="background:{COLORS['accent']}; padding:8px 18px; border:2px solid {COLORS['border']}; border-radius:30px; font-weight:700; color:{COLORS['text_heading']}; font-size:14px;">👤 {username}</div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        for idx, (icon, lbl, val) in enumerate([("📄", "Docs Indexed", "128"), ("🔍", "Queries Run", "47"), ("📊", "Efficiency", "98.4%"), ("🛡️", "Shield", "Active")]):
            with [c1, c2, c3, c4][idx]:
                st.markdown(f'<div class="nb-card" style="text-align:center;"><h3>{icon} {val}</h3>{lbl}</div>', unsafe_allow_html=True)

        chart_col, sand_col = st.columns([1.5, 1])
        with chart_col:
            st.markdown("### 📈 System Status Index")
            with st.container(border=True):
                fig = go.Figure(go.Indicator(
                    mode="gauge+number", value=96,
                    title={"text": "Performance Index", "font": {"color": COLORS['text_heading'], "size": 13, "family": "Poppins"}},
                    gauge={"axis": {"range": [0, 100]}, "bar": {"color": COLORS['accent']}, "bgcolor": COLORS['bg_card_alt'], "borderwidth": 2, "bordercolor": COLORS['border']}
                ))
                fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={"color": COLORS['text_main'], "family": "Inter"}, height=280, margin=dict(l=20, r=20, t=50, b=20))
                st.plotly_chart(fig, use_container_width=True)
        with sand_col:
            st.markdown("### ⚡ Analytics Sandbox")
            with st.container(border=True):
                metric = st.selectbox("Select Metric", ["Server Load (%)", "Latency (ms)", "Active Connections"])
                hours = st.slider("Timeframe (Hours)", 1, 24, 6)
                if st.button("Generate Telemetry", use_container_width=True):
                    times = [f"-{h}h" for h in range(hours, -1, -1)]
                    values = [int(10 + (idx * 5) % 80) for idx in range(len(times))]
                    fig_line = go.Figure(go.Scatter(x=times, y=values, mode='lines+markers', line=dict(color=COLORS['accent'], width=3)))
                    fig_line.update_layout(title=metric, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color=COLORS['text_main']), height=180, margin=dict(l=10, r=10, t=30, b=10))
                    st.plotly_chart(fig_line, use_container_width=True)
