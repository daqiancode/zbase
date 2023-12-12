import pytest
from sqlalchemy import text

from zbase.drivers.mysql import yieldSession,Base,mysqlEngineEnv
from sqlalchemy import Column, Integer, String

# docker run --name mysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

class User(Base):
    __tablename__ = 'user'
    id: int = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50))

def test_session():
    Base.metadata.drop_all(bind=mysqlEngineEnv)
    Base.metadata.create_all(bind=mysqlEngineEnv)
    with yieldSession() as session:
        u = User(name="test")
        session.add(u)
        session.flush()
        r = session.execute(text("select * from user")).all()
        assert len(r) == 1
    assert u.id ==1


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])