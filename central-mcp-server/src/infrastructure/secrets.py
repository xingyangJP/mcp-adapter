import os
import json
from dotenv import load_dotenv

load_dotenv()


def _get_secret(secret_id: str) -> str:
    """Secret Manager またはローカル環境変数からシークレットを取得する。"""
    env_key = secret_id.upper().replace("-", "_")
    env_val = os.getenv(env_key)
    if env_val:
        return env_val

    from google.cloud import secretmanager
    client = secretmanager.SecretManagerServiceClient()
    project = os.getenv("GOOGLE_CLOUD_PROJECT", "wordpressmcp")
    name = f"projects/{project}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("utf-8").strip()


def get_sites_config() -> list[dict]:
    """登録サイト一覧を取得する。リクエストごとに読み込むことで再デプロイなしにサイト追加が可能。"""
    raw = _get_secret("wp-sites-config")
    data = json.loads(raw)
    return data.get("sites", [])


def get_api_key() -> str:
    """このサーバーへのアクセスを認証する API キーを取得する。"""
    return _get_secret("wp-central-mcp-api-key")
