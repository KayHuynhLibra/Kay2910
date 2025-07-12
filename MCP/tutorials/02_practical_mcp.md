# 🛠️ Hướng dẫn thực hành MCP - Từ cơ bản đến nâng cao

## 🎯 Mục tiêu bài học

Sau bài học này, bạn sẽ:
- ✅ Hiểu cách MCP hoạt động trong thực tế
- ✅ Xây dựng được MCP Server đầu tiên
- ✅ Tích hợp MCP với AI models
- ✅ Xử lý các tình huống thực tế

## 🚀 Bắt đầu với MCP

### 1. **Cài đặt MCP**

```bash
# Cài đặt MCP client và server
pip install mcp

# Hoặc từ source
git clone https://github.com/modelcontextprotocol/python-sdk
cd python-sdk
pip install -e .
```

### 2. **Kiến trúc MCP cơ bản**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Client    │◄──►│   Server    │◄──►│  Resources  │
│             │    │             │    │             │
│ - AI Model  │    │ - Protocol  │    │ - Database  │
│ - App       │    │ - Security  │    │ - Files     │
│ - User      │    │ - Routing   │    │ - APIs      │
└─────────────┘    └─────────────┘    └─────────────┘
```

## 🏗️ Xây dựng MCP Server đầu tiên

### **Bước 1: Tạo MCP Server cơ bản**

```python
#!/usr/bin/env python3
"""
MCP Server cơ bản - Hướng dẫn từng bước
"""

import asyncio
import json
from typing import Dict, List, Any
from mcp import Server, StdioServerParameters
from mcp.types import (
    Resource, Tool, TextContent, ImageContent, 
    EmbeddedResource, LoggingLevel
)

class BasicMCPServer(Server):
    """MCP Server cơ bản với các tính năng cơ bản"""
    
    def __init__(self):
        super().__init__()
        self.resources = {}
        self.tools = {}
        self._setup_resources()
        self._setup_tools()
    
    def _setup_resources(self):
        """Thiết lập các tài nguyên mặc định"""
        
        # Database resource
        self.resources["database"] = Resource(
            uri="mcp://database",
            name="Database",
            description="SQLite database connection",
            mimeType="application/x-sqlite3"
        )
        
        # File system resource
        self.resources["filesystem"] = Resource(
            uri="mcp://filesystem",
            name="File System",
            description="Local file system access",
            mimeType="application/x-directory"
        )
        
        # API resource
        self.resources["api"] = Resource(
            uri="mcp://api",
            name="External API",
            description="REST API connections",
            mimeType="application/json"
        )
    
    def _setup_tools(self):
        """Thiết lập các công cụ"""
        
        # Data analysis tool
        self.tools["analyze_data"] = Tool(
            name="analyze_data",
            description="Analyze dataset and provide insights",
            inputSchema={
                "type": "object",
                "properties": {
                    "dataset": {"type": "string", "description": "Dataset name"},
                    "operation": {
                        "type": "string", 
                        "enum": ["summary", "correlation", "trend"],
                        "description": "Analysis operation"
                    }
                },
                "required": ["dataset", "operation"]
            }
        )
        
        # File processing tool
        self.tools["process_file"] = Tool(
            name="process_file",
            description="Process files (read, write, delete)",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {"type": "string", "description": "File path"},
                    "operation": {
                        "type": "string",
                        "enum": ["read", "write", "delete"],
                        "description": "File operation"
                    },
                    "content": {"type": "string", "description": "Content for write operation"}
                },
                "required": ["file_path", "operation"]
            }
        )
    
    async def list_resources(self) -> List[Resource]:
        """Liệt kê tất cả tài nguyên"""
        return list(self.resources.values())
    
    async def read_resource(self, uri: str) -> List[TextContent]:
        """Đọc tài nguyên"""
        if uri == "mcp://database":
            return [TextContent(
                type="text",
                text="Database connection established. Available tables: users, products, orders"
            )]
        elif uri == "mcp://filesystem":
            return [TextContent(
                type="text", 
                text="File system access granted. Root directory: /data"
            )]
        elif uri == "mcp://api":
            return [TextContent(
                type="text",
                text="API connection ready. Endpoints: /users, /products, /analytics"
            )]
        else:
            raise ValueError(f"Unknown resource: {uri}")
    
    async def list_tools(self) -> List[Tool]:
        """Liệt kê tất cả công cụ"""
        return list(self.tools.values())
    
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> List[TextContent]:
        """Gọi công cụ"""
        if name == "analyze_data":
            return await self._analyze_data(arguments)
        elif name == "process_file":
            return await self._process_file(arguments)
        else:
            raise ValueError(f"Unknown tool: {name}")
    
    async def _analyze_data(self, arguments: Dict[str, Any]) -> List[TextContent]:
        """Phân tích dữ liệu"""
        dataset = arguments.get("dataset", "unknown")
        operation = arguments.get("operation", "summary")
        
        # Mô phỏng phân tích dữ liệu
        analysis_results = {
            "summary": f"Dataset '{dataset}' contains 1000 records with 5 features",
            "correlation": f"Strong correlation found between features in '{dataset}'",
            "trend": f"Upward trend detected in '{dataset}' over the last 30 days"
        }
        
        return [TextContent(
            type="text",
            text=analysis_results.get(operation, "Analysis completed")
        )]
    
    async def _process_file(self, arguments: Dict[str, Any]) -> List[TextContent]:
        """Xử lý file"""
        file_path = arguments.get("file_path", "")
        operation = arguments.get("operation", "read")
        
        # Mô phỏng file operations
        file_results = {
            "read": f"Successfully read file: {file_path}",
            "write": f"Successfully wrote to file: {file_path}",
            "delete": f"Successfully deleted file: {file_path}"
        }
        
        return [TextContent(
            type="text",
            text=file_results.get(operation, "File operation completed")
        )]

