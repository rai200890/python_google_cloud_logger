from collections import OrderedDict

import pytest

from google_cloud_logger import GoogleCloudFormatter


@pytest.fixture
def formatter():
    return GoogleCloudFormatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        application_info={"type": "python-application"})


@pytest.fixture
def record(log_record_factory, mocker):
    data = {
        "asctime": "2018-08-30 20:40:57,245",
        "filename": "_internal.py",
        "funcName": "_log",
        "lineno": "88",
        "levelname": "WARNING",
        "message": "farofa",
        "extra_field": "extra"
    }
    record = log_record_factory(**data)
    record.getMessage = mocker.Mock(return_value=data["message"])
    return record


def test_add_fields(formatter, record, mocker):
    log_record = OrderedDict({})
    mocker.patch.object(
        formatter,
        "make_entry",
        return_value=OrderedDict([("timestamp", "2018-08-30 20:40:57Z"),
                                  ("severity", "WARNING"), ("message",
                                                            "farofa"),
                                  ("labels", {
                                      "type": "python-application"
                                  }), ("metadata", {
                                      "userLabels": {}
                                  }),
                                  ("sourceLocation", {
                                      "file": "_internal.py",
                                      "function": "_log",
                                      "line": "88"
                                  })]))
    formatter.add_fields(log_record, record, {})

    assert log_record == formatter.make_entry.return_value


def test_make_entry(formatter, record):
    entry = formatter.make_entry(record)

    assert entry["timestamp"] == "2018-08-30T20:40:57.245000Z"
    assert entry["severity"] == "WARNING"
    assert entry["message"] == "farofa"
    assert entry["metadata"]["userLabels"]["extra_field"] == "extra"
    assert entry["labels"] == {"type": "python-application"}
    assert entry["sourceLocation"] == {
        "file": "_internal.py",
        "function": "_log",
        "line": "88"
    }


def test_make_labels(formatter):
    labels = formatter.make_labels()

    assert labels == {"type": "python-application"}


def test_make_metadata(formatter, record):
    metadata = formatter.make_metadata(record)

    assert metadata["userLabels"]["extra_field"] == "extra"


def test_make_source_location(formatter, record):
    assert formatter.make_source_location(record) == {
        "file": "_internal.py",
        "function": "_log",
        "line": "88"
    }


def test_format_timestamp(formatter):
    assert formatter.format_timestamp(
        "2018-08-30 20:40:57,245") == "2018-08-30T20:40:57.245000Z"


@pytest.mark.parametrize("python_level, expected_level",
                         [("DEFAULT", "NOTSET"), ("CRITICAL", "CRITICAL"),
                          ("ERROR", "ERROR"), ("WARNING", "WARNING"),
                          ("INFO", "INFO"), ("DEBUG", "DEBUG")])
def test_format_severity(formatter, python_level, expected_level):
    assert formatter.format_severity(python_level) == expected_level
