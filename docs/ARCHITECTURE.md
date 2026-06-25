# アーキテクチャ設計書

**プロジェクト名:** WordPress Central MCP Server  
**プロファイル:** generic-layered（Team-architecture-mcp）  
**作成日:** 2026-06-25

---

## レイヤー構成

```
┌─────────────────────────────────┐
│        Presentation             │  MCP エンドポイント（Claude との I/O）
├─────────────────────────────────┤
│        Application              │  ツール定義・オーケストレーション
├─────────────────────────────────┤
│          Domain                 │  アビリティ管理・サイトレジストリのルール
├─────────────────────────────────┤
│       Infrastructure            │  WP サイトへの HTTP 通信・Secret Manager
└─────────────────────────────────┘
```

---

## 各レイヤーの責務

| レイヤー | 責務 | 主なモジュール |
|---|---|---|
| Presentation | FastMCP エントリーポイント、リクエスト受付 | `main.py` |
| Application | MCP ツール定義、API キー検証、処理フローの調停 | `tools/` |
| Domain | サイト有効判定、アビリティ実行ルール | `domain/` |
| Infrastructure | WP サイトへの HTTP 通信、Secret Manager 読み込み | `infrastructure/` |

---

## ディレクトリ構成

```
central-mcp-server/
├── Dockerfile
├── requirements.txt
└── src/
    ├── main.py                      # Presentation
    ├── tools/                       # Application
    │   ├── list_sites.py
    │   ├── discover_abilities.py
    │   └── execute_ability.py
    ├── domain/                      # Domain
    │   └── site_registry.py
    └── infrastructure/              # Infrastructure
        ├── wp_client.py             # WP サイトへの HTTP 通信
        └── secrets.py               # Secret Manager からの設定読み込み
```

---

## 依存方向ルール

| 依存元 → 依存先 | 可否 |
|---|---|
| Presentation → Application | ✅ |
| Application → Domain | ✅ |
| Application → Infrastructure | ✅ |
| Domain → Infrastructure | ❌ |
| Domain → Presentation | ❌ |
| Presentation → Infrastructure | ❌ |

---

## コミットメッセージ規約

- **言語:** 日本語（丁寧体）
- **避けるべき表現:** `fix`, `update`, `wip`, `misc`
- **例:** `サイト一覧取得ツールをApplicationレイヤーに追加する`
