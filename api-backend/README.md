# API-BACKEND

# Project Setup And Configuration

## Libraries And Packages Installation

-   If you don't have nodejs installed, follow the next link https://nodejs.org/en/
-   Open a command line interface on your cloned directory and type the following commands in order to install all
    the libraries and packages necessary for the backend environment:

> ```
> cd ./api-backend
> npm install
> ```

## Node Packages

```json
{
    "name": "intelliq",
    "version": "1.0.0",
    "description": "Project for course Software Engineering, NTUA-ECE 7th Semester",
    "main": "app.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "nodemon server.js",
        "start:prod": "set NODE_ENV=production&&nodemon server.js",
        "debug": "ndb server.js"
    },
    "author": "SoftEng22-36",
    "license": "ISC",
    "dependencies": {
        "bcryptjs": "^2.4.3",
        "body-parser": "^1.20.1",
        "cookie-parser": "^1.4.6",
        "csv-express": "^1.2.2",
        "dotenv": "^16.0.3",
        "express": "^4.18.2",
        "express-mongo-sanitize": "^2.2.0",
        "express-rate-limit": "^6.6.0",
        "helmet": "^6.0.0",
        "hpp": "^0.2.3",
        "json-2-csv": "^3.18.0",
        "json2csv": "^6.0.0-alpha.2",
        "jsonwebtoken": "^8.5.1",
        "mongoose": "^5.13.15",
        "morgan": "^1.10.0",
        "multer": "^1.4.5-lts.1",
        "ndb": "^1.1.5",
        "nodemailer": "^6.8.0",
        "slugify": "^1.6.5",
        "validator": "^13.7.0",
        "xss-clean": "^0.1.1"
    },
    "devDependencies": {
        "eslint": "^8.25.0",
        "eslint-config-airbnb": "^19.0.4",
        "eslint-config-prettier": "^8.5.0",
        "eslint-plugin-import": "^2.26.0",
        "eslint-plugin-jsx-a11y": "^6.6.1",
        "eslint-plugin-node": "^11.1.0",
        "eslint-plugin-prettier": "^4.2.1",
        "eslint-plugin-react": "^7.31.10",
        "prettier": "^2.7.1"
    }
}
```

## Creating a database connection

