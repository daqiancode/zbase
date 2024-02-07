from zbase.drivers.async_redis import newRedisEnv
import pytest

@pytest.mark.asyncio
async def test_get_set():
    redis = newRedisEnv()
    await redis.set("test", "hello")
    r = await redis.get("test")
    assert r.decode() == "hello"
