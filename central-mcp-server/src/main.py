import os
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from tools.auth import verify_api_key
import tools.list_sites as list_sites_mod
import tools.discover_abilities as discover_abilities_mod
import tools.execute_ability as execute_ability_mod


class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        api_key = (
            request.headers.get("X-API-Key")
            or request.query_params.get("api_key")
            or ""
        )
        if not verify_api_key(api_key):
            return JSONResponse({"error": "Invalid or missing API key"}, status_code=401)
        return await call_next(request)


mcp = FastMCP(
    "wp-central-mcp",
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)

list_sites_mod.register(mcp)
discover_abilities_mod.register(mcp)
execute_ability_mod.register(mcp)

app = mcp.streamable_http_app()
app.add_middleware(APIKeyMiddleware)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
