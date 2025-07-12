import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class ChatHistory:
    def __init__(self, storage_dir: str = "data/chat_history"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.current_file = None
        self.current_date = None
        self._initialize_storage()

    def _initialize_storage(self):
        """Initialize storage directory and create necessary files."""
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self._update_current_file()

    def _update_current_file(self):
        """Update the current file based on the current date."""
        today = datetime.now().date()
        if self.current_date != today:
            self.current_date = today
            self.current_file = self.storage_dir / f"chat_history_{today.isoformat()}.json"
            if not self.current_file.exists():
                self._create_new_history_file()

    def _create_new_history_file(self):
        """Create a new history file for the current date."""
        initial_data = {
            "date": self.current_date.isoformat(),
            "chats": [],
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "total_messages": 0
            }
        }
        with open(self.current_file, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)

    def add_message(self, user_id: str, message: str, response: str, metadata: Optional[Dict] = None):
        """Add a new message to the chat history."""
        self._update_current_file()
        
        try:
            with open(self.current_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            chat_entry = {
                "timestamp": datetime.now().isoformat(),
                "user_id": user_id,
                "message": message,
                "response": response,
                "metadata": metadata or {}
            }
            
            data["chats"].append(chat_entry)
            data["metadata"]["total_messages"] = len(data["chats"])
            data["metadata"]["last_updated"] = datetime.now().isoformat()
            
            with open(self.current_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            logger.error(f"Error adding message to chat history: {str(e)}")
            raise

    def get_chat_history(self, date: Optional[datetime] = None) -> List[Dict]:
        """Get chat history for a specific date."""
        if date is None:
            date = datetime.now()
        
        history_file = self.storage_dir / f"chat_history_{date.date().isoformat()}.json"
        
        if not history_file.exists():
            return []
            
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data["chats"]
        except Exception as e:
            logger.error(f"Error reading chat history: {str(e)}")
            return []

    def get_user_history(self, user_id: str, days: int = 7) -> List[Dict]:
        """Get chat history for a specific user over a number of days."""
        all_chats = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        current_date = start_date
        while current_date <= end_date:
            history_file = self.storage_dir / f"chat_history_{current_date.date().isoformat()}.json"
            if history_file.exists():
                try:
                    with open(history_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    user_chats = [chat for chat in data["chats"] if chat["user_id"] == user_id]
                    all_chats.extend(user_chats)
                except Exception as e:
                    logger.error(f"Error reading user history: {str(e)}")
            current_date += timedelta(days=1)
            
        return sorted(all_chats, key=lambda x: x["timestamp"])

    def cleanup_old_history(self, days_to_keep: int = 30):
        """Clean up chat history files older than specified days."""
        cutoff_date = datetime.now() - timedelta(days=days_to_keep)
        
        for history_file in self.storage_dir.glob("chat_history_*.json"):
            try:
                file_date = datetime.strptime(history_file.stem.split('_')[2], "%Y-%m-%d").date()
                if file_date < cutoff_date.date():
                    history_file.unlink()
                    logger.info(f"Deleted old history file: {history_file}")
            except Exception as e:
                logger.error(f"Error cleaning up history file {history_file}: {str(e)}")

    def get_statistics(self, date: Optional[datetime] = None) -> Dict:
        """Get statistics for chat history on a specific date."""
        if date is None:
            date = datetime.now()
            
        history_file = self.storage_dir / f"chat_history_{date.date().isoformat()}.json"
        
        if not history_file.exists():
            return {
                "total_messages": 0,
                "unique_users": 0,
                "date": date.date().isoformat()
            }
            
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            unique_users = len(set(chat["user_id"] for chat in data["chats"]))
            
            return {
                "total_messages": data["metadata"]["total_messages"],
                "unique_users": unique_users,
                "date": date.date().isoformat(),
                "last_updated": data["metadata"]["last_updated"]
            }
        except Exception as e:
            logger.error(f"Error getting statistics: {str(e)}")
            return {
                "total_messages": 0,
                "unique_users": 0,
                "date": date.date().isoformat(),
                "error": str(e)
            } 