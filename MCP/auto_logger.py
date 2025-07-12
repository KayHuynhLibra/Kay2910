#!/usr/bin/env python3
"""
Auto Logger - Tự động log mọi tương tác và lệnh chạy
"""

import os
import sys
import subprocess
import datetime
from typing import List
from session_logger import init_session_logger, log_current_interaction, log_current_command, log_current_error, log_current_fix, finalize_current_session

class AutoLogger:
    def __init__(self, session_name="auto_session"):
        self.logger = init_session_logger(session_name)
        self.session_start = datetime.datetime.now()
        
    def log_interaction(self, user_message: str, assistant_response: str):
        """Log tương tác giữa user và assistant"""
        log_current_interaction(user_message, assistant_response)
        
    def run_command(self, command: str, capture_output=True):
        """Chạy lệnh và tự động log kết quả"""
        print(f"Running: {command}")
        
        try:
            if capture_output:
                result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
                output = result.stdout
                error_output = result.stderr
                exit_code = result.returncode
                
                # Log command with combined output
                full_output = output
                if error_output:
                    full_output += f"\nError Output:\n{error_output}"
                
                log_current_command(command, full_output, exit_code)
                
                # Print output
                if output:
                    print(output)
                if error_output:
                    print(f"Error: {error_output}")
                    
                return result
            else:
                # Run without capturing output (for interactive commands)
                result = subprocess.run(command, shell=True)
                log_current_command(command, "[Interactive command - no output captured]", result.returncode)
                return result
                
        except Exception as e:
            error_msg = str(e)
            log_current_error("Command Execution", error_msg, f"Command: {command}")
            print(f"Error running command: {error_msg}")
            return None
            
    def log_error(self, error_type: str, error_message: str, context: str = ""):
        """Log lỗi"""
        log_current_error(error_type, error_message, context)
        
    def log_fix(self, problem: str, solution: str, files_modified: List[str] = None):
        """Log cách sửa"""
        log_current_fix(problem, solution, files_modified)
        
    def finalize(self):
        """Kết thúc session"""
        self.logger.finalize_session()
        
    def get_session_info(self):
        """Lấy thông tin session"""
        return {
            "session_id": self.logger.session_id,
            "start_time": self.session_start.isoformat(),
            "duration": str(datetime.datetime.now() - self.session_start),
            "log_directory": self.logger.log_dir
        }

# Global auto logger instance
auto_logger = None

def init_auto_logger(session_name="auto_session"):
    """Khởi tạo auto logger"""
    global auto_logger
    auto_logger = AutoLogger(session_name)
    return auto_logger

def run_and_log(command: str, capture_output=True):
    """Chạy lệnh và log kết quả"""
    global auto_logger
    if auto_logger:
        return auto_logger.run_command(command, capture_output)
    else:
        # Fallback to normal subprocess if no logger
        return subprocess.run(command, shell=True, capture_output=capture_output, text=True)

def log_current_session_interaction(user_message: str, assistant_response: str):
    """Log tương tác hiện tại"""
    global auto_logger
    if auto_logger:
        auto_logger.log_interaction(user_message, assistant_response)

def log_current_session_error(error_type: str, error_message: str, context: str = ""):
    """Log lỗi hiện tại"""
    global auto_logger
    if auto_logger:
        auto_logger.log_error(error_type, error_message, context)

def log_current_session_fix(problem: str, solution: str, files_modified: List[str] = None):
    """Log cách sửa hiện tại"""
    global auto_logger
    if auto_logger:
        auto_logger.log_fix(problem, solution, files_modified)

def finalize_current_session():
    """Kết thúc session hiện tại"""
    global auto_logger
    if auto_logger:
        auto_logger.finalize()

# Khởi tạo auto logger cho session hiện tại
init_auto_logger("ai_2025_mcp_session")

if __name__ == "__main__":
    # Test auto logger
    logger = init_auto_logger("test_auto_session")
    
    # Log một số tương tác
    logger.log_interaction("Tạo dữ liệu mẫu", "Đã tạo thành công các file dữ liệu")
    logger.log_interaction("Chạy thí nghiệm", "Đang chạy các thí nghiệm AI")
    
    # Chạy một số lệnh
    logger.run_command("python --version")
    logger.run_command("dir")
    
    # Log lỗi và cách sửa
    logger.log_error("JSON Serialization", "Object of type Int64DType is not JSON serializable")
    logger.log_fix("JSON Serialization Error", "Thêm hàm _make_serializable", ["deploy_experiments.py"])
    
    # Kết thúc
    logger.finalize()
    
    print("Auto logger test completed!") 