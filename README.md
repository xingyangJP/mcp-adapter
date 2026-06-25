# WordPress Central MCP Server

WordPress の複数サイトを一箇所で管理するための中央 MCP ゲートウェイプロジェクト。  
[MCP Adapter（WordPress 公式）](https://github.com/WordPress/mcp-adapter) をベースに、Jetpack 方式の中央集権アーキテクチャを実装します。

---

## プロジェクト概要

### 解決する課題

従来は各 WordPress サイトにアビリティ定義プラグインを個別にインストール・管理する必要があり、サイト数が増えるほど運用コストが増大していました。

### アーキテクチャ

```
Claude（開発者）
  └── wp-central-mcp（Cloud Run）   ← アビリティ定義を一元管理
        ├── site-a.com の mcp-adapter へ転送
        ├── site-b.com の mcp-adapter へ転送
        └── site-c.com の mcp-adapter へ転送
```

**各 WordPress サイトには `mcp-adapter` のみを配置。**  
アビリティの追加・修正は中央サーバーへの変更1回で全サイトの操作に適用されます。

---

## リポジトリ構成

```
/
├── docs/                        # プロジェクトドキュメント
│   ├── REQUIREMENTS.md          # 要件定義書
│   ├── SPEC.md                  # 仕様書
│   └── ARCHITECTURE.md          # アーキテクチャ設計書
├── mcp-adapter/                 # WordPress 公式 MCP Adapter（フォーク元）
├── wordpress-wae/               # WordPress Abilities 拡張
└── central-mcp-server/          # 中央 MCP サーバー（実装予定）
```

---

## mcp-adapter について

[WordPress 公式 MCP Adapter](https://github.com/WordPress/mcp-adapter) のフォークです。  
各 WordPress サイトに導入する薄いブリッジプラグインとして機能します。

### 役割

- 中央サーバーからのリクエストを受け付ける
- WordPress 関数（`wp_insert_post` など）を実行する
- アビリティ定義は**持たない**（中央サーバーが管理）

### 動作エンドポイント

```
HTTP: /wp-json/mcp/mcp-adapter-default-server
```

### インストール

WordPress の管理画面または WP-CLI でインストールします。

```bash
wp plugin install https://github.com/xingyangJP/mcp-adapter/releases/latest/download/mcp-adapter.zip --activate
```

---

## 中央 MCP サーバー（wp-central-mcp）

Cloud Run 上で動作する Python 製のゲートウェイサーバーです。

**Claude から使えるツール:**

| ツール名 | 内容 |
|---|---|
| `list_sites` | 登録済み WordPress サイト一覧を返す |
| `discover_abilities` | 対象サイトで使えるアビリティ一覧を返す |
| `execute_wp_ability` | 対象サイトでアビリティを実行する |

詳細は [`docs/SPEC.md`](docs/SPEC.md) を参照してください。

---

## Claude への接続方法

### 事前準備

API キーを管理者から入手してください。

---

### デスクトップ Claude アプリ

`~/Library/Application Support/Claude/claude_desktop_config.json` を開き、`mcpServers` を追加します。

```json
{
  "mcpServers": {
    "wp-central-mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://wp-central-mcp-621428460182.asia-northeast1.run.app/mcp",
        "--header",
        "X-API-Key:YOUR_API_KEY_HERE"
      ]
    }
  }
}
```

`YOUR_API_KEY_HERE` を実際の API キーに置き換えてください。  
保存後、Claude デスクトップを再起動すると `wp-central-mcp` が使えるようになります。

> **注意:** `mcp-remote` の初回起動時に `npx` が自動でパッケージをダウンロードします。Node.js が必要です。

---

### Claude Code（CLI）

プロジェクトルートに `.mcp.json` を作成します（`.gitignore` 済みのため git には上がりません）。

```json
{
  "mcpServers": {
    "wp-central-mcp": {
      "type": "http",
      "url": "https://wp-central-mcp-621428460182.asia-northeast1.run.app/mcp",
      "headers": {
        "X-API-Key": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

`YOUR_API_KEY_HERE` を実際の API キーに置き換えてください。

---

### 接続確認

Claude で以下を実行して接続を確認します。

```
list_sites ツールを呼んで
```

`gentleman-loser: Gentleman Loser` が返れば接続成功です。

---

## ドキュメント

| ドキュメント | 内容 |
|---|---|
| [要件定義書](docs/REQUIREMENTS.md) | プロジェクトの背景・目的・機能要件 |
| [仕様書](docs/SPEC.md) | インターフェース・認証・インフラ仕様 |
| [アーキテクチャ設計書](docs/ARCHITECTURE.md) | レイヤー構成・依存方向ルール |

---

## セキュリティ

- `.mcp.json`（接続情報）は `.gitignore` で除外済み
- 機密情報はローカルの `.env` で管理し、本番環境は Secret Manager を使用
- このリポジトリはパブリックのため、認証情報・個人情報は絶対にコミットしない

---

## ライセンス

[GPL-2.0-or-later](https://spdx.org/licenses/GPL-2.0-or-later.html)
