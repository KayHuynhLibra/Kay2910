import schedule
import time
import threading
from datetime import datetime, timedelta
import logging
from typing import Callable, List, Dict
from .chat_history import ChatHistory

logger = logging.getLogger(__name__)

class ChatScheduler:
    def __init__(self, chat_history: ChatHistory):
        self.chat_history = chat_history
        self.scheduled_tasks: List[Dict] = []
        self.running = False
        self.thread = None

    def start(self):
        """Start the scheduler in a separate thread."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_scheduler)
            self.thread.daemon = True
            self.thread.start()
            logger.info("Chat scheduler started")

    def stop(self):
        """Stop the scheduler."""
        self.running = False
        if self.thread:
            self.thread.join()
            logger.info("Chat scheduler stopped")

    def _run_scheduler(self):
        """Run the scheduler loop."""
        while self.running:
            schedule.run_pending()
            time.sleep(1)

    def schedule_daily_cleanup(self, hour: int = 0, minute: int = 0):
        """Schedule daily cleanup of old chat history."""
        def cleanup_task():
            logger.info("Running daily chat history cleanup")
            self.chat_history.cleanup_old_history()
            
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(cleanup_task)
        self.scheduled_tasks.append({
            "name": "daily_cleanup",
            "schedule": f"Daily at {hour:02d}:{minute:02d}",
            "task": cleanup_task
        })
        logger.info(f"Scheduled daily cleanup for {hour:02d}:{minute:02d}")

    def schedule_daily_backup(self, hour: int = 1, minute: int = 0):
        """Schedule daily backup of chat history."""
        def backup_task():
            logger.info("Running daily chat history backup")
            # Implement backup logic here
            pass
            
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(backup_task)
        self.scheduled_tasks.append({
            "name": "daily_backup",
            "schedule": f"Daily at {hour:02d}:{minute:02d}",
            "task": backup_task
        })
        logger.info(f"Scheduled daily backup for {hour:02d}:{minute:02d}")

    def schedule_daily_report(self, hour: int = 8, minute: int = 0):
        """Schedule daily report generation."""
        def report_task():
            logger.info("Generating daily chat report")
            yesterday = datetime.now() - timedelta(days=1)
            stats = self.chat_history.get_statistics(yesterday)
            # Implement report generation and distribution logic here
            pass
            
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(report_task)
        self.scheduled_tasks.append({
            "name": "daily_report",
            "schedule": f"Daily at {hour:02d}:{minute:02d}",
            "task": report_task
        })
        logger.info(f"Scheduled daily report for {hour:02d}:{minute:02d}")

    def add_custom_task(self, name: str, schedule_time: str, task: Callable):
        """Add a custom scheduled task."""
        schedule.every().day.at(schedule_time).do(task)
        self.scheduled_tasks.append({
            "name": name,
            "schedule": f"Daily at {schedule_time}",
            "task": task
        })
        logger.info(f"Added custom task '{name}' scheduled for {schedule_time}")

    def get_scheduled_tasks(self) -> List[Dict]:
        """Get list of all scheduled tasks."""
        return [
            {
                "name": task["name"],
                "schedule": task["schedule"],
                "next_run": schedule.next_run(task["task"]).isoformat() if schedule.next_run(task["task"]) else None
            }
            for task in self.scheduled_tasks
        ]

    def remove_task(self, task_name: str):
        """Remove a scheduled task by name."""
        for task in self.scheduled_tasks:
            if task["name"] == task_name:
                schedule.clear(task["task"])
                self.scheduled_tasks.remove(task)
                logger.info(f"Removed scheduled task: {task_name}")
                return
        logger.warning(f"Task not found: {task_name}") 