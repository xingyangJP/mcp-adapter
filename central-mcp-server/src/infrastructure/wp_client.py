from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def call_ability(url: str, auth: str, ability_name: str, parameters: dict) -> str:
    """WP サイトの mcp-adapter 経由でアビリティを実行する。"""
    async with streamablehttp_client(url, headers={"Authorization": auth}) as (r, w, _):
        async with ClientSession(r, w) as session:
            await session.initialize()
            result = await session.call_tool(
                "mcp-adapter-execute-ability",
                {"ability_name": ability_name, "parameters": parameters},
            )
            return "\n".join(c.text for c in result.content if hasattr(c, "text"))


async def get_abilities(url: str, auth: str) -> str:
    """WP サイトで利用可能なアビリティ一覧を取得する。"""
    async with streamablehttp_client(url, headers={"Authorization": auth}) as (r, w, _):
        async with ClientSession(r, w) as session:
            await session.initialize()
            result = await session.call_tool("mcp-adapter-discover-abilities", {})
            return "\n".join(c.text for c in result.content if hasattr(c, "text"))
