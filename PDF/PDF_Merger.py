import PyPDF2

print("PDF Merger")
print("")
x = input("Enter path to file #1: ")
y = input("Enter path to file #2: ")
z = input("Name of new PDF (Without .pdf extension): ")
zz = z + ".pdf"
pdf_merger = PyPDF2.PdfMerger()
files = [ x, y]

for file in files:
    pdf_merger.append(file)

pdf_merger.write(zz)
pdf_merger.close()

print("")
print("PDFs merged successfully! Saved as {zz}")