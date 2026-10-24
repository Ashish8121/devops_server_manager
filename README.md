# DevOps Server Health Monitor

A Python-based server monitoring tool that checks CPU load, memory usage, and disk usage, logs health metrics, handles errors, and runs automatically using cron.

## Features

- CPU load and logical CPU count monitoring
- Memory usage monitoring
- Disk usage monitoring
- Health status reporting: Healthy, Warning, and Critical
- Error handling for failed metric checks
- Timestamped logging
- Automated execution every five minutes using cron
- Log rotation with compression and retention of seven rotated logs

## Technologies Used

- Python
- psutil
- Linux (Ubuntu)
- Bash / Cron
- Git and GitHub
- logrotate

## Project Structure

```text
devops-server-manager/
├── config/
├── scripts/
│   └── server_health.py
├── logs/                 # Generated logs; not tracked by Git
├── venv/                 # Python virtual environment; not tracked by Git
├── learning_path.txt
├── .gitignore
└── README.md
```

## Setup

Clone the repository and enter the project directory:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd devops-server-manager
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependency:

```bash
pip install psutil
```

## Run the Monitor

```bash
python scripts/server_health.py
```

The script writes monitoring results to `logs/server_health.log`.

## Automation

Cron can execute the script every five minutes:

```cron
*/5 * * * * cd /home/ashish/devops-server-manager && /home/ashish/devops-server-manager/venv/bin/python /home/ashish/devops-server-manager/scripts/server_health.py
```

Update the paths if you install the project in a different directory.

## Log Rotation

The project uses Linux `logrotate` to rotate logs daily, compress old logs, and retain up to seven rotated logs.

## Purpose

This project demonstrates practical Linux administration, Python scripting, monitoring, scheduled automation, error handling, and log management.
