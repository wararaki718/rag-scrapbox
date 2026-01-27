# rag-scrapbox

Scrapbox のデータを RAG (Retrieval-Augmented Generation) で利用するためのプロジェクトです。

## 構成

- `elasticsearch`: 検索エンジン。SPLADE によるベクトル検索をサポートします。
- `splade-encoder-api`: テキストを SPLADE ベクトルに変換する API。
- `ingestion-batch`: Scrapbox のデータを Elasticsearch に取り込むバッチ。

## 実行方法

### サービスの起動

プロジェクト直下にある `compose.yml` を使用して、Elasticsearch と SPLADE Encoder API を一括で起動できます。

```bash
docker compose up -d
```

起動後、以下のポートで各サービスにアクセス可能です。

- Elasticsearch: [http://localhost:9200](http://localhost:9200)
- Kibana: [http://localhost:5601](http://localhost:5601)
- SPLADE Encoder API: [http://localhost:8000](http://localhost:8000)
