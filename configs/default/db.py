import os

if os.getenv("DJANGO_ENV") != "ci":
    # mysql 设置
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.mysql',
            "NAME": "sspanel",
            "PASSWORD": os.getenv("MYSQL_PASSWORD", "lys!QAZ1qaz"),
            "HOST": os.getenv("MYSQL_HOST", "107.148.250.132"),
            "USER": os.getenv("MYSQL_USER", "root"),
            "PORT": "33306",
            "OPTIONS": {
                "autocommit": True,
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
                "charset": "utf8mb4",
            },
        }
    }
