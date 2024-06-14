
# PDF Metadata Scrubber and Linearizer

This script allows you to edit the metadata of a PDF file and linearize it, using the PyPDF2 and pikepdf libraries. The metadata includes information such as the title, author, and producer of the PDF document.

## Prerequisites

Before using this script, ensure that you have the following prerequisites installed:

- Python 3.x
- PyPDF2 library
- pikepdf library

You can install the required libraries by running the following command:

```
pip install PyPDF2 pikepdf
```

## Usage

Follow the steps below to use the script:

1. Place the script in the same directory as the PDF file you want to edit.
2. Open the script file and modify the following line to specify the input PDF file name:

```python
reader = PdfReader("source.pdf")
```

3. Run the script using the following command:

```bash
python script.py
```

4. The script will read the metadata of the input PDF and create a new PDF file with the edited metadata. The new file will be named "result.pdf" and will be saved in the same directory as the script.
5. The producer name in the metadata will be replaced with an empty string to remove the default PyPDF2 value.
6. After saving the edited file, the script will open the "result.pdf" file and linearize it, overwriting the same file. Linearizing a PDF file rearranges its internal structure for faster web viewing.
7. The linearized PDF file will now be optimized for web viewing and will still retain the edited metadata.

Note: It's always a good idea to keep a backup of your original PDF file before running this script.


