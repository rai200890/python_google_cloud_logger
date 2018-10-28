from datetime import datetime

from pythonjsonlogger.jsonlogger import JsonFormatter


class GoogleCloudFormatter(JsonFormatter):
    """
       Log Formatter according to Google Cloud v2 Specification:
       https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
    """

    def __init__(self, *args, **kwargs):
        self.application_info = kwargs.pop("application_info", {})
        super(GoogleCloudFormatter, self).__init__(*args, **kwargs)

    def add_fields(self, log_record, record, _message_dict):
        entry = self.make_entry(record)
        for key, value in entry.items():
            log_record[key] = value

    def make_labels(self, record):
        fields = set(record.__dict__.keys()).difference(
            set(self.reserved_attrs.keys()))
        extra = {key: getattr(record, key) for key in fields}
        return {**self.application_info, **extra}

    def make_entry(self, record):
        return {
            "timestamp": self.format_timestamp(record.asctime),
            "severity": self.format_severity(record.levelname),
            "message": record.getMessage(),
            "metadata": self.make_metadata(record),
            "labels": self.make_labels(record),
            "sourceLocation": self.make_source_location(record)
        }

    def format_timestamp(self, asctime):
        return datetime.strptime(asctime,
                                 "%Y-%m-%d %H:%M:%S,%f").isoformat("T") + "Z"

    def format_severity(self, level_name):
        levels = {
            "DEFAULT": "NOTSET",
            "CRITICAL": "CRITICAL",
            "ERROR": "ERROR",
            "WARNING": "WARNING",
            "INFO": "INFO",
            "DEBUG": "DEBUG"
        }
        return levels[level_name.upper()]

    def make_metadata(self, _record):
        return {"userLabels": None}

    def make_source_location(self, record):
        return {
            "file": record.filename,
            "line": record.lineno,
            "function": record.funcName
        }
