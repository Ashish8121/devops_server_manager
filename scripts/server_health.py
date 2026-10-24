
from pathlib import Path
import psutil
import os
import logging


def memory():
    try:
        memory = psutil.virtual_memory()
        return memory.percent
    except Exception as e:
        logging.error(f"Memory check failed: {e}")
        return None


def cpu():
    try:
        cpu_count = psutil.cpu_count(logical=True)

        if cpu_count is None:
            raise RuntimeError("Unable to determine CPU count")

        load_avg_1min = os.getloadavg()[0]
        return cpu_count, load_avg_1min

    except Exception as e:
        logging.error(f"CPU check failed: {e}")
        return None


def disk():
    try:
        disk_usage = psutil.disk_usage("/").percent
        return disk_usage
    except Exception as e:
        logging.error(f"Disk check failed: {e}")
        return None


# Logging configuration
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "server_health.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    status = "Healthy"

    # Collect metrics
    memory_usage = memory()
    disk_usage = disk()
    cpu_result = cpu()

    # Memory check
    if memory_usage is None:
        status = "CRITICAL"
        logging.critical("Memory check failed")

    elif memory_usage >= 90:
        status = "CRITICAL"
        logging.critical(f"Memory usage is CRITICAL: {memory_usage:.1f}%")

    elif memory_usage >= 80:
        status = "WARNING"
        logging.warning(f"Memory usage is WARNING: {memory_usage:.1f}%")

    # CPU check
    if cpu_result is None:
        status = "CRITICAL"
        logging.critical("CPU metrics unavailable")

        cpu_count = None
        load_avg = None

    else:
        cpu_count, load_avg = cpu_result

        if load_avg > cpu_count and status != "CRITICAL":
            status = "WARNING"
            logging.warning(f"CPU load average is high: {load_avg:.1f}")

    # Disk check
    if disk_usage is None:
        status = "CRITICAL"
        logging.critical("Disk check failed")

    elif disk_usage >= 90:
        status = "CRITICAL"
        logging.critical(f"Disk usage is CRITICAL: {disk_usage:.1f}%")

    elif disk_usage >= 80:
        if status != "CRITICAL":
            status = "WARNING"
        logging.warning(f"Disk usage is WARNING: {disk_usage:.1f}%")

    # Log and display CPU metrics
    if cpu_result is None:
        logging.error("CPU metrics unavailable")
        print("CPU metrics: Unavailable")
    else:
        logging.info(f"CPU load average: {load_avg:.1f}")
        logging.info(f"CPU count: {cpu_count}")

        print(f"CPU load average: {load_avg:.1f}")
        print(f"CPU count: {cpu_count}")

    # Log and display memory and disk metrics
    logging.info(f"Memory usage: {memory_usage}")
    logging.info(f"Disk usage: {disk_usage}")

    print(f"Memory usage: {memory_usage if memory_usage is not None else 'Unavailable'}")
    print(f"Disk usage: {disk_usage if disk_usage is not None else 'Unavailable'}")
    print(f"Overall status: {status}")

    # Log overall status
    if status == "CRITICAL":
        logging.critical(f"Overall health status: {status}")
    elif status == "WARNING":
        logging.warning(f"Overall health status: {status}")
    else:
        logging.info(f"Overall health status: {status}")


if __name__ == "__main__":
    main()