from pathlib import Path
import os

# Base directory for chat history storage
CHAT_HISTORY_DIR = Path(os.getenv("CHAT_HISTORY_DIR", "data/chat_history"))

# Backup directory
BACKUP_DIR = CHAT_HISTORY_DIR / "backups"

# Report directory
REPORT_DIR = CHAT_HISTORY_DIR / "reports"

# Default retention period in days
DEFAULT_RETENTION_DAYS = 30

# Maximum number of messages per file
MAX_MESSAGES_PER_FILE = 1000

# File format for chat history
HISTORY_FILE_FORMAT = "%Y-%m-%d.json"

# Backup file format
BACKUP_FILE_FORMAT = "%Y-%m-%d-backup.zip"

# Report file format
REPORT_FILE_FORMAT = "%Y-%m-%d-report.json"

# Default schedule times
DEFAULT_CLEANUP_TIME = "00:00"  # Midnight
DEFAULT_BACKUP_TIME = "01:00"   # 1 AM
DEFAULT_REPORT_TIME = "08:00"   # 8 AM

# Create necessary directories
CHAT_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Logging configuration
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"
LOG_FILE = CHAT_HISTORY_DIR / "chat_history.log"

# Compression settings for backups
COMPRESSION_LEVEL = 9  # Maximum compression
COMPRESSION_METHOD = "zip"

# Report template settings
REPORT_TEMPLATE = {
    "total_messages": 0,
    "unique_users": 0,
    "average_messages_per_user": 0,
    "busiest_hour": None,
    "message_types": {},
    "user_activity": {}
}

# Security settings
ENCRYPT_BACKUPS = True
ENCRYPTION_KEY = os.getenv("CHAT_HISTORY_ENCRYPTION_KEY", None)

# Rate limiting
MAX_REQUESTS_PER_MINUTE = 60
MAX_REQUESTS_PER_HOUR = 1000

# Cache settings
CACHE_ENABLED = True
CACHE_TTL = 300  # 5 minutes
MAX_CACHE_SIZE = 1000  # Maximum number of cached items

# Error handling
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds

# Monitoring settings
ENABLE_METRICS = True
METRICS_PORT = 9090
METRICS_PATH = "/metrics" 