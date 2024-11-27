# apps/authentication/services/main.py
from .otp_services import verify_otp, request_new_otp
from .token_services import generate_refresh_token
from .user_auth_services import authenticate_user, handle_login, handle_logout, check_user_verification
from .student_services import handle_student_signup, handle_student_otp_verification, handle_student_new_otp
from .company_services import handle_company_signup, handle_company_otp_verification, handle_company_new_otp
from .user_services import get_user_data

# You can choose to export them explicitly (to improve clarity for views.py)
__all__ = ['verify_otp', 'request_new_otp', 'generate_refresh_token', 'authenticate_user',
           'handle_login', 'handle_student_signup', 'handle_student_otp_verification',
           'handle_student_new_otp', 'handle_company_signup', 'handle_company_otp_verification', 'handle_company_new_otp', 'handle_logout', 'check_user_verification', 'get_user_data']
