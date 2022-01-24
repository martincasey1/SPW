1. install the below into a python virtual environemt
Package                Version
---------------------- ---------
asgiref                3.4.1
certifi                2021.10.8
cffi                   1.15.0
charset-normalizer     2.0.9
colorama               0.4.4
cryptography           36.0.0
defusedxml             0.7.1
Django                 3.2.9
django-axes            5.28.0
django-cors-headers    3.10.1
django-crispy-forms    1.13.0
django-ipware          4.0.2
django-otp             1.1.3
django-passwords       0.3.12
django-ratelimit       3.0.1
django-recaptcha       2.0.6
django-session-timeout 0.1.0
django-sslserver       0.22
ecdsa                  0.17.0
idna                   3.3
oauthlib               3.1.1
Pillow                 8.4.0
pip                    21.3.1
pyasn1                 0.4.8
pycparser              2.21
PyJWT                  2.3.0
python-jose            3.3.0
python3-openid         3.2.0
pytz                   2021.3
qrcode                 7.3.1
requests               2.26.0
requests-oauthlib      1.3.0
rsa                    4.8
setuptools             58.3.0
six                    1.16.0
social-auth-app-django 5.0.0
social-auth-core       4.1.0
sqlparse               0.4.2
urllib3                1.26.7
wheel                  0.37.0


2. activate the environment by going to the environment directory in a powershell window and activate by running .\scripts\activate
3. To test password reset and contact us form please add the below to your environment variables on your machine exactly as they are below. Machine then requires a reboot after this to take effect
    EMAIL_USER = django.blog.reset@gmail.com
    EMAIL_PASS = zathlhyxztbpisug
4. change directory to web application
5. run python .\manage.py runserver if not using the ssl cert
6. navigate to http://localhost:8000 in a browser
7. if using the ssl cert install the RootCA cert on the machine
8. note chnage the path to the cert below depnding where you save the cert.
9. run with the ssl cert: python .\manage.py runsslserver --certificate 'C:\Program Files\OpenSSL-Win64\bin\localhost.crt' --key 'C:\Program Files\OpenSSL-Win64\bin\localhost.key'
10. navigate to https://localhost:8000 in a browser

any issues please email one of the team and we can help
x20256604@student.ncirl.ie - martin Casey
x20249128@student.ncirl.ie - Luke Wynne
x21113939@student.ncirl.ie - Conor Bolton