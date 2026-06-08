from azure.storage.blob import BlobServiceClient
import os

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "raw-data"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

files = [
    "data/google_trends.csv",
    "data/fuel_prices.csv",
    "data/events.csv"
]

for file_path in files:
    blob_name = os.path.basename(file_path)

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"{blob_name} uploaded successfully!")

