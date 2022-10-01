# cs279-when2meet

A when2meet-like scheduler app built from scratch with Flask. The app uses SQLAlchemy, the Python SQL toolkit, to store users' preferences in a database. To run it locally, first clone the repo and navigate to the root directory: 
```
git clone https://github.com/ZiweiGu/cs279-when2meet.git
cd cs279-when2meet
```
Then, set up the virtual environment (called venv) using virtualenv (installation [here](https://virtualenv.pypa.io/en/latest/installation.html)):
```
virtualenv -p python3 venv 
```
Activate the virtual environment:
```
source venv/bin/activate
```
Install necessary packages:
```
pip install -r requirements.txt
```
Run the app:
```
python3 app.py
```