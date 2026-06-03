import subprocess

print("Fetching Google Trends data...")

subprocess.run(
    ["python", "scripts/google_trends.py"],
    check=True
)

print("Uploading files to Azure Blob Storage...")

subprocess.run(
    ["python", "scripts/upload_to_blob.py"],
    check=True
)

print("Pipeline completed successfully")