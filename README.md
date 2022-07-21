# Django-Projects

1.python -m venv mylabenv //Create a virtual environtment that name is 'mylabenv'
2.python --version //check python version 
3.cd mylabenv 
3.cd Script
4.--> activate
5.pip install django // install django
6.django-admin startproject mylabproject //create a django project named 'mylabproject'
7.open korte hbe sript er vitorer folder
8.open project using pycharm
9.click terminal
10.cd.. goto script .then write " activate " //eta korte hbe terminal e    
11.python manage.py startapp mylabook //terminal 
12. python manage.py makemigrations // in terminal
13.python manage.py migrate //into terminal (to connect database --sqllite3)
14.goto  mylabproject goto sitting goto Templates and add " 'DIRS': [os.path.join(BASE_DIR, 'templates')],"
15.goto mylabproject goto url set the url  "path('labbook/', include('mylabbook.urls'))," //connect mylabbook apps url(mylabbbok is application)
16.Creates a directoy named template


17.Goto "templates" create a dirctory named "mylabbook"(We use templates for html and css file )
18.Into mylabook create a HTML file named "Home"
19.Create another HTML file name "base"
20. Create block into the "base.html" // block is a template so that it can be inherited into different files.
21.goto "boostrap 5" webside  goto download section goto "CDN via jsDelivr" copy this four links and paste into "base.html" into hed after title



23.Create database table using "models.py" of mylabbook
24.Goto "models.py" and create a database table.




25.goto lab3 goto sittings.py add "'mylabbook'" into installed apps
26.python manage.py makemigrations

27.python manage.py migrate

28.create "urls.py" into maylabook folder  and add url  from lab3 mylabooks url
29.create "views.py" into mylabook folder and link a html page .(We use home.html)




30.python manage.py createsuperuser   enter
31.username:admin email: " " passward:123
32.python manage.py runserver
33.run the "http://127.0.0.1:8000/admin/"
34.




 
