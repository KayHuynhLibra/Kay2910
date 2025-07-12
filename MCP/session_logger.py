#!/usr/bin/env python3
"""
Session Logger - Lưu lại toàn bộ lịch sử giao tiếp và lệnh chạy
"""

import os
import json
import datetime
from typing import Dict, List, Any
import subprocess
import sys

class SessionLogger:
    def __init__(self, session_name="ai_session"):
        self.session_name = session_name
        self.session_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_dir = f"historylog/sessions/{self.session_id}"
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Khởi tạo session log
        self.session_data = {
            "session_id": self.session_id,
            "start_time": datetime.datetime.now().isoformat(),
            "user_os": os.name,
            "python_version": sys.version,
            "interactions": [],
            "commands": [],
            "errors": [],
            "fixes": []
        }
        
        # Lưu session info
        self.save_session_info()
        
    def log_interaction(self, user_message: str, assistant_response: str, 
                       interaction_type: str = "chat"):
        """Lưu lại tương tác giữa user và assistant"""
        interaction = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": interaction_type,
            "user_message": user_message,
            "assistant_response": assistant_response
        }
        self.session_data["interactions"].append(interaction)
        self.save_session_data()
        
    def log_command(self, command: str, output: str, exit_code: int = 0, 
                   error: str = None):
        """Lưu lại lệnh đã chạy và kết quả"""
        cmd_log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "command": command,
            "output": output,
            "exit_code": exit_code,
            "error": error
        }
        self.session_data["commands"].append(cmd_log)
        self.save_session_data()
        
    def log_error(self, error_type: str, error_message: str, 
                  context: str = "", fix_attempt: str = ""):
        """Lưu lại lỗi và cách sửa"""
        error_log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "error_type": error_type,
            "error_message": error_message,
            "context": context,
            "fix_attempt": fix_attempt
        }
        self.session_data["errors"].append(error_log)
        self.save_session_data()
        
    def log_fix(self, problem: str, solution: str, 
                files_modified: List[str] = None):
        """Lưu lại cách sửa lỗi"""
        fix_log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "problem": problem,
            "solution": solution,
            "files_modified": files_modified or []
        }
        self.session_data["fixes"].append(fix_log)
        self.save_session_data()
        
    def save_session_info(self):
        """Lưu thông tin session"""
        info_file = f"{self.log_dir}/session_info.json"
        with open(info_file, 'w', encoding='utf-8') as f:
            json.dump(self.session_data, f, ensure_ascii=False, indent=2)
            
    def save_session_data(self):
        """Lưu toàn bộ dữ liệu session"""
        data_file = f"{self.log_dir}/session_data.json"
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(self.session_data, f, ensure_ascii=False, indent=2)
            
    def create_summary(self):
        """Tạo báo cáo tổng hợp session"""
        summary = {
            "session_id": self.session_id,
            "duration": self.get_session_duration(),
            "total_interactions": len(self.session_data["interactions"]),
            "total_commands": len(self.session_data["commands"]),
            "total_errors": len(self.session_data["errors"]),
            "total_fixes": len(self.session_data["fixes"]),
            "successful_commands": len([c for c in self.session_data["commands"] if c["exit_code"] == 0]),
            "failed_commands": len([c for c in self.session_data["commands"] if c["exit_code"] != 0])
        }
        
        summary_file = f"{self.log_dir}/session_summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
            
        return summary
        
    def get_session_duration(self):
        """Tính thời gian session"""
        start_time = datetime.datetime.fromisoformat(self.session_data["start_time"])
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        return str(duration)
        
    def create_readme(self):
        """Tạo file README cho session"""
        readme_content = f"""# Session Log: {self.session_id}

## Thông tin Session
- **Thời gian bắt đầu**: {self.session_data['start_time']}
- **Hệ điều hành**: {self.session_data['user_os']}
- **Python version**: {self.session_data['python_version']}

## Tổng quan
- Tổng số tương tác: {len(self.session_data['interactions'])}
- Tổng số lệnh chạy: {len(self.session_data['commands'])}
- Tổng số lỗi: {len(self.session_data['errors'])}
- Tổng số lần sửa: {len(self.session_data['fixes'])}

## Cấu trúc thư mục
```
{self.log_dir}/
├── session_info.json      # Thông tin session
├── session_data.json      # Dữ liệu chi tiết
├── session_summary.json   # Báo cáo tổng hợp
├── README.md             # File này
└── commands/             # Log từng lệnh riêng biệt
```

## Các file quan trọng
- `session_data.json`: Chứa toàn bộ lịch sử tương tác, lệnh, lỗi
- `session_summary.json`: Báo cáo tổng hợp session
- `commands/`: Thư mục chứa output chi tiết của từng lệnh

## Cách sử dụng
1. Xem `session_summary.json` để hiểu tổng quan
2. Xem `session_data.json` để xem chi tiết từng bước
3. Xem thư mục `commands/` để xem output của từng lệnh
"""
        
        readme_file = f"{self.log_dir}/README.md"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
            
    def log_command_output(self, command: str, output: str):
        """Lưu output của lệnh vào file riêng"""
        cmd_dir = f"{self.log_dir}/commands"
        os.makedirs(cmd_dir, exist_ok=True)
        
        # Tạo tên file từ command
        safe_cmd = "".join(c for c in command if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_cmd = safe_cmd.replace(' ', '_')[:50]  # Giới hạn độ dài
        timestamp = datetime.datetime.now().strftime("%H%M%S")
        filename = f"{cmd_dir}/{timestamp}_{safe_cmd}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Command: {command}\n")
            f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
            f.write("="*50 + "\n")
            f.write(output)
            
    def finalize_session(self):
        """Kết thúc session và tạo báo cáo cuối"""
        self.session_data["end_time"] = datetime.datetime.now().isoformat()
        self.create_summary()
        self.create_readme()
        self.save_session_data()
        
        print(f"\n=== Session Logged ===")
        print(f"Session ID: {self.session_id}")
        print(f"Log directory: {self.log_dir}")
        print(f"Total interactions: {len(self.session_data['interactions'])}")
        print(f"Total commands: {len(self.session_data['commands'])}")
        print(f"Total errors: {len(self.session_data['errors'])}")
        print(f"Total fixes: {len(self.session_data['fixes'])}")