-   Navigate to MongDB website and create an account if you don't have one: https://www.mongodb.com/cloud/atlas/register
-   On the left menu, under Organization, select Projects and click New Project
    ![mongodbCreateProject](https://user-images.githubusercontent.com/115047054/218852130-25b48110-5ed4-4aed-8892-f7d3a901e72f.png)

-   Name yout project and select Next
    ![mongodbCreateProject2](https://user-images.githubusercontent.com/115047054/218852192-f8c6de79-e4f3-4f8e-80b3-90bfdaa70af4.png)

-   Add members if you want and select Create Project

-   Make sure to select Add Current IP Address and select Build a Database
    ![mongodbCreateProject4](https://user-images.githubusercontent.com/115047054/218852520-8faf42ed-a5d9-4300-baaf-29abe381355c.png)

-   Select Create with Free of charge
-   On the bottom select Create Cluster
    ![mongodbCreateProject5](https://user-images.githubusercontent.com/115047054/218852557-daa33503-319d-4519-b732-1148f2813f4c.png)

-   On the text fields add your desired username and password and select Create User
    ![mongodbCreateProject6](https://user-images.githubusercontent.com/115047054/218852584-a46b347e-67e9-4386-ab36-8747069a9b3e.png)

-   Scroll on the bottom and select Finish And Close
-   You will be prompted to the initial screen and you can see your project on the upper left on your screen
    ![mongodbCreateProject7](https://user-images.githubusercontent.com/115047054/218852613-7a133ece-5766-498b-8cdb-2310ab38965d.png)

-   Now on Cluster0 select Connect
    ![mongodbCreateProject8](https://user-images.githubusercontent.com/115047054/218852689-fefb50ef-20d8-4ef9-b839-1bb13d17ff06.png)

-   On the menu appeared, select Connect using MongoDB Compass. If you don't have Compass installed, you can download
    it from here https://www.mongodb.com/try/download/compass
    ![mongodbCreateProject9](https://user-images.githubusercontent.com/115047054/218852753-f1c812e1-e6ad-4523-8fc7-b23e5cd497ed.png)

-   After Compass is installed select I have MongoDB Compass and copy the connection string from the menu appeared
    ![mongodbCreateProject10](https://user-images.githubusercontent.com/115047054/218852771-fd7fc10a-8d88-49df-8ede-7e3ba2eceb98.png)

-   Close the window and open Compass. On the top left select New Connection. Copy your connection string in the URI and
    replace "<password>" with the password you provided earlier. Select Connect
    ![mongodbCreateProject11](https://user-images.githubusercontent.com/115047054/218852810-6bedcea8-3077-43d3-87fa-ea1c145c1486.png)

-   Congratulations! The database is ready and is waiting for your queries!

## Create a config.env file by setting up the folowing environmental variables

Setup the following parameters in the config.env file:

> ```
> NODE_ENV=development
> PORT=your_desired_port
> HOST=localhost
> USERNAME=your_username
> PASSWORD=your_password
> DATABASE=your_connection_string_from_MongoDB_Atlas
> DATABASE_PASSWORD=the_password_you_inserted_on_MongoDB_Atlas
> PASS_PHRASE=hellothere
> ```

JWT_SECRET variable is saved on the server and is used for the decoding of the access token. Make sure you are the only one who knows it's value for security reasons.

JWT_EXPIRES_IN variable determines the time that the token is valid.

JWT_COOKIE_EXPIRES_IN variable determines the time that the cookie is valid.

> ```
> JWT_SECRET=your_secret
> JWT_EXPIRES_IN=you_expiration_time
> JWT_COOKIE_EXPIRES_IN=your_expiration_time
> ```

## Run the server

-   Open your command line and make sure your directory is /api-backen
-   Type the following command to start the server
    > ```
    > npm start
    > ```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# REST-API DOCUMENTATION

In this documentation, the provided services of the REST API are explained so that the user can send requests with the
appropriate parameters. Note that the API supports JSON and CSV return types via query variable format.
The base url is the following:

> ```
> https://{{host}}:{{port}}/intelliq_api/
> ```

## End-point: Sign Up

Endpoint to signup a user.

### Method: POST

> ```
> /signup?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication no auth

### Response: 200

```json
{
    "status": "OK"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Invalid input data. A password must have at least 8 characters"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Username taken! Please provide a new username."
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Invalid input data. Please provide a username"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Invalid input data. Please provide a password"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Logout

Endpoint to logout a user.

### Method: POST

> ```
> /logout?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "message": "You are successfully logged out."
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "Please log in to get access."
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Login

Endpoint to login a user.

### Method: POST

> ```
> /login?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication no auth

### Response: 200

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzZTIyNjIwYmM3NWI4YjMwY2QzZTA4NSIsImlhdCI6MTY3NTc4MjAwNCwiZXhwIjoxNjgzNTU4MDA0fQ.zlKnLrxPKr2K2NhFZsNd0HdD3Wn3hHa4iEIlFllwTKs"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "Incorrect username or password!"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Please provide username and password!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Questionnaire

Endpoint to create a questionnaire. Admin provides the questionnaire as a json file.

### Method: POST

> ```
> /admin/questionnaire_upd?format=json
> ```

### Body formdata

| Param | value                                                                  | Type |
| ----- | ---------------------------------------------------------------------- | ---- |
| file  | /C:/HMMY/7thSemester/SoftEng22-36/api-backend/exampleQuestionnaire.txt | file |

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "All IDs must be unique"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Invalid input data. A questionnaire must have a title"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Reset Questionnaire

Endpoint to reset all the answers of a certain questionnaire, based on it's ID. This endpoint is accessible only to the creator of the given questionnaire.

### Method: POST

> ```
> /admin/resetq/:questionnaireID?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK"
}
```

### Response: 400

```json
{
    "status": "failed",
    "reason": "Invalid questionnaireID"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Questionnaire

Endpoint that returns an object that contains general information and the questions of a certain questionnaire. The questions are sorted by their ID. This endpoint is accessible only to the creator of the questionnaire.

### Method: GET

> ```
> /questionnaire/:questionnaireID?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "questionnaire": {
        "keywords": ["keyword1", "keyword2", "keyword3"],
        "questions": [
            {
                "qID": "T00",
                "qtext": "This is Question 0",
                "required": "FALSE",
                "type": "profile"
            },
            {
                "qID": "T01",
                "qtext": "This is Question 1",
                "required": "TRUE",
                "type": "profile"
            },
            {
                "qID": "T02",
                "qtext": "This is Question 2",
                "required": "TRUE",
                "type": "profile"
            }
        ],
        "questionnaireID": "TEST0",
        "questionnaireTitle": "An example questionnaire"
    }
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Questionnaire ID TES not found"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Question

Returns an object that contains all the information of a certain question belonging to a certain questionnaire. The options of the question are sorted by their ID. This endpoint is accessible only by the creator of the questionnaire.

### Method: GET

> ```
> /question/:questionnaireID/:questionID?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "question": {
        "options": [
            {
                "optID": "T01A1",
                "opttxt": "option 1",
                "nextqID": "T02"
            },
            {
                "optID": "T01A2",
                "opttxt": "option 2",
                "nextqID": "T02"
            },
            {
                "optID": "T01A3",
                "opttxt": "option 3",
                "nextqID": "-"
            },
            {
                "optID": "T01A4",
                "opttxt": "option 4",
                "nextqID": "T02"
            }
        ],
        "qID": "T01",
        "qtext": "This is Question 1",
        "required": "TRUE",
        "type": "profile",
        "questionnaireID": "TEST0"
    }
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Question not found"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Do Answer

Endpoint that submits the option that was given on a question of a certain questionnaire on a certain answer session of the questionnaire. This endpoint is accessible only by the user who answers this session. Note that if a question type is profile, then there must be a request body with key "answertext" and value the desired answer. If the question's type is question, then the "answertext" value must be the empty string.

### Method: POST

> ```
> /doanswer/:questionnaireID/:questionID/:session/:optionID?format=json
> ```

### Body (**raw**)

```json
{
    "answertext": ""
}
```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "message": "Answer submitted!"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Arguments provided are invalid"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "An answer has already been submitted for this question",
    "previous answer": "option 1"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "You have already submitted a session for this questionnaire"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Session's Answers

Endpoint that returns an object with the answers that were given to all the questions of a certain questionnaire during a certain answer session. The answers are sorted by the ID of the question. This endpoint is accessible only to the admin that has created the given questionnaire.

### Method: GET

> ```
> /getsessionanswers/:questionnaireID/:session?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "answers": [
            {
                "qID": "T00",
                "ans": "My answertext"
            },
            {
                "qID": "T01",
                "ans": "T01A1"
            },
            {
                "qID": "T02",
                "ans": "T02A1"
            }
        ],
        "sessionID": "TST0",
        "questionnaireID": "TEST0"
    }
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Questionnaire ID TES not found"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Session ID TST0SS not found"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Question's Answers

Endpoint that returns an object with all the answers that were given in a certain question, during all answer sessions of a certain questionnaire. The answers are sorted by the time they were submitted. This endpoint is accessible only to the admin that has created the given questionnaire.

### Method: GET

> ```
> /getquestionanswers/:questionnaireID/:questionID?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "questionnaireID": "TEST0",
        "questionID": "T00",
        "answers": [
            {
                "session": "TST0",
                "ans": "My answertext"
            }
        ]
    }
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Question ID T00aa not found"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Admin's Created Questionnaires

Endpoint that returns all the questionnaires created by the logged in admin. This endpoint is accessible only to users with role admin.

### Method: GET

> ```
> /questionnaire/getadmincreatedquestionnaires
> ```

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "questionnaires": [
            {
                "keywords": ["keyword1", "keyword2", "keyword3"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "T00OPT",
                                "opttxt": "<open string>",
                                "nextqID": "T01"
                            }
                        ],
                        "qID": "T00",
                        "qtext": "This is Question 0",
                        "required": "FALSE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "T01A1",
                                "opttxt": "option 1",
                                "nextqID": "T02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T01A2",
                                "opttxt": "option 2",
                                "nextqID": "T02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T01A3",
                                "opttxt": "option 3",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T01A4",
                                "opttxt": "option 4",
                                "nextqID": "T02"
                            }
                        ],
                        "qID": "T01",
                        "qtext": "This is Question 1",
                        "required": "TRUE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "T02A1",
                                "opttxt": "option 1",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T02A2",
                                "opttxt": "option 2",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T02A3",
                                "opttxt": "option 3",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T02A4",
                                "opttxt": "option 4",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "T02",
                        "qtext": "This is Question 2",
                        "required": "TRUE",
                        "type": "profile"
                    }
                ],
                "questionnaireID": "TEST0",
                "questionnaireTitle": "An example questionnaire"
            }
        ]
    }
}
```

### Response: 402

```json
{
    "status": "no data",
    "data": {
        "questionnaires": []
    }
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get User's Answered Questionnaires

Endpoint that returns all the questionnaires answered by the logged in user. This endpoint is accessible only to users with role user.

### Method: GET

> ```
> /questionnaire/getuseransweredquestionnaires
> ```

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "answeredQuestionnaires": [
            {
                "keywords": ["keyword1", "keyword2", "keyword3"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 1,
                                "optID": "T00OPT",
                                "opttxt": "<open string>",
                                "nextqID": "T01"
                            }
                        ],
                        "qID": "T00",
                        "qtext": "This is Question 0",
                        "required": "FALSE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 1,
                                "optID": "T01A1",
                                "opttxt": "option 1",
                                "nextqID": "T02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T01A2",
                                "opttxt": "option 2",
                                "nextqID": "T02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T01A3",
                                "opttxt": "option 3",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T01A4",
                                "opttxt": "option 4",
                                "nextqID": "T02"
                            }
                        ],
                        "qID": "T01",
                        "qtext": "This is Question 1",
                        "required": "TRUE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 1,
                                "optID": "T02A1",
                                "opttxt": "option 1",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T02A2",
                                "opttxt": "option 2",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T02A3",
                                "opttxt": "option 3",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "T02A4",
                                "opttxt": "option 4",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "T02",
                        "qtext": "This is Question 2",
                        "required": "TRUE",
                        "type": "profile"
                    }
                ],
                "questionnaireID": "TEST0",
                "questionnaireTitle": "An example questionnaire",
                "creator": "jimv"
            }
        ]
    }
}
```

### Response: 402

```json
{
    "status": "no data",
    "data": {
        "answeredQuestionnaires": []
    }
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get User's Not Answered Questionnaires

Endpoint that returns all the questionnaires that are not answered by the logged in user. This endpoint is accessible only to users with role user.

### Method: GET

> ```
> /questionnaire/getusernotansweredquestionnaires
> ```

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "notAnsweredQuestionnaires": [
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 7,
                                "optID": "Q01A1",
                                "opttxt": "Prasino",
                                "nextqID": "Q02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q01A2",
                                "opttxt": "Kokkino",
                                "nextqID": "Q02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q01A3",
                                "opttxt": "Kitrino",
                                "nextqID": "Q02"
                            }
                        ],
                        "qID": "Q01",
                        "qtext": "Poio einai to agaphmeno sas xroma;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q02A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q03"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q02A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q04"
                            }
                        ],
                        "qID": "Q02",
                        "qtext": "Asxoleiste me to podosfairo;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 11,
                                "optID": "Q03A1",
                                "opttxt": "Pao",
                                "nextqID": "Q04"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q03A2",
                                "opttxt": "Osfp ",
                                "nextqID": "Q04"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q03A3",
                                "opttxt": "AEK",
                                "nextqID": "Q04"
                            }
                        ],
                        "qID": "Q03",
                        "qtext": "Ti omada eiste;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q04A1",
                                "opttxt": "Nai",
                                "nextqID": "Q03"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q04A2",
                                "opttxt": "Oxi",
                                "nextqID": "Q03"
                            }
                        ],
                        "qID": "Q04",
                        "qtext": "Exete zhsei se nhsi;",
                        "required": "TRUE",
                        "type": "question"
                    }
                ],
                "_id": "63b57c16edfc7d4fccdb9a4b",
                "questionnaireID": "QQ001",
                "questionnaireTitle": "My second research questionnaire"
            },
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q11A1",
                                "opttxt": "Prasino",
                                "nextqID": "Q12"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q11A2",
                                "opttxt": "Kokkino",
                                "nextqID": "Q12"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q11A3",
                                "opttxt": "Kitrino",
                                "nextqID": "Q12"
                            }
                        ],
                        "qID": "Q11",
                        "qtext": "Poio einai to agaphmeno sas xroma;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q12A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q13"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q12A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q14"
                            }
                        ],
                        "qID": "Q12",
                        "qtext": "Asxoleiste me to podosfairo;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q13A1",
                                "opttxt": "Pao",
                                "nextqID": "Q14"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q13A2",
                                "opttxt": "Osfp ",
                                "nextqID": "Q14"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q13A3",
                                "opttxt": "AEK",
                                "nextqID": "Q14"
                            }
                        ],
                        "qID": "Q13",
                        "qtext": "Ti omada eiste;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q14A1",
                                "opttxt": "Nai",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q14A2",
                                "opttxt": "Oxi",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "Q14",
                        "qtext": "Exete zhsei se nhsi;",
                        "required": "TRUE",
                        "type": "question"
                    }
                ],
                "_id": "63b6f8cd945aba5410493f82",
                "questionnaireID": "QQ042",
                "questionnaireTitle": "My third research questionnaire"
            },
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "P20TXT",
                                "opttxt": "<open string>",
                                "nextqID": "Q21"
                            }
                        ],
                        "qID": "P20",
                        "qtext": "Poio einai to email sas?",
                        "required": "FALSE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 2,
                                "optID": "Q21A1",
                                "opttxt": "Prasino",
                                "nextqID": "Q22"
                            },
                            {
                                "wasChosenBy": 1,
                                "optID": "Q21A2",
                                "opttxt": "Kokkino",
                                "nextqID": "Q22"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q21A3",
                                "opttxt": "Kitrino",
                                "nextqID": "Q22"
                            }
                        ],
                        "qID": "Q21",
                        "qtext": "Poio einai to agaphmeno sas xroma;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 2,
                                "optID": "Q22A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q23"
                            },
                            {
                                "wasChosenBy": 1,
                                "optID": "Q22A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q24"
                            }
                        ],
                        "qID": "Q22",
                        "qtext": "Asxoleiste me to podosfairo;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q23A1",
                                "opttxt": "Pao",
                                "nextqID": "Q24"
                            },
                            {
                                "wasChosenBy": 2,
                                "optID": "Q23A2",
                                "opttxt": "Osfp ",
                                "nextqID": "Q24"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q23A3",
                                "opttxt": "AEK",
                                "nextqID": "Q24"
                            }
                        ],
                        "qID": "Q23",
                        "qtext": "Ti omada eiste;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 1,
                                "optID": "Q24A1",
                                "opttxt": "Nai",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 2,
                                "optID": "Q24A2",
                                "opttxt": "Oxi",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "Q24",
                        "qtext": "Exete zhsei se nhsi;",
                        "required": "TRUE",
                        "type": "question"
                    }
                ],
                "_id": "63bc110ded7ab64f38d39687",
                "questionnaireID": "QQ052",
                "questionnaireTitle": "My fourth research questionnaire"
            },
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "P30TXT",
                                "opttxt": "<open string>",
                                "nextqID": "Q31"
                            }
                        ],
                        "qID": "P30",
                        "qtext": "Poio einai to email sas?",
                        "required": "FALSE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q31A1",
                                "opttxt": "Prasino",
                                "nextqID": "Q32"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q31A2",
                                "opttxt": "Kokkino",
                                "nextqID": "Q32"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q31A3",
                                "opttxt": "Kitrino",
                                "nextqID": "Q32"
                            }
                        ],
                        "qID": "Q31",
                        "qtext": "Poio einai to agaphmeno sas xroma;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q32A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q33"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q32A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q34"
                            }
                        ],
                        "qID": "Q32",
                        "qtext": "Asxoleiste me to podosfairo;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q33A1",
                                "opttxt": "Pao",
                                "nextqID": "Q34"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q33A2",
                                "opttxt": "Osfp ",
                                "nextqID": "Q34"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q33A3",
                                "opttxt": "AEK",
                                "nextqID": "Q34"
                            }
                        ],
                        "qID": "Q33",
                        "qtext": "Ti omada eiste;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q34A1",
                                "opttxt": "Nai",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q34A2",
                                "opttxt": "Oxi",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "Q34",
                        "qtext": "Exete zhsei se nhsi;",
                        "required": "TRUE",
                        "type": "question"
                    }
                ],
                "_id": "63bd62925397442ec4c12440",
                "questionnaireID": "QQ062",
                "questionnaireTitle": "My fifth research questionnaire"
            },
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "F01A1",
                                "opttxt": "Prasino",
                                "nextqID": "Q02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "F01A2",
                                "opttxt": "Kokkino",
                                "nextqID": "Q02"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "F01A3",
                                "opttxt": "Kitrino",
                                "nextqID": "Q02"
                            }
                        ],
                        "qID": "F01",
                        "qtext": "Poio einai to agaphmeno sas xroma;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "F02A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q03"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "F02A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q04"
                            }
                        ],
                        "qID": "F02",
                        "qtext": "Asxoleiste me to podosfairo;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "F03A1",
                                "opttxt": "Pao",
                                "nextqID": "Q04"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "F03A2",
                                "opttxt": "Osfp ",
                                "nextqID": "Q04"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "F03A3",
                                "opttxt": "AEK",
                                "nextqID": "F04"
                            }
                        ],
                        "qID": "F03",
                        "qtext": "Ti omada eiste;",
                        "required": "TRUE",
                        "type": "question"
                    }
                ],
                "_id": "63cc68e3759bff09749fe4c5",
                "questionnaireID": "QQ119",
                "questionnaireTitle": "My test research questionnaireDD"
            },
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "M00TXT",
                                "opttxt": "<open string>",
                                "nextqID": "M01"
                            }
                        ],
                        "qID": "M00",
                        "qtext": "erothsh1?",
                        "required": "FALSE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "M01A1",
                                "opttxt": "<30",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "M01A2",
                                "opttxt": "30-50",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "M01",
                        "qtext": "erothsh2?",
                        "required": "TRUE",
                        "type": "profile"
                    }
                ],
                "_id": "63d7a0d352683873aca8bd05",
                "questionnaireID": "QQ129",
                "questionnaireTitle": "My x research questionnaire"
            },
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 1,
                                "optID": "M14TXT",
                                "opttxt": "<open string>",
                                "nextqID": "M015"
                            }
                        ],
                        "qID": "M014",
                        "qtext": "erothsh1?",
                        "required": "FALSE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "M015A1",
                                "opttxt": "<30",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 1,
                                "optID": "M01A3",
                                "opttxt": "30-50",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "M015",
                        "qtext": "erothsh2?",
                        "required": "TRUE",
                        "type": "profile"
                    }
                ],
                "_id": "63d989469f6e9e2ff013f9c6",
                "questionnaireID": "QQ130",
                "questionnaireTitle": "My great research questionnaire"
            },
            {
                "keywords": ["funny", "critical thinking", "dilemma"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "PJ1A0",
                                "opttxt": "I'd go rock climbing",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "PJ1A1",
                                "opttxt": "I'd eat a lot of grass",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "PJ1A2",
                                "opttxt": "I'd travel to see the world on panoramic-mode on",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 12,
                                "optID": "PJ1A3",
                                "opttxt": "I'd be a software engineer",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "QJ1",
                        "qtext": "What if you could live as a goat?",
                        "required": "FALSE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "PJ0A0",
                                "opttxt": "It would ask for a raise",
                                "nextqID": "QJ1"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "PJ0A1",
                                "opttxt": "It would talk about its hopes and dreams",
                                "nextqID": "QJ1"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "PJ0A2",
                                "opttxt": "It would make the best Joe Rogan impression",
                                "nextqID": "QJ1"
                            },
                            {
                                "wasChosenBy": 12,
                                "optID": "PJ0A3",
                                "opttxt": "It would ask me to change clothes more than once a week.. that's fair",
                                "nextqID": "QJ1"
                            }
                        ],
                        "qID": "QJ0",
                        "qtext": "What if your wardrobe could talk?",
                        "required": "FALSE",
                        "type": "question"
                    }
                ],
                "_id": "63de937145d41ef8a4e65827",
                "questionnaireID": "QQ574",
                "questionnaireTitle": "What if..."
            },
            {
                "keywords": ["footbal", "islands", "timezone"],
                "questions": [
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "P90TXT",
                                "opttxt": "<open string>",
                                "nextqID": "P91"
                            }
                        ],
                        "qID": "P90",
                        "qtext": "Ποιο είναι το mail σας;",
                        "required": "FALSE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "P91A1",
                                "opttxt": "<30",
                                "nextqID": "Q91"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "P91A2",
                                "opttxt": "30-50",
                                "nextqID": "Q91"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "P91A3",
                                "opttxt": "50-70",
                                "nextqID": "Q91"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "P91A4",
                                "opttxt": ">70",
                                "nextqID": "Q91"
                            }
                        ],
                        "qID": "P91",
                        "qtext": "Ποια είναι η ηλικία σας;",
                        "required": "TRUE",
                        "type": "profile"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q91A1",
                                "opttxt": "Πράσινο",
                                "nextqID": "Q92"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q91A2",
                                "opttxt": "Κόκκινο",
                                "nextqID": "Q92"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q91A3",
                                "opttxt": "Κίτρινο",
                                "nextqID": "Q92"
                            }
                        ],
                        "qID": "Q91",
                        "qtext": "Ποιο είναι το αγαπημένο σας χρώμα;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q92A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q93"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q92A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q94"
                            }
                        ],
                        "qID": "Q92",
                        "qtext": "Ασχολείστε με το ποδόσφαιρο;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q93A1",
                                "opttxt": "Παναθηναϊκός",
                                "nextqID": "Q94"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q93A2",
                                "opttxt": "Ολυμπιακός ",
                                "nextqID": "Q94"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q93A3",
                                "opttxt": "ΑΕΚ",
                                "nextqID": "Q94"
                            }
                        ],
                        "qID": "Q93",
                        "qtext": "Τι ομάδα είστε;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q94A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q95"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q94A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q96"
                            }
                        ],
                        "qID": "Q94",
                        "qtext": "Έχετε ζήσει σε νησί;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q95A1",
                                "opttxt": "Καμία",
                                "nextqID": "Q97"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q95A2",
                                "opttxt": "Μικρή",
                                "nextqID": "Q97"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q95A3",
                                "opttxt": "Μεγάλη",
                                "nextqID": "Q97"
                            }
                        ],
                        "qID": "Q95",
                        "qtext": "Με δεδομένο ότι απαντήσατε [*Q04A1] στην ερώτηση [*Q04]: Ποια η σχέση σας με το θαλάσσιο σκι;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q96A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q97"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q96A2",
                                "opttxt": "Οχι",
                                "nextqID": "Q97"
                            }
                        ],
                        "qID": "Q96",
                        "qtext": "Είστε χειμερινός κολυμβητής",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q97A1",
                                "opttxt": "Σπάνια - καθόλου",
                                "nextqID": "Q98"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q97A2",
                                "opttxt": "Περιστασιακά",
                                "nextqID": "Q98"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q97A3",
                                "opttxt": "Τακτικά",
                                "nextqID": "Q98"
                            }
                        ],
                        "qID": "Q97",
                        "qtext": "Κάνετε χειμερινό σκι;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q98A1",
                                "opttxt": "Ναι",
                                "nextqID": "Q99"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q98A2",
                                "opttxt": "Οχι",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "Q98",
                        "qtext": "Συμφωνείτε να αλλάζει η ώρα κάθε χρόνο;",
                        "required": "TRUE",
                        "type": "question"
                    },
                    {
                        "options": [
                            {
                                "wasChosenBy": 0,
                                "optID": "Q99A1",
                                "opttxt": "Θερινή",
                                "nextqID": "-"
                            },
                            {
                                "wasChosenBy": 0,
                                "optID": "Q99A2",
                                "opttxt": "Χειμερινή",
                                "nextqID": "-"
                            }
                        ],
                        "qID": "Q99",
                        "qtext": "Με δεδομένο ότι απαντήσατε [*Q08A2] στην ερώτηση [*Q08]: Προτιμάτε τη θερινή ή την χειμερινή ώρα;",
                        "required": "TRUE",
                        "type": "question"
                    }
                ],
                "_id": "63e218ac97249b0ac007db6b",
                "questionnaireID": "QQ999",
                "questionnaireTitle": "Test Questionnaire"
            }
        ]
    }
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Questionnaire

Endpoint that deletes a certain questionnaire and all it's related data (questions, options, sessions and answers). This endpoint is accessible only to the admin that has created the given questionnaire.

### Method: DELETE

> ```
> /questionnaire/deletequestionnaire/:questionnaireID
> ```

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "message": "Questionnaire and related documents deleted successfully"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "bad request"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get All Questionnaire's Sessions

Endpoint that returns all the sessions of a certain questionnaire. This endpoint is accessible only to the admin that has created the given questionnaire.

### Method: GET

> ```
> /session/getallquestionnairesessions/:questionnaireID
> ```

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "sessions": [
            {
                "answers": [
                    {
                        "answertext": "My answertext",
                        "qID": "T00",
                        "optID": "T00OPT"
                    },
                    {
                        "answertext": "",
                        "qID": "T01",
                        "optID": "T01A1"
                    },
                    {
                        "answertext": "",
                        "qID": "T02",
                        "optID": "T02A1"
                    }
                ],
                "sessionID": "TST0"
            }
        ]
    }
}
```

### Response: 402

```json
{
    "status": "no data",
    "data": {
        "sessions": []
    }
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get All Sessions' IDs

Endpoint that returns all the session IDs currently stored in the database. This endpoint is accessible only to users with role user.

### Method: GET

> ```
> /session/getallsessionsids
> ```

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "sessionsIDs": [
            {
                "sessionID": "kT8a"
            },
            {
                "sessionID": "8uwd"
            },
            {
                "sessionID": "9iUO"
            },
            {
                "sessionID": "ld1g"
            },
            {
                "sessionID": "TST0"
            },
            {
                "sessionID": "tEsT1"
            }
        ]
    }
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get User's Questionnaire's Session

Endpoint that returns the session submitted by the logged-in user. This endpoint is accessible only to users with role user.

### Method: GET

> ```
> /session/getuserquestionnairesession/:questionnaireID
> ```

### Response: 200

```json
{
    "status": "OK",
    "data": {
        "session": {
            "answers": [
                {
                    "answertext": "My answertext",
                    "qID": "T00",
                    "optID": "T00OPT"
                },
                {
                    "answertext": "",
                    "qID": "T01",
                    "optID": "T01A1"
                },
                {
                    "answertext": "",
                    "qID": "T02",
                    "optID": "T02A1"
                }
            ],
            "_id": "63e24a7ae4555fa4bca6a89a",
            "sessionID": "TST0",
            "questionnaireID": "TEST0",
            "submitter": "test-user1",
            "__v": 1
        }
    }
}
```

### Response: 402

```json
{
    "status": "no data",
    "data": {
        "sessions": []
    }
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Healthcheck

Endpoint that confirms the connection of the server with the database.

### Method: GET

> ```
> /admin/healthcheck?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "dbconnection": "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority"
}
```

### Response: 500

```json
{
    "status": "failed",
    "dbconnection": "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Reset All

Endpoint that resets all the data stored in the database.

### Method: POST

> ```
> /admin/resetall?format=json
> ```

### Body formdata

| Param | value | Type |
| ----- | ----- | ---- |

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create User

Endpoint that creates a new user with the given role, username and password.

### Method: POST

> ```
> /admin/:usermod/:username/:password?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Username taken! Please provide a new username."
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "Invalid input data. A password must have at least 8 characters"
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get User

Endpoint that returns an object with information about a certain user.

### Method: GET

> ```
> /admin/users/:username?format=json
> ```

### Query Params

| Param  | value |
| ------ | ----- |
| format | json  |

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "user": {
        "username": "test-admin1",
        "role": "admin"
    }
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "No user found with the given username."
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete User

Endpoint that deletes a certain user.

### Method: DELETE

> ```
> /admin/users/deleteUser/:username?format=json
> ```

### Query Params

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK"
}
```

### Response: 400

```json
{
    "status": "failed",
    "message": "No user found with the given username."
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Import Dummy Data

Endpoint to import data in the database.

### Method: POST

> ```
> /dummy-data/import
> ```

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "message": "Documents imported successfully."
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Export Dummy Data

Endpoint to export data from the database.

### Method: GET

> ```
> /dummy-data/export
> ```

### 🔑 Authentication jwt with cookie

| Param  | value       | type           |
| ------ | ----------- | -------------- |
| Cookie | jwt=eyJh... | JSON web token |

### Response: 200

```json
{
    "status": "OK",
    "message": "Documents exported successfully."
}
```

### Response: 401

```json
{
    "status": "failed",
    "message": "User unauthorized to continue!"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
