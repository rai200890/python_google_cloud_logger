import pytest


class MockLogRecord(object):
    def __init__(self, args={}, **kwargs):
        merged = {**args, **kwargs}
        for field, value in merged.items():
            setattr(self, field, value)


@pytest.fixture
def log_record_factory():
    def build_log_record(**args):
        return MockLogRecord(**args)

    return build_log_record
