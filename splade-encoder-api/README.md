# SPLADE Encoder API

SPLADE (Sparse Lexical and Expansion) モデルを使用して、テキストをスパースベクトル（単語重みの集合）に変換する FastAPI ベースの API サーバーです。
Elasticsearch の `rank_features` フィールドなどと組み合わせて、高度なセマンティック検索を実現するために使用します。

## 特徴

- **SPLADE**: `hotchpotch/japanese-splade-v2` モデルを使用して、日本語の語彙拡張（Expansion）を伴うベクトル化を行います。
- **FastAPI**: 高速で使いやすい REST API を提供します。
- **uv**: 高速な Python パッケージ管理ツールを使用しています。

## ディレクトリ構成

- `api/`: アプリケーションのコード
- `tests/`: テストコード

## セットアップ

### 依存関係のインストール

```bash
uv sync
```

## 実行方法

### API サーバーの起動

```bash
uv run uvicorn api.main:app
```

サーバーはデフォルトで `http://localhost:8000` で起動します。

### テストの実行

```bash
uv run pytest
```

## API エンドポイント

### 1. `POST /encode`
テキストをスパースベクトルに変換します。

**リクエスト本体:**
```json
{
  "text": "Scrapboxは知識共有のためのツールです。"
}
```

**レスポンス:**
```json
{
  "sparse_vector": {
    "token_id_1": 1.23,
    "token_id_2": 0.85
  }
}
```

### 2. `POST /encode_debug`
デバッグ用に、トークン（単語）と重みの対応を含めた結果を返します。

### 3. `GET /health`
API の稼働状態を確認します。

## モデルの変更
環境変数 `MODEL_ID` を指定することで、使用する SPLADE モデルを変更できます。
例: `MODEL_ID=hotchpotch/japanese-splade-v2 uv run splade-encoder-api`
