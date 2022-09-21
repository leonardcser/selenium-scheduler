# Selenium Scheduler

- [Selenium Scheduler](#selenium-scheduler)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Install](#install)
      - [Advanced](#advanced)
    - [Status](#status)
    - [Logs](#logs)
    - [Uninstall](#uninstall)
  - [Example](#example)

## Installation

```sh
pip install git+https://github.com/leonardcser/selenium-scheduler
```

## Usage

### Install

```sh
selenium_scheduler install -e main.py
```

A `requirements.txt` file must be in the root of your project
The `main.py` defines the entry-point for the scheduler

#### Advanced

```sh
selenium_scheduler install -e main.py -r requirements/requirements.txt -m "module1,module2" -env .env
```

### Status

```sh
selenium_scheduler status
```

### Logs

```sh
selenium_scheduler logs
```

### Uninstall

```sh
selenium_scheduler uninstall
```

## Example

See https://github.com/leonardcser/epfl-scheduler
