class Config:
    pass

class DevelopmentConf(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductConf(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://osos:123@localhost:5432/library'


config_options = {"dev": DevelopmentConf,
                  "prd": ProductConf}
