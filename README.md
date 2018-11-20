# python_google_cloud_logger

[![CircleCI](https://circleci.com/gh/rai200890/python_google_cloud_logger.svg?style=svg&circle-token=cdb4c95268aa18f240f607082833c94a700f96e9)](https://circleci.com/gh/rai200890/python_google_cloud_logger)
[![PyPI version](https://badge.fury.io/py/google-cloud-logger.svg)](https://badge.fury.io/py/google-cloud-logger)
[![Maintainability](https://api.codeclimate.com/v1/badges/e988f26e1590a6591d96/maintainability)](https://codeclimate.com/github/rai200890/python_google_cloud_logger/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e988f26e1590a6591d96/test_coverage)](https://codeclimate.com/github/rai200890/python_google_cloud_logger/test_coverage)

Python log formatter for Google Cloud according to [v2 specification](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) using [python-json-logger](https://github.com/madzak/python-json-logger) formatter

Inspired by Elixir's [logger_json](https://github.com/Nebo15/logger_json) 

## Instalation

### Pipenv

```
    pipenv install google_cloud_logger 
```

### Pip

```
    pip install google_cloud_logger 
```

## Usage

```python
LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "()": "google_cloud_logger.GoogleCloudFormatter",
            "application_info": {
                "type": "python-application",
                "name": "Example Application"
            },
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        }
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json"
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["json"]
        }
    }
}
import logging

from logging import config

config.dictConfig(LOG_CONFIG) # load log config from dict

logger = logging.getLogger("root") # get root logger instance


logger.info("farofa", extra={"extra": "extra"}) # log message with extra arguments  
```

Example output:

```json
{"timestamp": "2018-11-03T22:05:03.818000Z", "severity": "INFO", "message": "farofa", "labels": {"type": "python-application", "name": "Example Application"}, "metadata": {"userLabels": {"extra": "extra"}}, "sourceLocation": {"file": "<ipython-input-9-8e9384d78e2a>", "line": 1, "function": "<module>"}}
```

## Credits

Thanks [@thulio](https://github.com/thulio), [@robsonpeixoto](https://github.com/robsonpeixoto), [@ramondelemos](https://github.com/ramondelemos)