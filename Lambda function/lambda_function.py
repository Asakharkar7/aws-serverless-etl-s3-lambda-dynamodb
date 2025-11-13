import boto3
import csv

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("RetailOrders2")

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # Get S3 bucket + key from event
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    
    print(f"Bucket: {bucket}, Key: {key}")

    # Download file from S3 to /tmp
    tmp_path = f"/tmp/{key}"
    s3.download_file(bucket, key, tmp_path)

    # Stream through CSV rows
    with open(tmp_path, "r") as f:
        reader = csv.DictReader(f)

        count = 0
        for row in reader:
            # Convert row to DynamoDB-friendly format
            item = {k: str(v) for k, v in row.items()}

            table.put_item(Item=item)
            count += 1

            # Print progress every 1000 rows
            if count % 1000 == 0:
                print(f"Inserted {count} rows...")

    print(f"✅ SUCCESS — Inserted total {count} rows.")
    return {"status": "done", "rows_inserted": count}