async def main():
    """Chạy MCP Server"""
    server = BasicMCPServer()
    
    # Khởi động server với stdio
    async with server.run_stdio(StdioServerParameters()) as stream:
        print("🚀 MCP Server đang chạy...")
        await stream.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
```

### **Bước 2: Tạo MCP Client**

```python
#!/usr/bin/env python3
"""
MCP Client - Kết nối với AI Model
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class MCPClient:
    """MCP Client để giao tiếp với AI model"""
    
    def __init__(self, server_path: str):
        self.server_path = server_path
        self.session = None
    
    async def connect(self):
        """Kết nối với MCP Server"""
        self.session = await stdio_client(
            StdioServerParameters(server_path=self.server_path)
        )
        print(f"✅ Đã kết nối với MCP Server: {self.server_path}")
    
    async def list_resources(self):
        """Liệt kê tài nguyên"""
        resources = await self.session.list_resources()
        print("📋 Tài nguyên có sẵn:")
        for resource in resources:
            print(f"  - {resource.name}: {resource.description}")
        return resources
    
    async def read_resource(self, uri: str):
        """Đọc tài nguyên"""
        contents = await self.session.read_resource(uri)
        print(f"📖 Nội dung từ {uri}:")
        for content in contents:
            print(f"  {content.text}")
        return contents
    
    async def list_tools(self):
        """Liệt kê công cụ"""
        tools = await self.session.list_tools()
        print("🛠️ Công cụ có sẵn:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        return tools
    
    async def call_tool(self, name: str, arguments: dict):
        """Gọi công cụ"""
        contents = await self.session.call_tool(name, arguments)
        print(f"🔧 Kết quả từ {name}:")
        for content in contents:
            print(f"  {content.text}")
        return contents
    
    async def close(self):
        """Đóng kết nối"""
        if self.session:
            await self.session.aclose()
            print("🔌 Đã đóng kết nối MCP")

async def demo_mcp_client():
    """Demo sử dụng MCP Client"""
    client = MCPClient("python code/01_mcp_basics.py")
    
    try:
        # Kết nối
        await client.connect()
        
        # Liệt kê tài nguyên
        await client.list_resources()
        
        # Đọc tài nguyên
        await client.read_resource("mcp://database")
        
        # Liệt kê công cụ
        await client.list_tools()
        
        # Gọi công cụ
        await client.call_tool("analyze_data", {
            "dataset": "sales_data",
            "operation": "summary"
        })
        
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(demo_mcp_client())
```

## 🔧 Tích hợp với AI Models

### **Tích hợp với OpenAI GPT**

```python
#!/usr/bin/env python3
"""
Tích hợp MCP với OpenAI GPT
"""

import openai
import asyncio
from typing import Dict, List, Any
from mcp import ClientSession

class MCPOpenAIIntegration:
    """Tích hợp MCP với OpenAI"""
    
    def __init__(self, api_key: str, mcp_session: ClientSession):
        self.client = openai.AsyncOpenAI(api_key=api_key)
        self.mcp_session = mcp_session
    
    async def get_context_from_mcp(self, query: str) -> str:
        """Lấy context từ MCP resources"""
        context_parts = []
        
        # Liệt kê resources
        resources = await self.mcp_session.list_resources()
        
        # Đọc từ database nếu có
        try:
            db_content = await self.mcp_session.read_resource("mcp://database")
            context_parts.append("Database context: " + db_content[0].text)
        except:
            pass
        
        # Đọc từ filesystem nếu có
        try:
            fs_content = await self.mcp_session.read_resource("mcp://filesystem")
            context_parts.append("File system context: " + fs_content[0].text)
        except:
            pass
        
        return "\n".join(context_parts)
    
    async def call_mcp_tools(self, tool_calls: List[Dict]) -> List[Dict]:
        """Gọi MCP tools"""
        tool_results = []
        
        for tool_call in tool_calls:
            tool_name = tool_call["function"]["name"]
            arguments = json.loads(tool_call["function"]["arguments"])
            
            try:
                contents = await self.mcp_session.call_tool(tool_name, arguments)
                tool_results.append({
                    "tool_call_id": tool_call["id"],
                    "output": contents[0].text if contents else ""
                })
            except Exception as e:
                tool_results.append({
                    "tool_call_id": tool_call["id"],
                    "output": f"Error: {str(e)}"
                })
        
        return tool_results
    
    async def chat_with_context(self, user_message: str) -> str:
        """Chat với context từ MCP"""
        
        # 1. Lấy context từ MCP
        context = await self.get_context_from_mcp(user_message)
        
        # 2. Liệt kê tools
        tools = await self.mcp_session.list_tools()
        tool_definitions = [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                }
            }
            for tool in tools
        ]
        
        # 3. Gọi OpenAI với context và tools
        messages = [
            {
                "role": "system",
                "content": f"You have access to the following context:\n{context}\n\nUse the available tools when needed."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
        
        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            tools=tool_definitions,
            tool_choice="auto"
        )
        
        # 4. Xử lý tool calls nếu có
        if response.choices[0].message.tool_calls:
            tool_results = await self.call_mcp_tools(response.choices[0].message.tool_calls)
            
            # Gọi lại OpenAI với tool results
            messages.append(response.choices[0].message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_results[0]["tool_call_id"],
                "content": tool_results[0]["output"]
            })
            
            final_response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=messages
            )
            
            return final_response.choices[0].message.content
        
        return response.choices[0].message.content

# Demo sử dụng
async def demo_openai_integration():
    """Demo tích hợp OpenAI với MCP"""
    
    # Khởi tạo MCP session (giả sử đã có)
    # mcp_session = await create_mcp_session()
    
    # Tích hợp
    integration = MCPOpenAIIntegration(
        api_key="your-openai-api-key",
        mcp_session=None  # Thay bằng session thực tế
    )
    
    # Chat với context
    response = await integration.chat_with_context(
        "Analyze the sales data and provide insights"
    )
    
    print(f"AI Response: {response}")

if __name__ == "__main__":
    asyncio.run(demo_openai_integration())
```

## 🔒 Bảo mật và Quản lý quyền truy cập

### **Implementing Access Control**

```python
#!/usr/bin/env python3
"""
Bảo mật MCP Server với Access Control
"""

import jwt
import hashlib
from typing import Dict, Optional
from datetime import datetime, timedelta

class MCPSecurityManager:
    """Quản lý bảo mật cho MCP Server"""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.access_tokens = {}
        self.resource_permissions = {
            "database": ["read", "write"],
            "filesystem": ["read"],
            "api": ["read", "write"]
        }
    
    def generate_token(self, user_id: str, permissions: List[str]) -> str:
        """Tạo access token"""
        payload = {
            "user_id": user_id,
            "permissions": permissions,
            "exp": datetime.utcnow() + timedelta(hours=24)
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Xác thực token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def check_permission(self, user_permissions: List[str], resource: str, action: str) -> bool:
        """Kiểm tra quyền truy cập"""
        if resource not in self.resource_permissions:
            return False
        
        required_permissions = self.resource_permissions[resource]
        return action in required_permissions and action in user_permissions

class SecureMCPServer(Server):
    """MCP Server với bảo mật"""
    
    def __init__(self, secret_key: str):
        super().__init__()
        self.security_manager = MCPSecurityManager(secret_key)
        self._setup_resources()
    
    async def read_resource(self, uri: str, access_token: str = None) -> List[TextContent]:
        """Đọc tài nguyên với xác thực"""
        
        # Xác thực token
        if not access_token:
            raise ValueError("Access token required")
        
        user_info = self.security_manager.verify_token(access_token)
        if not user_info:
            raise ValueError("Invalid or expired token")
        
        # Kiểm tra quyền
        resource_name = uri.split("://")[1] if "://" in uri else uri
        if not self.security_manager.check_permission(
            user_info["permissions"], resource_name, "read"
        ):
            raise ValueError("Insufficient permissions")
        
        # Thực hiện đọc
        return await super().read_resource(uri)
    
    async def call_tool(self, name: str, arguments: Dict[str, Any], access_token: str = None) -> List[TextContent]:
        """Gọi công cụ với xác thực"""
        
        # Xác thực token
        if not access_token:
            raise ValueError("Access token required")
        
        user_info = self.security_manager.verify_token(access_token)
        if not user_info:
            raise ValueError("Invalid or expired token")
        
        # Kiểm tra quyền cho tool
        if "admin" not in user_info["permissions"]:
            raise ValueError("Admin permission required for tools")
        
        # Thực hiện gọi tool
        return await super().call_tool(name, arguments)
```

## 📊 Monitoring và Logging

### **Implementing Monitoring**

```python
#!/usr/bin/env python3
"""
Monitoring và Logging cho MCP Server
"""

import logging
import time
from typing import Dict, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class MCPMetrics:
    """Metrics cho MCP Server"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    average_response_time: float = 0.0
    resource_access_count: Dict[str, int] = None
    tool_usage_count: Dict[str, int] = None
    
    def __post_init__(self):
        if self.resource_access_count is None:
            self.resource_access_count = {}
        if self.tool_usage_count is None:
            self.tool_usage_count = {}

