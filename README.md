# Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

## Installation

Create virtual environment with command:
```
virtualenv -p python3 venv
```
Activate virtual environment by command:
```
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
Migration Command to create tables in db:
```
python manage.py migrate
```
Command to run server:
```
python manage.py runserver
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)