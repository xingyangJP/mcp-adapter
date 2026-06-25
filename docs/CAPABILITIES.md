# できること一覧

Claude + wp-central-mcp + mcp-adapter + wordpress-wae プラグインで実現できる操作の一覧です。  
gentleman-loser.com で確認済みのアビリティ（136個）を機能カテゴリごとにまとめています。

---

## サイト情報・環境

| できること | アビリティ |
|---|---|
| サイト名・URL・説明文などの基本情報を取得 | `core/get-site-info` |
| 認証中ユーザーのプロフィールを取得 | `core/get-user-info` |
| PHP バージョン・DB・WordPress バージョンを取得 | `core/get-environment-info` |
| 投稿数・ページ数・コメント数などの統計を取得 | `ewpa/site-stats`, `mcp-wp/get-site-stats` |
| WordPress の設定（タイトル・パーマリンクなど）を取得・更新 | `mcp-wp/get-settings`, `mcp-wp/update-settings` |

---

## 投稿（Post）

| できること | アビリティ |
|---|---|
| 投稿一覧をステータス・カテゴリ・件数・順序でフィルタして取得 | `ewpa/get-posts`, `mcp-wp/list-posts` |
| 投稿の全詳細（本文・メタ・アイキャッチ）を取得 | `ewpa/get-post`, `mcp-wp/get-post` |
| 新しい投稿を作成（タイトル・本文・カテゴリ・タグ・アイキャッチ・ステータス） | `ewpa/create-post`, `mcp-wp/create-post` |
| 既存投稿を更新（部分更新可） | `ewpa/update-post`, `mcp-wp/edit-post` |
| 投稿をゴミ箱に送る・完全削除 | `ewpa/delete-post`, `mcp-wp/delete-post` |
| 投稿内の特定テキストを検索して置換 | `ewpa/search-replace`, `mcp-wp/search-replace-content` |
| 高度な条件でクエリ（メタ値・タクソノミー組み合わせ） | `mcp-wp/query-posts-advanced` |
| 投稿を複製 | `mcp-wp/clone-item` |
| 複数投稿をまとめて更新 | `mcp-wp/batch-update` |

---

## ページ（Page）

| できること | アビリティ |
|---|---|
| ページ一覧・詳細を取得（テンプレート・階層含む） | `ewpa/get-pages`, `ewpa/get-page`, `mcp-wp/list-pages`, `mcp-wp/get-page` |
| 新しいページを作成 | `ewpa/create-page`, `mcp-wp/create-page` |
| 既存ページを編集 | `mcp-wp/edit-page` |
| ページを削除 | `mcp-wp/delete-page` |
| フロントエンドの描画済み HTML を取得 | `mcp-wp/get-rendered-page-html` |

---

## カスタム投稿タイプ（CPT）

| できること | アビリティ |
|---|---|
| サイトに登録されているカスタム投稿タイプ一覧を取得 | `ewpa/list-post-types` |
| CPT アイテムの一覧・詳細を取得 | `ewpa/get-cpt-items`, `ewpa/get-cpt-item`, `mcp-wp/list-content`, `mcp-wp/get-content` |
| CPT アイテムを作成・更新・削除 | `ewpa/create-cpt-item`, `ewpa/update-cpt-item`, `ewpa/delete-cpt-item` |
| CPT に紐づくタクソノミーとタームを取得・割り当て | `ewpa/get-cpt-taxonomies`, `ewpa/assign-cpt-terms` |

---

## カテゴリ・タグ（タクソノミー）

| できること | アビリティ |
|---|---|
| カテゴリ一覧（ID・スラッグ・投稿数）を取得 | `ewpa/get-categories`, `mcp-wp/list-categories` |
| タグ一覧を取得 | `ewpa/get-tags`, `mcp-wp/list-tags` |
| カテゴリ・タグを新規作成 | `ewpa/create-category`, `ewpa/create-tag`, `mcp-wp/create-category`, `mcp-wp/create-tag` |
| 既存のターム（カテゴリ・タグなど）を編集・削除 | `mcp-wp/edit-term`, `mcp-wp/delete-term` |

---

## コメント

| できること | アビリティ |
|---|---|
| コメント一覧をステータス・投稿でフィルタして取得 | `ewpa/get-comments`, `mcp-wp/list-comments` |
| コメントを承認・保留・スパム・ゴミ箱に変更 | `ewpa/moderate-comment` |
| コメントに返信 | `ewpa/reply-comment` |
| コメントを編集 | `ewpa/update-comment`, `mcp-wp/edit-comment` |
| コメントを削除 | `mcp-wp/delete-comment` |

---

## メディア

| できること | アビリティ |
|---|---|
| メディアライブラリの一覧を取得（MIME タイプ・検索でフィルタ） | `ewpa/get-media`, `mcp-wp/list-media` |
| 外部 URL から画像をダウンロードしてメディアライブラリに登録 | `ewpa/upload-image` |
| ファイルをアップロード | `mcp-wp/upload-media` |
| メディアのタイトル・キャプション・ALT テキストを編集 | `mcp-wp/edit-media` |
| メディアファイルを差し替え（ID を維持したまま） | `mcp-wp/replace-media-file` |
| メディアを削除 | `mcp-wp/delete-media` |

---

## ユーザー

