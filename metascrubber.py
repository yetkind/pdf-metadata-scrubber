# PDF Metadata Scrubber and Linearizer
# MIT License
# Copyright (c) 2023 Yetkin Degirmenci

import PyPDF2   # For editing metadata.
from PyPDF2 import PdfReader, PdfWriter
from pikepdf import Pdf # For linearization.

reader = PdfReader("source.pdf")
writer = PdfWriter()

writer.append_pages_from_reader(reader)
metadata = reader.metadata
# Print the read metadata from the source PDF file.
# Just for crosscheck what you can read, you can disable this later.
print(str(reader.metadata))
# Replace dictionary values with empty values.
{k: v for k, v in metadata.items() if v!=None}

# Clean Producer Name otherwise it shows PyPDF2 by default
writer.add_metadata({"/Producer":""})

# Save the edited file.
with open("result.pdf", "wb") as fp:
    writer.write(fp)

# Re-open / linearize and save the same file.
new_pdf = Pdf.new()
with Pdf.open("result.pdf" , allow_overwriting_input=True) as pdf:
     pdf.save("result.pdf", linearize=True)
