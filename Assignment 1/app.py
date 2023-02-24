from azure.storage.blob import BlobServiceClient
from flask import Flask


def get_blob_from_container():
    """
    input: takes container name as input
    output: returns a list of blobs in the container
    """

    # AccountName='mlestorageaccount'
    # AccountKey='sxn6Kfm5Hhd2We6GOFpgNiBxB/J3M0J3c681XaxtAIU2z9903dNYNINaApq/3y1lslNrJnLM1l2v+AStcNJApA=='
    container_name = 'datacontainer'
    connection_string = "DefaultEndpointsProtocol=https;AccountName=mlestorageaccount;AccountKey=sxn6Kfm5Hhd2We6GOFpgNiBxB/J3M0J3c681XaxtAIU2z9903dNYNINaApq/3y1lslNrJnLM1l2v+AStcNJApA==;EndpointSuffix=core.windows.net"
    
    container_name = container_name

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    container_client = blob_service_client.get_container_client(
        container=container_name
    )

    blob_list = container_client.list_blobs()
    folders = []
    for blob in blob_list:
        print("\t" + blob.name)
        folders.append(blob.name)
    return folders


# print(blob_service_client.list_containers()[0])
"""
download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
container_client = blob_service_client.get_container_client(container= container_name) 
print("\nDownloading blob to \n\t" + download_file_path)

with open(file=download_file_path, mode="wb") as download_file:
 download_file.write(container_client.download_blob(blob.name).readall())
"""


app = Flask(__name__)


@app.route("/")
def display_folders():
    # displays the dictionary containing folder name and their respective file
    folders = get_blob_from_container()
    folders_dict = {}
    for folder in folders:
        print("************", folder)
        folder_name = folder.split("/")[0]
        files = folder.split("/")[1]
        folders_dict[folder_name] = files
    return folders_dict


if __name__ == "__main__":
    app.run()