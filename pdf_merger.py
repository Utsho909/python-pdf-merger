import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()
    print(f"✅ Merged {len(pdf_list)} files into '{output}'")

def get_pdfs_from_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.pdf')]

if __name__ == "__main__":
    print("🧩 PDF Merger Tool")
    folder = input("Enter the folder path containing PDFs: ").strip()
    output = input("Enter output file name (e.g., merged.pdf): ").strip()

    pdfs = get_pdfs_from_folder(folder)
    if not pdfs:
        print("❌ No PDFs found in the folder.")
    else:
        merge_pdfs(pdfs, output)
