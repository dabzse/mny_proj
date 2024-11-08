# Mihaly Nyilas

hopefully this file will be updated...

see the result on ["DEV"](http://dabzse.net/dev.php) url

## offline usage

### setup

1. `git clone https://github.com/dabzse/mny_proj.git`
2. `cd mny_proj`
3. create a new virtual environment and run it or use an existing one
4. `pip install -r requirements.txt`
5. `mkdir static`
6. `cp assets/* static/`
7. `rm -rf static/admin`

steps 5-7: so, copy everything from the assets directory to the static directory, except the admin folder \
if you would like to see the warnings and errors, you can run the server with the `DEBUG=True` option or you can edit the configuration file and set the `DEBUG` variable to `True` (in line 13)

### run

`python manage.py runserver`
