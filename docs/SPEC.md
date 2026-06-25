# 仕様書

**プロジェクト名:** WordPress Central MCP Server  
**作成日:** 2026-06-25  
**ステータス:** 確定

---

## 1. アーキテクチャ概要

```
Claude（開発者）
  └── wp-central-mcp（Cloud Run: wordpressmcp）
        ├── gentleman-loser.com の mcp-adapter へ転送
        ├── site-b.com の mcp-adapter へ転送
        └── site-c.com の mcp-adapter へ転送
```

---

## 2. 役割分担

### 中央 MCP サーバー（wp-central-mcp）

| 項目 | 内容 |
|---|---|
| 責務 | アビリティ定義の一元管理、Claude からの接続受付、WP サイトへのプロキシ |
| 実装言語 | Python |
| 実行環境 | Cloud Run（wordpressmcp / asia-northeast1） |
| 認証 | API キー（`X-API-Key` ヘッダー） |
| サイト接続情報 | Secret Manager で管理 |

### WP サイト側（mcp-adapter のみ）

| 項目 | 内容 |
|---|---|
| 責務 | 中央サーバーからのリクエスト受付、WP 関数の実行 |
| プラグイン | `mcp-adapter`（薄いブリッジのみ） |
| 廃止プラグイン | `enable-abilities-for-mcp`（アビリティ定義は中央サーバーへ移行） |

---

## 3. Claude から見たインターフェース（MCP ツール）

| ツール名 | 引数 | 内容 |
|---|---|---|
| `list_sites` | なし | 登録済み WP サイト一覧を返す |
| `discover_abilities` | `site_id` | 対象サイトで使えるアビリティ一覧を返す |
| `execute_wp_ability` | `site_id`, `ability_name`, `parameters` | 対象サイトでアビリティを実行する |

---

## 4. サイトレジストリ

各 WP サイトの接続情報を Secret Manager で管理する。

| フィールド | 内容 | 例 |
|---|---|---|
| `site_id` | サイト識別子 | `gentleman-loser` |
| `url` | mcp-adapter エンドポイント | `https://example.com/wp-json/mcp/...` |
| `auth` | 認証情報 | `Basic xxxxxxxx` |

Secret Manager のシークレット名: `wp-sites-config`  
形式: JSON

```json
{
  "sites": [
    {
      "site_id": "gentleman-loser",
      "url": "https://example.com/wp-json/mcp/mcp-adapter-default-server",
      "auth": "Basic <SECRET_MANAGER_で管理>"
    }
  ]
}
```

---

## 5. 認証フロー

```
Claude
  └── X-API-Key: {api_key} ヘッダー付きでリクエスト
        └── wp-central-mcp がキーを検証
              └── 正当であれば対象 WP サイトへ転送
```

API キーは Secret Manager の `wp-central-mcp-api-key` に保存。

---

## 6. インフラ

| 項目 | 内容 |
|---|---|
| サービス名 | `wp-central-mcp` |
| プロジェクト | `wordpressmcp`（621428460182） |
| リージョン | asia-northeast1 |
| デプロイ URL | https://wp-central-mcp-621428460182.asia-northeast1.run.app |

---

## 7. 新サイト追加手順

1. WP サイトに `mcp-adapter` をインストール・有効化
2. Secret Manager の `wp-sites-config` にサイト情報を追加
3. **再デプロイ不要** — Secret Manager はリクエストごとに読み取るため、追加後すぐに反映される

---

## 8. 実験サイト

| サイト | 用途 |
|---|---|
| gentleman-loser.com | 動作確認・実験用 |
