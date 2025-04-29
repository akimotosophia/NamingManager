# 📖 README.md

```
# Naming Generator Project

命名ルールを選択・生成できるシンプルなWebアプリです。  
AWS上にReactフロントエンド＋Lambda/API Gateway/DynamoDBバックエンドをSAMで構築します。

---

## 📂 プロジェクト構成

```plaintext
naming-generator-project/
├── infrastructure/      # インフラ (SAMテンプレート)
│   └── template.yaml
├── backend/              # Lambdaバックエンド (Python3.12)
│   └── src/
│       └── app.py
├── frontend/             # Reactフロントエンド
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
├── README.md             # このファイル
```

---

## 🚀 デプロイ手順

### ① インフラ構築（SAM）

```bash
cd infrastructure/

# パッケージ作成（S3バケットは事前作成しておく）
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket <your-sam-artifact-bucket>

# デプロイ
sam deploy \
    --template-file packaged.yaml \
    --stack-name naming-generator-stack \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides CIDRBlock=<社内IPアドレス(CIDR形式)>
```

※ デプロイ完了後、以下が作成されます
- Lambda(API付き)
- DynamoDBテーブル
- フロントエンド用S3バケット
- CloudFrontディストリビューション

---

### ② フロントエンドビルド & デプロイ

```bash
# フロントエンドビルド
cd frontend/
npm install
npm run build

# S3にアップロード
aws s3 sync build/ s3://<デプロイされたS3バケット名>/
```

CloudFront URL（OutputsのFrontendURL）にアクセスして、画面表示を確認します。

---

## ✏️ 補足情報

- **API Gateway URL**は、Outputsの`ApiUrl`で確認できます。
- **フロントエンドからAPI呼び出し**する際は、`src/App.js` の fetch先URL をデプロイ後の `ApiUrl` に設定してください。
- **社内IP制限**  
  → API GatewayのリソースポリシーでCIDR制限されます。
- **課金イメージ**  
  → 基本すべて従量課金制（リクエスト数/データ転送量/ストレージ使用量ベース）です。
  → 1日数回程度の利用なら、AWS無料枠内か、数円〜数十円/月に収まる想定です。

---

## 📌 今後の追加予定（提案）

- Cognito認証を追加して認可制御
- LambdaのAPIをPOST対応にして、命名ルールの登録も可能に
- フロントエンドをVite化してビルド高速化

---

## 🛠️ 開発環境（参考）

- Node.js v20
- Python 3.12
- AWS SAM CLI v1.100.0
- Docker Desktop（ローカルSAMビルド用）
```
