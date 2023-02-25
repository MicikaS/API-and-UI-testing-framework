

**It's a dockerized tool to load test APIs.** 


_Starting tests with Docker:_

Build the image from Dockerfile:  `docker build -t internship_qa-python_app .` 
 

Once image is built successfully launch the container with a following command: `docker-compose up     ` 




_Starting tests without Docker:_


**Requirements:** 

Running project requires:
* Python 3.10

**Installation** 

In order to run the tests please install the following modules from requirements.txt file:


* cd to the directory where requirements.txt is located
* activate your virtualenv
* run: pip install -r requirements.txt in your shell

or

* pip install -r /path/to/requirements.txt


**How to run tests?**

**1. Run server**

Start default server with command:

docker run -p 80:80 svenwal/jsonplaceholder

Or make env var HOST = "https://jsonplaceholder.typicode.com" 
so it can be get with HOST = os.environ.get("HOST", "https://jsonplaceholder.typicode.com"))


**2. Run tests**

* Run all tests:

Select right click on test folder and select Run 'pytest in tests'  

* Run one test:
* 
* Select right click on test file and select Run 'pytest in test_file'  