class MCPMonitor:
    """Monitor cho MCP Server"""
    
    def __init__(self):
        self.metrics = MCPMetrics()
        self.logger = logging.getLogger("mcp_monitor")
        self.logger.setLevel(logging.INFO)
        
        # Setup file handler
        handler = logging.FileHandler("mcp_server.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def log_request(self, request_type: str, resource: str = None, 
                   success: bool = True, response_time: float = 0.0):
        """Log request"""
        self.metrics.total_requests += 1
        
        if success:
            self.metrics.successful_requests += 1
        else:
            self.metrics.failed_requests += 1
        
        # Update response time
        if self.metrics.total_requests > 0:
            self.metrics.average_response_time = (
                (self.metrics.average_response_time * (self.metrics.total_requests - 1) + response_time) 
                / self.metrics.total_requests
            )
        
        # Update resource/tool usage
        if resource:
            if request_type == "resource_access":
                self.metrics.resource_access_count[resource] = \
                    self.metrics.resource_access_count.get(resource, 0) + 1
            elif request_type == "tool_call":
                self.metrics.tool_usage_count[resource] = \
                    self.metrics.tool_usage_count.get(resource, 0) + 1
        
        # Log
        self.logger.info(
            f"Request: {request_type}, Resource: {resource}, "
            f"Success: {success}, Response Time: {response_time:.3f}s"
        )
    
    def get_metrics(self) -> Dict[str, Any]:
        """Lấy metrics hiện tại"""
        return {
            "total_requests": self.metrics.total_requests,
            "successful_requests": self.metrics.successful_requests,
            "failed_requests": self.metrics.failed_requests,
            "success_rate": (
                self.metrics.successful_requests / self.metrics.total_requests 
                if self.metrics.total_requests > 0 else 0
            ),
            "average_response_time": self.metrics.average_response_time,
            "resource_access_count": self.metrics.resource_access_count,
            "tool_usage_count": self.metrics.tool_usage_count
        }
    
    def generate_report(self) -> str:
        """Tạo báo cáo"""
        metrics = self.get_metrics()
        
        report = f"""
MCP Server Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*50}

📊 Performance Metrics:
- Total Requests: {metrics['total_requests']}
- Successful Requests: {metrics['successful_requests']}
- Failed Requests: {metrics['failed_requests']}
- Success Rate: {metrics['success_rate']:.2%}
- Average Response Time: {metrics['average_response_time']:.3f}s

📁 Resource Access:
"""
        
        for resource, count in metrics['resource_access_count'].items():
            report += f"- {resource}: {count} accesses\n"
        
        report += "\n🛠️ Tool Usage:\n"
        for tool, count in metrics['tool_usage_count'].items():
            report += f"- {tool}: {count} calls\n"
        
        return report

