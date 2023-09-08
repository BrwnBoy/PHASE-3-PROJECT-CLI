# PHASE-3-PROJECT-CLI
Authour:**Brian Mwangi Maina**

## Prequisites:

**Technologies Used**

<li>Python
<li>SQLAlchemy

**Setup/Installation Requirements**

*To run the application, in your terminal*

<li>Open the terminal and clone the repository to your local machine: git clone git@github.com:BrwnBoy/PHASE-3-PROJECT-CLI.git//
<li>cd into *PHASE-3-PROJECT-CLI*
<li>Finally, open up VS.Code by typing in (code .) in your terminal while in the repository.

### What Goes Into Making The Program Run:
(1)**Installing Of Dependencies**:
Make sure you have the dependecy library installed. You can install it using pipenv/pip:
(*pipenv install click*)

(2)**Database Configuration**:
The code assumes that you have a database and a User and Subject table defined in a file called db.py. Make sure you have the db.py file with the necessary table definitions.
Ensure that the database connection details are correctly configured in the db.py file. This includes the database URL, credentials, and any other required configuration.

(3)**Running the Code**:
Once you have the dependencies installed and the database configured, you can run the code by executing the education_app.py file using Python:
(*python3 education_app.py*)

(4)**Interacting with the CLI**:
After running the code, you can interact with the CLI by entering commands in the terminal.
Available commands:
*register_user*: Prompts for a username and adds a new user to the database.
*list_subjects*: Retrieves and displays all subjects from the database.
*quiz*: Asks a random question from the questions list and checks if the user's answer is correct or wrong.
*show_history*: Displays the unique command history.
You can enter the command names in the terminal to execute the corresponding functionality.

**Please ensure that you have the necessary dependencies, a properly configured database, and run the code using Python to interact with the CLI.**

#### License 

Copyright (c) 2023 Brian Mwangi Maina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
