#!/usr/bin/env python3
"""
MCP (Model Context Protocol) - Ví dụ cơ bản
Hướng dẫn sử dụng MCP để kết nối AI với dữ liệu bên ngoài
"""

import asyncio
import json
import logging
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class MCPRequest:
    """Đại diện cho một yêu cầu MCP"""
    method: str
    params: Dict[str, Any]
    id: str
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

@dataclass
class MCPResponse:
    """Đại diện cho một phản hồi MCP"""
    result: Any
    error: str = None
    id: str = None

class MCPServer:
    """MCP Server đơn giản để xử lý yêu cầu"""
    
    def __init__(self):
        self.resources = {}
        self.tools = {}
        self._setup_default_resources()
    
    def _setup_default_resources(self):
        """Thiết lập các tài nguyên mặc định"""
        # Database resource
        self.resources['database'] = {
            'type': 'sqlite',
            'connection': None,
            'tables': ['users', 'products', 'orders']
        }
        
        # File system resource
        self.resources['filesystem'] = {
            'type': 'local',
            'root_path': './data',
            'allowed_extensions': ['.txt', '.json', '.csv', '.pdf']
        }
        
        # API resource
        self.resources['api'] = {
            'type': 'rest',
            'base_url': 'https://api.example.com',
            'endpoints': ['/users', '/products', '/analytics']
        }
    
    async def handle_request(self, request: MCPRequest) -> MCPResponse:
        """Xử lý yêu cầu MCP"""
        logger.info(f"Xử lý yêu cầu: {request.method}")
        
        try:
            if request.method == 'resources/list':
                return await self._list_resources(request)
            elif request.method == 'resources/read':
                return await self._read_resource(request)
            elif request.method == 'tools/list':
                return await self._list_tools(request)
            elif request.method == 'tools/call':
                return await self._call_tool(request)
            else:
                return MCPResponse(
                    result=None,
                    error=f"Phương thức không được hỗ trợ: {request.method}",
                    id=request.id
                )
        except Exception as e:
            logger.error(f"Lỗi xử lý yêu cầu: {e}")
            return MCPResponse(
                result=None,
                error=str(e),
                id=request.id
            )
    
    async def _list_resources(self, request: MCPRequest) -> MCPResponse:
        """Liệt kê các tài nguyên có sẵn"""
        resources_info = []
        for name, config in self.resources.items():
            resources_info.append({
                'name': name,
                'type': config['type'],
                'description': f"Tài nguyên {config['type']} cho {name}"
            })
        
        return MCPResponse(
            result={'resources': resources_info},
            id=request.id
        )
    
    async def _read_resource(self, request: MCPRequest) -> MCPResponse:
        """Đọc dữ liệu từ tài nguyên"""
        resource_name = request.params.get('name')
        query = request.params.get('query', {})
        
        if resource_name not in self.resources:
            return MCPResponse(
                result=None,
                error=f"Tài nguyên không tồn tại: {resource_name}",
                id=request.id
            )
        
        # Mô phỏng đọc dữ liệu
        mock_data = {
            'database': {
                'users': [
                    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
                    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
                ],
                'products': [
                    {'id': 1, 'name': 'Laptop', 'price': 999.99},
                    {'id': 2, 'name': 'Mouse', 'price': 29.99}
                ]
            },
            'filesystem': {
                'files': [
                    {'name': 'report.txt', 'size': 1024, 'modified': '2025-01-15'},
                    {'name': 'data.json', 'size': 2048, 'modified': '2025-01-14'}
                ]
            },
            'api': {
                'status': 'online',
                'endpoints': ['/users', '/products', '/analytics'],
                'rate_limit': '1000 requests/hour'
            }
        }
        
        return MCPResponse(
            result={'data': mock_data.get(resource_name, {})},
            id=request.id
        )
    
    async def _list_tools(self, request: MCPRequest) -> MCPResponse:
        """Liệt kê các công cụ có sẵn"""
        tools_info = [
            {
                'name': 'data_analysis',
                'description': 'Phân tích dữ liệu cơ bản',
                'parameters': {
                    'dataset': {'type': 'string', 'description': 'Tên dataset'},
                    'operation': {'type': 'string', 'enum': ['summary', 'correlation', 'trend']}
                }
            },
            {
                'name': 'file_processor',
                'description': 'Xử lý file',
                'parameters': {
                    'file_path': {'type': 'string', 'description': 'Đường dẫn file'},
                    'operation': {'type': 'string', 'enum': ['read', 'write', 'delete']}
                }
            }
        ]
        
        return MCPResponse(
            result={'tools': tools_info},
            id=request.id
        )
    
    async def _call_tool(self, request: MCPRequest) -> MCPResponse:
        """Gọi công cụ"""
        tool_name = request.params.get('name')
        tool_params = request.params.get('arguments', {})
        
        if tool_name == 'data_analysis':
            return await self._analyze_data(tool_params, request.id)
        elif tool_name == 'file_processor':
            return await self._process_file(tool_params, request.id)
        else:
            return MCPResponse(
                result=None,
                error=f"Công cụ không tồn tại: {tool_name}",
                id=request.id
            )
    
    async def _analyze_data(self, params: Dict, request_id: str) -> MCPResponse:
        """Phân tích dữ liệu"""
        dataset = params.get('dataset', 'default')
        operation = params.get('operation', 'summary')
        
        # Mô phỏng phân tích dữ liệu
        analysis_results = {
            'summary': {
                'total_records': 1000,
                'missing_values': 5,
                'data_types': {'numeric': 3, 'categorical': 2, 'text': 1}
            },
            'correlation': {
                'feature_1': {'feature_2': 0.75, 'feature_3': 0.32},
                'feature_2': {'feature_3': 0.45}
            },
            'trend': {
                'trend_direction': 'increasing',
                'growth_rate': '15%',
                'seasonality': 'monthly'
            }
        }
        
        return MCPResponse(
            result={'analysis': analysis_results.get(operation, {})},
            id=request_id
        )
    
    async def _process_file(self, params: Dict, request_id: str) -> MCPResponse:
        """Xử lý file"""
        file_path = params.get('file_path', '')
        operation = params.get('operation', 'read')
        
        # Mô phỏng xử lý file
        file_operations = {
            'read': {'status': 'success', 'content': 'File content here...'},
            'write': {'status': 'success', 'bytes_written': 1024},
            'delete': {'status': 'success', 'file_removed': True}
        }
        
        return MCPResponse(
            result={'file_operation': file_operations.get(operation, {})},
            id=request_id
        )

