import os
import pymysql
from configs.default import *  # noqa

pymysql.version_info=(1,3,13,"final",0)
pymysql.install_as_MySQLdb()

django_env = os.getenv("DJANGO_ENV", "development")
if django_env == "production":
    from configs.production import *  # noqa
else:
    from configs.development import *  # noqa
