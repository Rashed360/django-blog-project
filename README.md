# django-blog-project

## Dependencies:
- `Django==4.0.1`
- `Pillow==9.0.0`
- `django-crispy-forms==1.14.0`
- `django-cleanup==5.2.0`

## Installation Process
The Given Project needs virtual environment to work, so please follow below steps.
first clone or fork this repo

### Creating the Vitual Environment with `venv`
```bash
python -m venv venv
```

### Activating `venv` on Windows With CMD.
```cmd
venv\\Scripts\\activate.bat
```

### Activating `venv` on Windows With Powershell.
```powershell
./venv/Scripts/activate.ps1
```

### Activating `venv` on Windows With Shells Like Windows Terminal or Git Bash.
```bash
source venv/Scripts/activate
```

### Activating `venv` on Linux Based OS or MacOS
```bash
source venv/bin/activate
```

### Install the dependencies
```bash
pip install -r requirements.txt
```

### Migrate the project
```python3
python manage.py makemigrations

python manage.py migrate
```

### Lastly Run Server Locally
```python3
python manage.py runserver
```
