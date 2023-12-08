# Firefox bookmark fetching script for Alfred.app

Python script for an Alfred workflow to search and open Firefox bookmarks.

## What it does

The script searches for the automated backup files of bookmarks with the `.jsonlz4` extention in the profile folder of the Firefox application.
(cf. <https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data>)

Then, it decompresses the latest backup file and parses the data to display them in the Alfred UI.

## Installation

### Prerequisites

You need to have Python installed on your machine.
You also need to install additional packages specified in the **Requirements** section, if you haven't already done so.

### Python script

Clone this repository into a suitable location.
You can also download ZIP of this repository if you prefer.

### Alfred workflow

Create an Alfred Workflow inside the Alfred application.
Choose "Script Filter" as the input and copy-paste the following script into the "Script" field.

```zsh
cd $script_root_path

$python_executable ./scr/main.py
```

Then create two Environment Variables named `script_root_path` and `python_executable` in the workflow editor.
You should set the values for these variables according to your environment.

You can also replace `$script_root_path` and `$python_executable` in the script with appropriate values, instead of creating variables.

Finally, create an "Open URL" action and connect it to the Script Filter input.
Enter `{query}` into the URL field in the object configuration and save.

## Requirements

You need to have the following additional Python package installed.

- `lz4`: for LZ4 decompression purposes (<https://github.com/python-lz4/python-lz4>).

## Future works

- Publish the workflow as a bundle in the Alfred Gallery, if this tool gets enough attention.

---

Alfred is a registered trademark of Running with Crayons Ltd.

Firefox is a trademark of the Mozilla Foundation in the U.S. and other countries.

All the trademarks in this repository are used only to refer to and/or link to the original programs, products, services, and technologies.

