import pytest
from sqlalchemy import text

from zbase.drivers.postgre import Base, postgre_session , Session
from sqlalchemy import Column, Integer, String


# docker run --name mysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id: int = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50))

@postgre_session()
def test_session(postgre:Session=None):
    # Base.metadata.drop_all(bind=mysqlEngineEnv)
    # Base.metadata.create_all(bind=mysqlEngineEnv)

    r  = postgre.execute(text("select count(*) from people")).all()
    print(r)
    


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])