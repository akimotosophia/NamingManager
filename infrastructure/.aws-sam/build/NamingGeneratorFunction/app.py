import json
import boto3

dynamodb = boto3.client('dynamodb')
TABLE_NAME = 'your-table-name'  # ここはあなたのテーブル名に合わせてね

def lambda_handler(event, context):
    # ① まずOPTIONSリクエストなら即CORSレスポンス
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            },
            'body': json.dumps({'message': 'CORS preflight OK'})
        }

    # ② それ以外（GETとか）の処理
    try:
        response = dynamodb.scan(TableName=TABLE_NAME)
        rules = [item['RULE_BODY']['S'] for item in response.get('Items', [])]
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Naming generated successfully',
                'rules': rules
            }),
            'headers': {
                'Access-Control-Allow-Origin': '*',  # CORSを許可するオリジン
                'Access-Control-Allow-Methods': 'GET, OPTIONS',  # 許可するメソッド
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'  # 許可するヘッダー
            },
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            },
        }
