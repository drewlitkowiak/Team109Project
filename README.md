## Instructions for setting up the virtual environment:

use the command

`virtualenv env`

to create a virtual environment for you to use. Once that is done, type

`source env/bin/activate`

In order to activate the virtual environment.
You can then install all required packages in requirements.txt using the following command:

`pip install -r requirements.txt`


If you ever add more pip packages at any point, please update requirements.txt with the follwing:

`pip freeze > requirements.txt`

