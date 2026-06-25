from dataclasses import dataclass


@dataclass
class Site:
    site_id: str
    url: str
    auth: str
    name: str = ""


def parse_sites(raw: list[dict]) -> list[Site]:
    return [
        Site(
            site_id=s["site_id"],
            url=s["url"],
            auth=s["auth"],
            name=s.get("name", s["site_id"]),
        )
        for s in raw
    ]


def find_site(sites: list[Site], site_id: str) -> Site | None:
    return next((s for s in sites if s.site_id == site_id), None)


def list_enabled_sites(sites: list[Site]) -> list[Site]:
    return [s for s in sites if s.site_id and s.url and s.auth]
