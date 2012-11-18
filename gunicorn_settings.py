import multiprocessing
import os

bind = "127.0.0.1:8080"
timeout = 120
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "/var/log/gunicorn/redwire.log"
errorlog = "/var/log/gunicorn/redwire-error.log"
