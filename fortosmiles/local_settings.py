# Email settings
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

SITE_COMPANY_NAME = 'Fort O Smiles Family Dental'
EMAIL_CONTACTUS_SUBJECT = 'An message from ' + SITE_COMPANY_NAME
EMAIL_APPOINTMENT_SUBJECT = 'An appointment request from ' + SITE_COMPANY_NAME + ' Website'
EMAIL_SIGNATURE = 'Sincerely, ' + SITE_COMPANY_NAME + ' Website Messenger'
EMAIL_TO = 'pobrejuanito@gmail.com'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '0506ded70d67da'
EMAIL_HOST_PASSWORD = 'a55294a1eeb075'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR + '/static',
)
