# microservice_project
This will hold the code for the microservice i implemented for my partners project 

Paywall detector Microservice

You can receive data from the microservice by sending a GET request to the '/check_paywall'
endpoint with the 'url' query parameter set to the url for the news article that you want to check 

GET /check_paywall?url=https://https://www.theatlantic.com/ideas/archive/2023/04/why-first-republic-failing/673914/

This will return a response indicating wether or not a paywall was detected, and if so whether it was removed by 12ft.io

The microservice returns a response indicating whether or not a paywall was detected and if so, whether it was removed by 12ft.io.
The response will be 0 if 'No paywall was detected', 1 if paywall was detected but removed by 12ft.io and -1 if paywall was detected but not removed by 12ft.io.

![UML Diagram for the microservice](./'Screenshot 2023-05-08 203251.jpg')
