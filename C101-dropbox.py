import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, "rb")

        dbx.files_upload(f.read(), file_to)


def main():
    access_token = "ODHEUJrdoxMAAAAAAAAAAastY7zsjLNNa7XlxgK9zhX9rKLQbh3LJswC4sdZUlqJ"

    transferData = TransferData(access_token)

    file_from = input("Enter file from source: ")
    file_to = input("Enter where you want your file to go: ")

    transferData.upload_files(file_from, file_to)

    print("File successfully uploaded!!!!!!!!!!!!!!!!!!!!")


main()

        
