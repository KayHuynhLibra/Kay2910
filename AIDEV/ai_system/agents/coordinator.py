from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent
from .chat_agent import ChatAgent
from .task_agent import TaskAgent
import asyncio
import json

class Coordinator(BaseAgent):
    def __init__(self, name: str, config: Dict[str, Any]):
        super().__init__(name, config)
        self.agents = {}
        self.agent_types = {
            "chat": ChatAgent,
            "task": TaskAgent
        }
        
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process request and delegate to appropriate agent"""
        try:
            request_type = input_data.get("type")
            agent_type = input_data.get("agent_type")
            agent_id = input_data.get("agent_id")
            
            if request_type == "create_agent":
                return await self.create_agent(agent_type, input_data.get("config", {}))
            elif request_type == "delete_agent":
                return await self.delete_agent(agent_id)
            elif request_type == "get_agent":
                return await self.get_agent_info(agent_id)
            elif request_type == "list_agents":
                return await self.list_agents()
            elif request_type == "delegate":
                return await self.delegate_to_agent(agent_id, input_data.get("data", {}))
            else:
                return {"error": f"Unknown request type: {request_type}"}
                
        except Exception as e:
            self.logger.error(f"Error processing request: {str(e)}")
            return {"error": str(e)}
    
    async def learn(self, data: Dict[str, Any]) -> None:
        """Learn from agent interactions"""
        try:
            self.add_to_memory({
                "type": "agent_interaction",
                "data": data
            })
            
            # Update agent performance metrics
            agent_id = data.get("agent_id")
            if agent_id in self.agents:
                agent = self.agents[agent_id]
                agent.add_to_memory(data)
                
        except Exception as e:
            self.logger.error(f"Error in learning: {str(e)}")
    
    async def create_agent(self, agent_type: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new agent"""
        if agent_type not in self.agent_types:
            return {"error": f"Unknown agent type: {agent_type}"}
            
        agent_id = f"{agent_type}_{len(self.agents) + 1}"
        agent = self.agent_types[agent_type](agent_id, config)
        
        self.agents[agent_id] = agent
        await agent.start()
        
        return {
            "agent_id": agent_id,
            "type": agent_type,
            "status": "created"
        }
    
    async def delete_agent(self, agent_id: str) -> Dict[str, Any]:
        """Delete an agent"""
        if agent_id not in self.agents:
            return {"error": f"Agent {agent_id} not found"}
            
        agent = self.agents[agent_id]
        await agent.stop()
        del self.agents[agent_id]
        
        return {
            "agent_id": agent_id,
            "status": "deleted"
        }
    
    async def get_agent_info(self, agent_id: str) -> Dict[str, Any]:
        """Get information about an agent"""
        if agent_id not in self.agents:
            return {"error": f"Agent {agent_id} not found"}
            
        agent = self.agents[agent_id]
        return {
            "agent_id": agent_id,
            "type": agent.__class__.__name__,
            "status": agent.get_status()
        }
    
    async def list_agents(self) -> Dict[str, Any]:
        """List all agents"""
        return {
            "agents": [
                {
                    "agent_id": agent_id,
                    "type": agent.__class__.__name__,
                    "status": agent.get_status()
                }
                for agent_id, agent in self.agents.items()
            ]
        }
    
    async def delegate_to_agent(self, agent_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Delegate task to specific agent"""
        if agent_id not in self.agents:
            return {"error": f"Agent {agent_id} not found"}
            
        agent = self.agents[agent_id]
        result = await agent.process(data)
        
        # Learn from the interaction
        await self.learn({
            "agent_id": agent_id,
            "input": data,
            "output": result
        })
        
        return result
    
    async def start(self) -> None:
        """Start the coordinator"""
        await super().start()
        self.logger.info("Coordinator started")
    
    async def stop(self) -> None:
        """Stop the coordinator and all agents"""
        for agent_id, agent in self.agents.items():
            await agent.stop()
        await super().stop()
        self.logger.info("Coordinator stopped")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get overall system status"""
        return {
            "coordinator": self.get_status(),
            "agents": {
                agent_id: agent.get_status()
                for agent_id, agent in self.agents.items()
            },
            "total_agents": len(self.agents),
            "agent_types": list(self.agent_types.keys())
        } 