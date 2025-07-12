"""
Bài tập 22: Networking

Mục tiêu:
- Hiểu cách làm việc với mạng trong Python
- Thực hành với sockets và HTTP
- Sử dụng async networking
"""

import socket
import asyncio
import aiohttp
import http.server
import socketserver
import json
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse, parse_qs
import ssl
import logging

# TODO: TCP server
class TCPServer:
    """
    TCP server implementation
    """
    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def start(self):
        """
        Start the server
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address}")
            
            try:
                data = client_socket.recv(1024)
                if data:
                    response = self.handle_request(data)
                    client_socket.send(response)
            except Exception as e:
                print(f"Error: {e}")
            finally:
                client_socket.close()
    
    def handle_request(self, data: bytes) -> bytes:
        """
        Handle client request
        """
        try:
            request = json.loads(data.decode())
            response = {
                'status': 'success',
                'message': f"Received: {request}"
            }
            return json.dumps(response).encode()
        except Exception as e:
            response = {
                'status': 'error',
                'message': str(e)
            }
            return json.dumps(response).encode()

# TODO: TCP client
class TCPClient:
    """
    TCP client implementation
    """
    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port
    
    def send_request(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send request to server
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.send(json.dumps(data).encode())
            response = client_socket.recv(1024)
            return json.loads(response.decode())

# TODO: HTTP server
class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler
    """
    def do_GET(self):
        """
        Handle GET request
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'status': 'success',
            'message': 'Hello, World!'
        }
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        """
        Handle POST request
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode())
            response = {
                'status': 'success',
                'message': f"Received: {data}"
            }
        except Exception as e:
            response = {
                'status': 'error',
                'message': str(e)
            }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

class HTTPServer:
    """
    HTTP server implementation
    """
    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port
        self.server = socketserver.TCPServer(
            (self.host, self.port),
            HTTPRequestHandler
        )
    
    def start(self):
        """
        Start the server
        """
        print(f"Server listening on {self.host}:{self.port}")
        self.server.serve_forever()

# TODO: HTTP client
class HTTPClient:
    """
    HTTP client implementation
    """
    def __init__(self, base_url: str = 'http://localhost:8000'):
        self.base_url = base_url
    
    def get(self, path: str = '/') -> Dict[str, Any]:
        """
        Send GET request
        """
        url = f"{self.base_url}{path}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', 8000))
            request = f"GET {path} HTTP/1.1\r\nHost: localhost\r\n\r\n"
            client_socket.send(request.encode())
            response = client_socket.recv(1024)
            return json.loads(response.decode().split('\r\n\r\n')[1])
    
    def post(self, path: str = '/', data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Send POST request
        """
        url = f"{self.base_url}{path}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', 8000))
            body = json.dumps(data or {})
            request = (
                f"POST {path} HTTP/1.1\r\n"
                f"Host: localhost\r\n"
                f"Content-Type: application/json\r\n"
                f"Content-Length: {len(body)}\r\n"
                f"\r\n"
                f"{body}"
            )
            client_socket.send(request.encode())
            response = client_socket.recv(1024)
            return json.loads(response.decode().split('\r\n\r\n')[1])

# TODO: Async HTTP server
class AsyncHTTPRequestHandler:
    """
    Async HTTP request handler
    """
    async def handle_request(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """
        Handle HTTP request
        """
        request_line = await reader.readline()
        method, path, version = request_line.decode().split()
        
        headers = {}
        while True:
            line = await reader.readline()
            if line == b'\r\n':
                break
            key, value = line.decode().split(': ')
            headers[key] = value
        
        if method == 'GET':
            response = {
                'status': 'success',
                'message': 'Hello, World!'
            }
        elif method == 'POST':
            content_length = int(headers.get('Content-Length', 0))
            body = await reader.read(content_length)
            try:
                data = json.loads(body.decode())
                response = {
                    'status': 'success',
                    'message': f"Received: {data}"
                }
            except Exception as e:
                response = {
                    'status': 'error',
                    'message': str(e)
                }
        else:
            response = {
                'status': 'error',
                'message': 'Method not allowed'
            }
        
        writer.write(b'HTTP/1.1 200 OK\r\n')
        writer.write(b'Content-Type: application/json\r\n')
        writer.write(b'\r\n')
        writer.write(json.dumps(response).encode())
        await writer.drain()
        writer.close()

class AsyncHTTPServer:
    """
    Async HTTP server implementation
    """
    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port
        self.handler = AsyncHTTPRequestHandler()
    
    async def start(self):
        """
        Start the server
        """
        server = await asyncio.start_server(
            self.handler.handle_request,
            self.host,
            self.port
        )
        print(f"Server listening on {self.host}:{self.port}")
        async with server:
            await server.serve_forever()

# TODO: Async HTTP client
class AsyncHTTPClient:
    """
    Async HTTP client implementation
    """
    def __init__(self, base_url: str = 'http://localhost:8000'):
        self.base_url = base_url
    
    async def get(self, path: str = '/') -> Dict[str, Any]:
        """
        Send GET request
        """
        url = f"{self.base_url}{path}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    
    async def post(self, path: str = '/', data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Send POST request
        """
        url = f"{self.base_url}{path}"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                return await response.json()

# TODO: Example usage
def example_usage():
    """
    Example usage of networking
    """
    # TCP server and client
    print("TCP server and client example:")
    server = TCPServer()
    client = TCPClient()
    
    # Start server in a separate thread
    import threading
    server_thread = threading.Thread(target=server.start)
    server_thread.daemon = True
    server_thread.start()
    
    # Send request
    response = client.send_request({'message': 'Hello, Server!'})
    print(f"Response: {response}")
    
    # HTTP server and client
    print("\nHTTP server and client example:")
    http_server = HTTPServer()
    http_client = HTTPClient()
    
    # Start server in a separate thread
    http_server_thread = threading.Thread(target=http_server.start)
    http_server_thread.daemon = True
    http_server_thread.start()
    
    # Send requests
    get_response = http_client.get()
    print(f"GET Response: {get_response}")
    
    post_response = http_client.post(data={'message': 'Hello, Server!'})
    print(f"POST Response: {post_response}")
    
    # Async HTTP server and client
    print("\nAsync HTTP server and client example:")
    async def run_async_example():
        async_server = AsyncHTTPServer()
        async_client = AsyncHTTPClient()
        
        # Start server
        server_task = asyncio.create_task(async_server.start())
        
        # Send requests
        get_response = await async_client.get()
        print(f"Async GET Response: {get_response}")
        
        post_response = await async_client.post(data={'message': 'Hello, Server!'})
        print(f"Async POST Response: {post_response}")
        
        # Stop server
        server_task.cancel()
    
    asyncio.run(run_async_example())

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo một máy chủ TCP cho một ứng dụng chat
2. Tạo một máy chủ HTTP cho một ứng dụng REST API
3. Tạo một máy chủ WebSocket cho một ứng dụng real-time
4. Tạo một máy chủ FTP cho một ứng dụng file transfer
5. Tạo một máy chủ SMTP cho một ứng dụng email
""" 