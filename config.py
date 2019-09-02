import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECERT_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # 配置数据库路径
