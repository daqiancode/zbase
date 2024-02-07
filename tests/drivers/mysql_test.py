import pytest
from sqlalchemy import text

from zbase.drivers.mysql import Base,mysqlEngineEnv, mysql_session , Session
from sqlalchemy import Column, Integer, String

# docker run --name mysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id: int = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50))

@mysql_session()
def test_session(mysql:Session=None):
    # Base.metadata.drop_all(bind=mysqlEngineEnv)
    # Base.metadata.create_all(bind=mysqlEngineEnv)
    u = User(name="test1")
    mysql.add(u)
    print(u.id)
    # order by id desc
    r  = mysql.query(User).filter(User.name=="test1").order_by(User.id.desc()).first()
    print(r.id)
    


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])