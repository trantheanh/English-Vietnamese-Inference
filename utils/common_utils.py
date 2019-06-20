import requests
import sys


# def download_file_from_url(id, destination):
#     url = "https://docs.google.com/uc?export=download"
#
#     print("opening url:{}".format(url))
#
#     site = urllib.urlopen(url)
#
#     meta = site.info()
#
#     print("Content-Length:", meta.getheaders("Content-Length")[0])
#
#     f = open(destination, "w")
#     f.write(site.read())
#     site.close()
#     f.close()
#
#     f = open("out.txt", "r")
#     print("File on disk after download:", len(f.read()))
#     f.close()
#
#     print("os.stat().st_size returns:", os.stat("out.txt").st_size)


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    i = 0
    length = len(response.content)
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            # sys.stdout.write("\rDownload progress: %.2f /%" % (i*CHUNK_SIZE/length))
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

            i = i + 1

    print("DOWNLOAD MODEL SUCCESS")
