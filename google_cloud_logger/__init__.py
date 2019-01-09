import inspect
import traceback
from datetime import datetime
from io import StringIO

from pythonjsonlogger.jsonlogger import JsonFormatter


class GoogleCloudFormatter(JsonFormatter):
    """
       Log Formatter according to Google Cloud v2 Specification:
       https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
    """

    def __init__(self, *args, **kwargs):
        self.application_info = kwargs.pop("application_info", {})
        super(GoogleCloudFormatter, self).__init__(*args, **kwargs)

    def _get_extra_fields(self, record):
        if hasattr(record, "extra"):
            return record.extra
        attributes = (
            field for field in record.__dict__.keys() if not inspect.ismethod(field)
        )

        fields = set(attributes).difference(set(self.reserved_attrs.keys()))
        return {key: getattr(record, key) for key in fields if key}

    def add_fields(self, log_record, record, _message_dict):
        entry = self.make_entry(record)
        for key, value in entry.items():
            log_record[key] = value

    def make_labels(self):
        return self.application_info

    def make_user_labels(self, record):
        return self._get_extra_fields(record)

    def make_entry(self, record):
        return {
            "timestamp": self.format_timestamp(record.asctime),
            "severity": self.format_severity(record.levelname),
            "message": record.getMessage(),
            "labels": self.make_labels(),
            "metadata": self.make_metadata(record),
            "sourceLocation": self.make_source_location(record),
        }

    def format_timestamp(self, asctime):
        datetime_format = "%Y-%m-%d %H:%M:%S,%f"
        return datetime.strptime(asctime, datetime_format).isoformat("T") + "Z"

    def format_severity(self, level_name):
        levels = {
            "DEFAULT": "NOTSET",
            "CRITICAL": "CRITICAL",
            "ERROR": "ERROR",
            "WARNING": "WARNING",
            "INFO": "INFO",
            "DEBUG": "DEBUG",
        }
        return levels[level_name.upper()]

    def make_exception(self, record):
        with StringIO() as buf:
            exception_info = record.exc_info
            traceback.print_tb(exception_info[2], file=buf)
            return {
                "class": record.exc_info[0],
                "message": record.exc_info[1],
                "traceback": buf.getvalue(),
            }

    def make_metadata(self, record):
        if record.exc_info:
            return {
                "userLabels": self.make_user_labels(record),
                "exception": self.make_exception(record),
            }
        return {"userLabels": self.make_user_labels(record)}

    def make_source_location(self, record):
        return {
            "file": record.filename,
            "line": record.lineno,
            "function": record.funcName,
        }
