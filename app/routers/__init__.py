from app import config
from app.repositories.activties_record_repository import ActivitiesRecordRepository

auxiliary_repository = ActivitiesRecordRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)
