import os
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from mcp.server.fastmcp import FastMCP
from tools.auth import verify_api_key
import tools.list_sites as list_sites_mod
import tools.discover_abilities as discover_abilities_mod
import tools.execute_ability as execute_ability_mod


class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        api_key = request.headers.get("X-API-Key", "")
        if not verify_api_key(api_key):
            return JSONResponse({"error": "Invalid or missing API key"}, status_code=401)
        return await call_next(request)


class HostOverrideMiddleware:
    """MCP SDK のホスト検証を通過させるため Host ヘッダーを localhost に書き換える。
    API キー認証で保護済みのため DNS リバインディング攻撃のリスクはない。"""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] in ("http", "websocket"):
            scope["headers"] = [
                (b"host", b"localhost") if k == b"host" else (k, v)
                for k, v in scope.get("headers", [])
            ]
        await self.app(scope, receive, send)


mcp = FastMCP("wp-central-mcp")

list_sites_mod.register(mcp)
discover_abilities_mod.register(mcp)
execute_ability_mod.register(mcp)

_mcp_app = mcp.streamable_http_app()
_mcp_app.add_middleware(APIKeyMiddleware)

app = HostOverrideMiddleware(_mcp_app)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