class MCPClient:
    """MCP Client để giao tiếp với AI model"""
    
    def __init__(self, server: MCPServer):
        self.server = server
        self.request_id = 0
    
    def _generate_request_id(self) -> str:
        """Tạo ID duy nhất cho yêu cầu"""
        self.request_id += 1
        return f"req_{self.request_id}_{datetime.now().timestamp()}"
    
    async def list_resources(self) -> Dict:
        """Liệt kê tài nguyên"""
        request = MCPRequest(
            method='resources/list',
            params={},
            id=self._generate_request_id()
        )
        response = await self.server.handle_request(request)
        return response.result
    
    async def read_resource(self, resource_name: str, query: Dict = None) -> Dict:
        """Đọc tài nguyên"""
        request = MCPRequest(
            method='resources/read',
            params={'name': resource_name, 'query': query or {}},
            id=self._generate_request_id()
        )
        response = await self.server.handle_request(request)
        return response.result
    
    async def list_tools(self) -> Dict:
        """Liệt kê công cụ"""
        request = MCPRequest(
            method='tools/list',
            params={},
            id=self._generate_request_id()
        )
        response = await self.server.handle_request(request)
        return response.result
    
    async def call_tool(self, tool_name: str, arguments: Dict) -> Dict:
        """Gọi công cụ"""
        request = MCPRequest(
            method='tools/call',
            params={'name': tool_name, 'arguments': arguments},
            id=self._generate_request_id()
        )
        response = await self.server.handle_request(request)
        return response.result

async def demo_mcp_basics():
    """Demo cơ bản về MCP"""
    print("=== Bắt đầu Demo MCP Basics ===")
    print("=" * 50)
    
    # Khởi tạo server và client
    server = MCPServer()
    client = MCPClient(server)
    
    # 1. Liệt kê tài nguyên
    print("\n1. Liệt kê tài nguyên có sẵn:")
    resources = await client.list_resources()
    for resource in resources['resources']:
        print(f"  - {resource['name']} ({resource['type']}): {resource['description']}")
    
    # 2. Đọc dữ liệu từ database
    print("\n2. Đọc dữ liệu từ database:")
    db_data = await client.read_resource('database')
    print(f"  Users: {len(db_data['data']['users'])} records")
    print(f"  Products: {len(db_data['data']['products'])} records")
    
    # 3. Liệt kê công cụ
    print("\n3. Liệt kê công cụ có sẵn:")
    tools = await client.list_tools()
    for tool in tools['tools']:
        print(f"  - {tool['name']}: {tool['description']}")
    
    # 4. Sử dụng công cụ phân tích dữ liệu
    print("\n4. Phân tích dữ liệu:")
    analysis = await client.call_tool('data_analysis', {
        'dataset': 'sales_data',
        'operation': 'summary'
    })
    print(f"  Kết quả phân tích: {analysis['analysis']}")
    
    # 5. Xử lý file
    print("\n5. Xử lý file:")
    file_result = await client.call_tool('file_processor', {
        'file_path': '/path/to/file.txt',
        'operation': 'read'
    })
    print(f"  Kết quả xử lý file: {file_result['file_operation']}")
    
    print("\n=== Demo hoàn thành! ===")

if __name__ == "__main__":
    # Chạy demo
    asyncio.run(demo_mcp_basics()) 