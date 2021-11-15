# Simple django blog

#### Чтобы запустить проект вам нужно сделать следующие шаги:
1) В любой удобной директории mkdir 'название директории с будущим проектом'
2) git init в новосозданной директории
3) git clone git@github.com:Se7enquick/justblog.git
4) cd justblog/
5) pip3 install virtualenv
6) virtualenv 'любое удобное имя'
7) source 'имя окружения'/bin/activate
8) pip install -r requirements.txt
9) python manage.py makemigrations && python manage.py migrate
10) python3 manage.py runserver