| できること | アビリティ |
|---|---|
| ユーザー一覧（ID・名前・メール・ロール）を取得 | `ewpa/get-users`, `mcp-wp/list-users` |
| ユーザー詳細・現在のユーザー情報を取得 | `mcp-wp/get-user`, `mcp-wp/get-current-user` |
| ユーザーを新規作成・編集 | `mcp-wp/create-user`, `mcp-wp/edit-user` |

---

## SEO

### Rank Math

| できること | アビリティ |
|---|---|
| 投稿・ページの Rank Math メタ情報を取得（タイトル・説明・OGP・スコアなど） | `ewpa/get-rankmath` |
| フォーカスキーワード・SEO タイトル・メタ説明などを更新 | `ewpa/update-rankmath` |
| FAQ・Article などの構造化データ（JSON-LD スキーマ）を書き込み | `ewpa/update-rankmath-schema` |

### SEOPress

| できること | アビリティ |
|---|---|
| SEOPress メタ情報を取得 | `ewpa/get-seopress` |
| SEOPress メタ情報を更新 | `ewpa/update-seopress` |

### Yoast SEO

| できること | アビリティ |
|---|---|
| Yoast SEO メタ情報を取得 | `ewpa/yoast-get-seo` |
| フォーカスキーフレーズ・SEO タイトル・メタ説明などを更新 | `ewpa/yoast-update-seo` |
| サイトマップインデックスを取得 | `ewpa/yoast-get-sitemap-index` |

### 共通

| できること | アビリティ |
|---|---|
| 任意の投稿メタキーを直接読み書き（SEO Framework など） | `ewpa/get-post-meta`, `ewpa/update-post-meta` |

---

## ナビゲーションメニュー

| できること | アビリティ |
|---|---|
| メニューロケーションと割り当て済みメニューを取得 | `mcp-wp/list-menu-locations` |
| メニュー一覧・詳細を取得 | `mcp-wp/list-menus`, `mcp-wp/get-menu` |
| メニューを作成・編集・削除 | `mcp-wp/create-menu`, `mcp-wp/edit-menu`, `mcp-wp/delete-menu` |
| メニューをテーマのロケーションに割り当て | `mcp-wp/assign-menu-location` |
| メニューアイテムを追加・編集・削除 | `mcp-wp/create-menu-item`, `mcp-wp/edit-menu-item`, `mcp-wp/delete-menu-item` |

---

## ブロックエディタ（Gutenberg / FSE）

| できること | アビリティ |
|---|---|
| テンプレート・テンプレートパート・ナビゲーションエンティティを取得・作成・編集・削除 | `mcp-wp/list-block-entities` など |
| パターンの一覧・取得・作成・編集・削除 | `mcp-wp/list-patterns` など |
| パターンの JSON エクスポート・インポート | `mcp-wp/export-pattern`, `mcp-wp/import-pattern` |
| パターンの使用箇所を検索 | `mcp-wp/get-pattern-usage` |
| 利用可能なブロックタイプ一覧を取得 | `mcp-wp/get-block-types` |
| ブロック JSON を検証 | `mcp-wp/validate-blocks` |
| Gutenberg の設定情報を取得 | `mcp-wp/get-gutenberg-settings` |

---

## プラグイン管理

| できること | アビリティ |
|---|---|
| 有効化中のプラグイン一覧を取得（SEO・多言語・WooCommerce の検出付き） | `ewpa/get-active-plugins` |
| インストール済みプラグインの一覧・詳細を取得 | `mcp-wp/list-plugins`, `mcp-wp/get-plugin` |
| プラグインを有効化・無効化・更新・削除 | `mcp-wp/activate-plugin` など |
| WordPress.org スラッグまたは ZIP URL からインストール | `mcp-wp/install-plugin` |
| PHP コードスニペットを安全に作成（Code Snippets プラグイン経由） | `ewpa/create-code-snippet` |

---

## テーマ管理

| できること | アビリティ |
|---|---|
| テーマ一覧・詳細・サポート機能を取得 | `mcp-wp/list-themes`, `mcp-wp/get-theme`, `mcp-wp/get-theme-supports` |
| テーマを切り替え・インストール・更新・削除 | `mcp-wp/switch-theme` など |

---

## 多言語（Polylang / WPML）

| できること | アビリティ |
|---|---|
| 投稿に言語を割り当て | `ewpa/set-post-language` |
| 2 つの投稿を翻訳としてリンク | `ewpa/link-post-translation` |
| 投稿の全言語バージョン（ID・タイトル・URL）を取得 | `ewpa/get-post-translations` |

---

## JetEngine オプションページ

| できること | アビリティ |
|---|---|
| 登録済みオプションページとフィールドスキーマを一覧表示 | `ewpa/je-list-options-pages` |
| オプションページの全フィールド値を取得 | `ewpa/je-get-options-page` |
| 任意のフィールドを更新（リピーター・セレクトなど対応） | `ewpa/je-update-options-page-field` |

---

## その他

| できること | アビリティ |
|---|---|
| カスタム REST エンドポイントを直接呼び出し | `mcp-wp/custom-rest-call` |

---

## 対応 SEO プラグイン

- **Rank Math** — メタ・スキーマ・OGP
- **SEOPress** — メタ・OGP・Twitter Card
- **Yoast SEO** — メタ・OGP・サイトマップ
- **The SEO Framework / AIOSEO など** — `ewpa/get-post-meta` / `ewpa/update-post-meta` で対応可

## 対応プラグイン（特殊機能）

- **Polylang / WPML** — 多言語投稿管理
- **JetEngine** — オプションページ操作
- **Code Snippets** — PHP スニペット安全作成
