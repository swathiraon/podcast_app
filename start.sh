export LC_ALL=C.UTF-8
export LANG=C.UTF-8
nginx
pipenv run gunicorn -w 4 --bind unix:bit.sock -m 777 app:app
