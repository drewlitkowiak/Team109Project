## Instructions for setting up the virtual environment:

- Make sure you have the pip package `virtualenv` installed and on your PATH  

- To create the virtual environment, use the bash command

`virtualenv env`

- Once that is done, activate the environment by typing

`source env/bin/activate`

- You can then install all required packages in requirements.txt using the following command:

`pip install -r requirements.txt`

- If you ever add more pip packages at any point, please update requirements.txt with the follwing:

`pip freeze > requirements.txt`

