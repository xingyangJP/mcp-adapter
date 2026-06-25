from infrastructure.secrets import get_api_key


def verify_api_key(provided: str) -> bool:
    """提供された API キーが有効かどうかを検証する。"""
    expected = get_api_key()
    return bool(provided) and provided == expected
