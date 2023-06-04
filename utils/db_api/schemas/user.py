from utils.db_api.DB import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Float


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    age = Column(String(3))
    referal_id = Column(BigInteger)
    balance = Column(Float)
    photo = Column(String(200))


    query: sql.select