import glob
import os

import pypdf


def pdf_merge(folder_path):
    with pypdf.PdfMerger() as pdf:
        pdf_list = glob.glob(os.path.join(folder_path, "*.pdf"))
        pdf_list.sort()

        for page in pdf_list:
            pdf.append(page)

        pdf.write(folder_path + ".pdf")


if __name__ == "__main__":
    pdf_path = str(input("結合するPDFファイルを含むフォルダ："))
    pdf_merge(pdf_path)
