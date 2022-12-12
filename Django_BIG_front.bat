@echo off
call C:\Users\USER\anaconda3\Scripts\activate.bat

call D:

call cd D:\AIVLE\Project Web Code\BIG

call python manage.py makemigrations
call python manage.py migrate
Start python manage.py runserver
timeout 3
Start chrome http://127.0.0.1:8000/Introduction 