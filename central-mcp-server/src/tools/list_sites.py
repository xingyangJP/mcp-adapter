from mcp.server.fastmcp import FastMCP
from infrastructure.secrets import get_sites_config
from domain.site_registry import parse_sites, list_enabled_sites


def register(mcp: FastMCP) -> None:
    @mcp.tool()
    async def list_sites() -> str:
        """登録済みの WordPress サイト一覧を返す。"""
        sites = list_enabled_sites(parse_sites(get_sites_config()))
        if not sites:
            return "登録済みサイトはありません。"
        lines = [f"- {s.site_id}: {s.name} ({s.url})" for s in sites]
        return "\n".join(lines)
