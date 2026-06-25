from mcp.server.fastmcp import FastMCP
from infrastructure.secrets import get_sites_config
from infrastructure.wp_client import get_abilities
from domain.site_registry import parse_sites, find_site


def register(mcp: FastMCP) -> None:
    @mcp.tool()
    async def discover_abilities(site_id: str) -> str:
        """指定サイトで利用可能なアビリティ一覧を取得する。"""
        sites = parse_sites(get_sites_config())
        site = find_site(sites, site_id)
        if site is None:
            return f"エラー: サイト '{site_id}' が見つかりません。"
        return await get_abilities(site.url, site.auth)
