from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line

settings.configure(
    # __name__ 指的是当前文件
    ROOT_URLCONF=__name__,
    DEBUG=True,
    # SECRET_KEY 用于帮助确保项目在部署时的安全
    SECRET_KEY="my-secret-key",
)

def index(request):
    return HttpResponse("BlogMaker Lite")

urlpatterns = [
    path("", index)
]

# web server gateway interface
application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()