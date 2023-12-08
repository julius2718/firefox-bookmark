import lz4.block
import json

import os
import sys


def get_firefox_bookmarks():
    # detect home directory of the user
    home = os.path.expanduser("~")

    # detect the path to the database file
    ## https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data
    path = os.path.join(home, "Library/Application Support/Firefox/Profiles/")

    ## search in the subdirectories for bookmarkbackups directory
    backup_path = None
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if name == "bookmarkbackups":
                backup_path = os.path.join(root, name)
                break

    ## raise an error if the backup path is not found
    if not backup_path:
        raise FileNotFoundError("Bookmark backup path not found")

    # detect the latest backup file
    ## https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder-using-python
    list_of_backups = [os.path.join(backup_path, f) for f in os.listdir(backup_path)]
    latest = max(list_of_backups, key=os.path.getctime)

    # read the latest backup file
    ## https://gist.github.com/snorey/3eaa683d43b0e08057a82cf776fd7d83
    with open(latest, "rb") as f:
        f.read(8)
        data = f.read()
        json_str = lz4.block.decompress(data).decode("utf-8")

    # parse json data
    data = json.loads(json_str)

    return data


# extract bookmarks
## recursive function to extract bookmarks
def extract_bookmarks(data):
    if "children" in data.keys():
        for child in data["children"]:
            yield from extract_bookmarks(child)
    elif data["typeCode"] == 1:
        yield data
    else:
        pass


def main():
    data = get_firefox_bookmarks()
    bookmarks = list(extract_bookmarks(data))

    alfred_results = []
    for bookmark in bookmarks:
        item = {
            "uid": bookmark["guid"],
            "title": bookmark["title"],
            "subtitle": bookmark["uri"],
            "arg": bookmark["uri"],
            "autocomplete": bookmark["title"],
            "icon": {"path": "./icon.png"},
        }
        alfred_results.append(item)

    # output the results
    response = json.dumps({"items": alfred_results})

    sys.stdout.write(response)


if __name__ == "__main__":
    main()
