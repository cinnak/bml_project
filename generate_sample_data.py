import os

import django
from django.core.management import call_command



# Load settings.
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

# Flush current data.
call_command("flush", "--noinput")
print("Flushed existing db.")


# Create a superuser.
os.environ["DJANGO_SUPERUSER_PASSWORD"] = "fake_pw"

cmd = "createsuperuser --username fake_admin"
cmd += " --email fake_email@example.com"
cmd += " --noinput"

cmd_parts = cmd.split()
call_command(*cmd_parts)


# Create sample blogs.
# 在 Python 中，我们通常将所有 import 语句放在文件的顶部。但是 BlogFactory 导入 Blog ，您必须在导入任何模型之前调用 django.setup() 。
# 因此，我们在需要使用它之前导入 BlogFactory 。如果将此 import 语句放在文件顶部，则会出现难以排除故障的错误。

from model_factories import BlogFactory, BlogPostFactory

for _ in range(10):
    BlogFactory.create()

for _ in range(100):
    BlogPostFactory.create()
