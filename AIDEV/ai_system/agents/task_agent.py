from typing import Any, Dict, List
import asyncio
from datetime import datetime
from .base_agent import BaseAgent

class TaskAgent(BaseAgent):
    def __init__(self, name: str, config: Dict[str, Any]):
        super().__init__(name, config)
        self.tasks = {}
        self.running_tasks = set()
        self.task_queue = asyncio.Queue()
        
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process task request"""
        try:
            task_id = input_data.get("task_id")
            task_type = input_data.get("type")
            task_data = input_data.get("data", {})
            
            if task_type == "schedule":
                return await self.schedule_task(task_data)
            elif task_type == "cancel":
                return await self.cancel_task(task_id)
            elif task_type == "status":
                return await self.get_task_status(task_id)
            else:
                return {"error": f"Unknown task type: {task_type}"}
                
        except Exception as e:
            self.logger.error(f"Error processing task: {str(e)}")
            return {"error": str(e)}
    
    async def learn(self, data: Dict[str, Any]) -> None:
        """Learn from task execution results"""
        try:
            self.add_to_memory({
                "type": "task_result",
                "data": data
            })
            
            # Update task success/failure rates
            task_type = data.get("task_type")
            if task_type in self.tasks:
                self.tasks[task_type]["success_rate"] = (
                    self.tasks[task_type].get("success_count", 0) + 
                    (1 if data.get("success") else 0)
                ) / (self.tasks[task_type].get("total_count", 0) + 1)
                
        except Exception as e:
            self.logger.error(f"Error in learning: {str(e)}")
    
    async def schedule_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Schedule a new task"""
        task_id = f"task_{len(self.tasks) + 1}"
        task = {
            "id": task_id,
            "type": task_data.get("type"),
            "data": task_data,
            "status": "scheduled",
            "created_at": datetime.now().isoformat(),
            "scheduled_for": task_data.get("scheduled_for"),
            "success_rate": 0.0,
            "total_count": 0,
            "success_count": 0
        }
        
        self.tasks[task_id] = task
        await self.task_queue.put(task)
        
        return {
            "task_id": task_id,
            "status": "scheduled",
            "scheduled_for": task["scheduled_for"]
        }
    
    async def cancel_task(self, task_id: str) -> Dict[str, Any]:
        """Cancel a scheduled task"""
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = "cancelled"
            return {"status": "cancelled", "task_id": task_id}
        return {"error": f"Task {task_id} not found"}
    
    async def get_task_status(self, task_id: str) -> Dict[str, Any]:
        """Get status of a task"""
        if task_id in self.tasks:
            return self.tasks[task_id]
        return {"error": f"Task {task_id} not found"}
    
    async def execute_task(self, task: Dict[str, Any]) -> None:
        """Execute a task"""
        try:
            self.tasks[task["id"]]["status"] = "running"
            self.running_tasks.add(task["id"])
            
            # Execute task based on type
            if task["type"] == "api_call":
                result = await self.execute_api_call(task["data"])
            elif task["type"] == "data_processing":
                result = await self.process_data(task["data"])
            else:
                result = {"error": f"Unknown task type: {task['type']}"}
            
            # Update task status
            self.tasks[task["id"]].update({
                "status": "completed" if "error" not in result else "failed",
                "result": result,
                "completed_at": datetime.now().isoformat()
            })
            
            # Update statistics
            self.tasks[task["id"]]["total_count"] += 1
            if "error" not in result:
                self.tasks[task["id"]]["success_count"] += 1
            
        except Exception as e:
            self.logger.error(f"Error executing task {task['id']}: {str(e)}")
            self.tasks[task["id"]].update({
                "status": "failed",
                "error": str(e),
                "completed_at": datetime.now().isoformat()
            })
        finally:
            self.running_tasks.remove(task["id"])
    
    async def execute_api_call(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute API call task"""
        # Implement API call logic here
        return {"status": "success", "message": "API call executed"}
    
    async def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute data processing task"""
        # Implement data processing logic here
        return {"status": "success", "message": "Data processed"}
    
    async def start(self) -> None:
        """Start the task agent"""
        await super().start()
        asyncio.create_task(self._process_task_queue())
    
    async def _process_task_queue(self) -> None:
        """Process task queue"""
        while self.status == "running":
            try:
                task = await self.task_queue.get()
                if task["status"] != "cancelled":
                    await self.execute_task(task)
            except Exception as e:
                self.logger.error(f"Error processing task queue: {str(e)}")
            finally:
                self.task_queue.task_done() 