# Sử dụng trong MCP Server
class MonitoredMCPServer(Server):
    """MCP Server với monitoring"""
    
    def __init__(self):
        super().__init__()
        self.monitor = MCPMonitor()
        self._setup_resources()
    
    async def read_resource(self, uri: str) -> List[TextContent]:
        """Đọc tài nguyên với monitoring"""
        start_time = time.time()
        
        try:
            result = await super().read_resource(uri)
            response_time = time.time() - start_time
            
            self.monitor.log_request(
                "resource_access", 
                uri, 
                success=True, 
                response_time=response_time
            )
            
            return result
        except Exception as e:
            response_time = time.time() - start_time
            
            self.monitor.log_request(
                "resource_access", 
                uri, 
                success=False, 
                response_time=response_time
            )
            
            raise e
    
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> List[TextContent]:
        """Gọi công cụ với monitoring"""
        start_time = time.time()
        
        try:
            result = await super().call_tool(name, arguments)
            response_time = time.time() - start_time
            
            self.monitor.log_request(
                "tool_call", 
                name, 
                success=True, 
                response_time=response_time
            )
            
            return result
        except Exception as e:
            response_time = time.time() - start_time
            
            self.monitor.log_request(
                "tool_call", 
                name, 
                success=False, 
                response_time=response_time
            )
            
            raise e
    
    def get_monitoring_report(self) -> str:
        """Lấy báo cáo monitoring"""
        return self.monitor.generate_report()
```

## 🎯 Bài tập thực hành

### **Bài tập 1: Xây dựng MCP Server đơn giản**

1. Tạo MCP Server với 3 resources: database, filesystem, api
2. Implement 2 tools: data_analyzer, file_processor
3. Thêm logging và monitoring
4. Test với MCP Client

### **Bài tập 2: Tích hợp với AI Model**

1. Kết nối MCP Server với OpenAI GPT
2. Implement context retrieval từ MCP resources
3. Sử dụng MCP tools trong AI conversations
4. Test với các use cases thực tế

### **Bài tập 3: Bảo mật và Access Control**

1. Implement JWT-based authentication
2. Thêm role-based access control
3. Log security events
4. Test với different user roles

## 📚 Tài liệu tham khảo

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [JWT Security Best Practices](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/)

---

**🚀 Chúc bạn thành công với MCP!**

*"MCP mở ra một thế giới mới cho AI integration - hãy khám phá và sáng tạo!"* 