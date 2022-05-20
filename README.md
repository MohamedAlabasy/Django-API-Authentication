<h1 align="center"> Django API Authentication </h1>

## Description :  
Django API Authentication Using JWT Tokens and Rest Framework

## To run this project :   

`Step 1` :  
&nbsp; &nbsp; &nbsp; &nbsp; You must have installed virtual server i.e XAMPP on your PC (for Windows). This System in Django with source code   
&nbsp; &nbsp; &nbsp; &nbsp; is free to download, Use for educational purposes only! .  

`Step 2` :  Download the source code .
```
git clone https://github.com/MohamedAlabasy/Django-API-Authentication.git
```


`Step 3` :  Enter the project file then ...
<h3 align="center"> Windows </h3>

```
py -m venv .venv
```
```
source .venv/Scripts/activate
```
```
pip install -r requirements.txt
```
```
winpty python manage.py runserver
```
<h3 align="center"> Ubuntu </h3>

```
python3 -m venv .venv
```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
```
```
python3 manage.py runserver
```

`Step 4` :  
&nbsp; &nbsp; &nbsp; &nbsp; Create database call `hospital` then ...
```
python manage.py migrate
```
`Step 5` :  To Create Admin Account : 
```
python manage.py createsuperuser
```

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  `To help you understand the project databases, see the following ERF`
<h3 align="center"> DataBase ERD </h3>
<p align="center">
   <img src="">
</p>


