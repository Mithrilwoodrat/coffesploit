# -*- coding: utf-8 -*-
from flask import Flask
from celery import Celery
from coffesploit.core.coffesplot import Coffesploit


csfserver = Flask(__name__)
csfserver.config.from_object('config')
main = Coffesploit()


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            print('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(self.request))
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

csfserver.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379')

celery = make_celery(csfserver)


@celery.task
def task_run(plugin_name, status):
    print plugin_name, status
    main.use(plugin_name)
    main.pluginmanager.current_plugin.run(status)
    return main.pluginmanager.current_plugin.result()


from server import views, models
