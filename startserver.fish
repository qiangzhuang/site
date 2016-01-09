#!/usr/local/bin/fish
uwsgi --shared-socket 0.0.0.0:443 --https =0,ssl/foobar.crt,ssl/foobar.key,HIGH --master --processes 256 --gevent 1000 -w run:app --uid www-data --gid www-data --cheaper 4 --cheaper-initial 4 --cheaper-step 2 --check-static /root/flaskstuff/mysite/911911/app/static/ --offload-threads 4
