import os

class Config:
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
    MONGO_DB = os.getenv("MONGO_DB", "flask_db")

    @property
    def mongo_uri(self):
        return (
            f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}"
            f"@{self.MONGO_HOST}:27017/{self.MONGO_DB}?authSource=admin"
        )

config = Config()
