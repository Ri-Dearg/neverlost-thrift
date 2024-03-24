set -o errexit
pip install -r requirements.txt
python manage.py compilescss --traceback
python manage.py collectstatic --noinput --ignore=*.scss
python manage.py makemigrations && python manage.py migrate
