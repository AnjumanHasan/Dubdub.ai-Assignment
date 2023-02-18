
# Todo List Backend

This is a submission repository for the intern assignment task allotted by Dubdub.ai 

This is the backend of a Todo application. It has different routes for different CRUD Operations

# Steps to Run

- Clone this repository.

```git clone https://github.com/AnjumanHasan/Dubdub.ai-Assignment.git```

- After cloning, navigate to the project directory 

``` cd your-project ```

- pip install the required files in requirements.txt
- Run the app.py file using the command
``` python app.py```

- The server will run on port 5000

- Head over to postman to test the APIs

- Use the following endpoints to test the working of the APIs:
```
- Add a new task :
    Method : POST 
    Endpoint : http://127.0.0.1:5000/todo

- Get all tasks List
    Method : GET
    Endpoint : http://127.0.0.1:5000/todo

- Get particular tasks based on id
    Method : GET
    Endpoint : http://127.0.0.1:5000/todo/Your-ID

-For marking the task as done/notdone 
    Method : PUT
    Endpoint : http://127.0.0.1:5000/todo/mark/Your-ID