# Global session logger instance
session_logger = None

def init_session_logger(session_name="ai_session"):
    """Khởi tạo session logger"""
    global session_logger
    session_logger = SessionLogger(session_name)
    return session_logger

def log_current_interaction(user_message: str, assistant_response: str):
    """Log tương tác hiện tại"""
    global session_logger
    if session_logger:
        session_logger.log_interaction(user_message, assistant_response)

def log_current_command(command: str, output: str, exit_code: int = 0):
    """Log lệnh hiện tại"""
    global session_logger
    if session_logger:
        session_logger.log_command(command, output, exit_code)
        session_logger.log_command_output(command, output)

def log_current_error(error_type: str, error_message: str, context: str = ""):
    """Log lỗi hiện tại"""
    global session_logger
    if session_logger:
        session_logger.log_error(error_type, error_message, context)

def log_current_fix(problem: str, solution: str, files_modified: List[str] = None):
    """Log cách sửa hiện tại"""
    global session_logger
    if session_logger:
        session_logger.log_fix(problem, solution, files_modified)

def finalize_current_session():
    """Kết thúc session hiện tại"""
    global session_logger
    if session_logger:
        session_logger.finalize_session()

if __name__ == "__main__":
    # Test session logger
    logger = init_session_logger("test_session")
    
    # Log một số tương tác mẫu
    logger.log_interaction("Tạo dữ liệu mẫu", "Đã tạo thành công các file dữ liệu")
    logger.log_interaction("Chạy thí nghiệm", "Đang chạy các thí nghiệm AI")
    
    # Log một số lệnh mẫu
    logger.log_command("python create_sample_data.py", "Created: data/raw\nCreated: datasets/text/...")
    logger.log_command("python deploy_experiments.py", "Running experiments...", 0)
    
    # Log một số lỗi và cách sửa
    logger.log_error("JSON Serialization", "Object of type Int64DType is not JSON serializable", 
                    "Khi lưu kết quả thí nghiệm")
    logger.log_fix("JSON Serialization Error", "Thêm hàm _make_serializable để chuyển pandas dtype thành string",
                  ["deploy_experiments.py"])
    
    # Kết thúc session
    logger.finalize_session() 