import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MzayhQZJ8rvcbGqz6cjPWetWwQ'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite'))

config = {
    'default': ProductionConfig
}
