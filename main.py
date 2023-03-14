import PyPDF2
import os
import datetime
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames


merger = PyPDF2.PdfMerger()
now = datetime.datetime.now()
# prompt the user to select two PDF files
Tk().withdraw()
pdf_files = askopenfilenames(filetypes=[('PDF Files', '*.pdf')], title='Select two PDF files')

# get the first filename from each tuple returned by askopenfilenames()
pdf_file1 = pdf_files[0]
pdf_file2 = pdf_files[1]

pdf_reader1 = PyPDF2.PdfReader(open(pdf_file1, 'rb'))
pdf_reader2 = PyPDF2.PdfReader(open(pdf_file2, 'rb'))

merger.append(pdf_reader1)
merger.append(pdf_reader2)

date = now.strftime(' %m-%d-%Y-%H%M%S')

# get the user's Downloads folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# create the output file path
output_file_path = os.path.join(downloads_folder, f"CombinedPDF{date}.pdf")

# write the combined PDF to a file
output_file = open(output_file_path, 'wb')
merger.write(output_file)
output_file.close()

print(f"Saved merged PDF to {output_file_path}")
