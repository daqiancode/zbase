import pytest
from sqlalchemy import text
import asyncio
pytest_plugins = ('pytest_asyncio',)



from zbase.drivers.async_mysql import mysql_session , AsyncSession,Base

# docker run --name mysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

from sqlalchemy import Column, Integer, String

# docker run --name mysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id: int = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50))

@pytest.mark.asyncio
@mysql_session()
async def test_session(mysql:AsyncSession=None):
    # Base.metadata.drop_all(bind=mysqlEngineEnv)
    # Base.metadata.create_all(bind=mysqlEngineEnv)
    u = User(name="test1")
    print("mysql:", mysql)
    mysql.add(u)
    print(u.id)
    # order by id desc
    r  = await mysql.execute(text("select * from user order by id desc"))
    print("all:",r.fetchall())
    


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])