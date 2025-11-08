import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anna_beauty.settings")

app = Celery("anna_beauty")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"🔧 Celery está rodando direitinho, miga! Request: {self.request!r}")

