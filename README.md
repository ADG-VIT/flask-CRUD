# Flask-CRUD

This is a boilerplate for building Flask apps.

## ▶️ Run Locally

1. _Clone_ the repo
   `git clone https://github.com/cryptus-neoxys/flask-CRUD.git <name>`
2. Setup _virtual environment_
   `python -m venv venv/`
3. _Switch_ to virtual environment for development (\<venv\> is your env name, here "venv")
   - **Windows** (`cmd`)
     - _Activate_
       `<venv>\Scripts\acitvate`
     - _Deactivate_
       `<venv>\Scripts\deacitvate`
   - **Linux/Mac**
     - _Activate_
       `source <venv>/bin/activate`
     - _Deactivate_
       `deactivate`
4. _Install_ dependencies
   `pip install -r requirements.txt`
5. Setup _DB_
   `python db_init.py`
6. _Run_ the _app_ with
   `python app.py`
7. Open [localhost:5000](http://localhost:5000/) to view your app
