from mcp.server.fastmcp import FastMCP
from infrastructure.secrets import get_sites_config
from infrastructure.wp_client import call_ability
from domain.site_registry import parse_sites, find_site


def register(mcp: FastMCP) -> None:
    @mcp.tool()
    async def execute_wp_ability(
        site_id: str,
        ability_name: str,
        parameters: dict,
    ) -> str:
        """指定サイトで WordPress アビリティを実行する。"""
        sites = parse_sites(get_sites_config())
        site = find_site(sites, site_id)
        if site is None:
            return f"エラー: サイト '{site_id}' が見つかりません。"
        return await call_ability(site.url, site.auth, ability_name, parameters)
