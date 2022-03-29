# Preparation
1. sudo apt install python3-pip
2. sudo apt install python3-venv
## Creating virtual environment
3. python3 -m venv ./venv
## Activating environment
4. source ./venv/bin/activate
## Installing necesary packages
5. pip install flask
    (pip install requirements)

# Launching app
Option 1:
## Preconfiguration of flask
6. export FLASK_APP=flaskpage.py
7. export FLASK_DEBUG=1
## Starting app
8. flask run

Option 2:
# By running it with python
6. if __name__ == '__main__':
    app.run(debug=True)
7. python flaskpage.py