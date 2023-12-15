import pytest
import time


@pytest.fixture()
def log_time():
    t0 = time.localtime()
    t0_fmt = time.strftime("%H:%M:%S", t0)
    print(f"\nTEST STARTED AT: {t0_fmt}")
    yield
    t1 = time.localtime()
    t1_fmt = time.strftime("%H:%M:%S", t1)
    print(f"\nTEST FINISHED AT: {t1_fmt}")
