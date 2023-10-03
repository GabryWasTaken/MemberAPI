![MemberAPI](https://cdn.discordapp.com/attachments/733391066136313879/1158759181646573598/MemberAPI.png?ex=651d6a15&is=651c1895&hm=65dd26c6a2eac12cd16d9b8fd19eba89fe5e287a04cba6de484b26ed03a19a06&)

![Logo](https://img.shields.io/badge/Created%20by-GabryWasTaken-purple)
## DESCRIPTION
The MemberAPI allows you to easily manage your company's member database, with this API you can perform the following actions:  

**Add a Member** 
 * Add a new member to the database by submitting their details like name, email, role in JSON format.

**Get Members List**
 * Get a list of all the members in the database in JSON format. 

**Get Single Member** 
 * Get the details of a single member by specifying their member ID. 

**Update Member**
* Update or modify an existing member's details by specifying the member ID and the fields you want to update. 

**Delete Member**
* Delete a member from the database by specifying their member ID. \

This provides a centralized way to add, view, edit or remove members without needing to manage the database directly. It enables easy integration with your existing systems.
## PREREQUISITES

![Python3](https://img.shields.io/badge/Install-Python%203%20or%20greater-blue?link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F)

Install the external dependencies, they are located in
```bash
requirements.txt
```
## HOW TO RUN PROGRAM

* Install all of the prerequisites in your virtual environment or your machine with the following command:
```bash
pip install -r requirements.txt
```
* Write this command to run the API:
```bash
python3 ./app.py
``` 
* Or : 
```bash
flask run
``` 
if you wanna start the program with flask run you need to set the environment variable with the command:
```bash
set FLASK_APP=app.py
``` 
Once you runned the app, to authenticate yourself in the program:
* **Username**: admin
* **Password**: password
## CREDITS

Application based on the guided exercise "MemberAPI" of the "The Ultimate Flask Course" on Udemy

