import os

import pypdf


def pdf_split(pdf_path):
    assert os.path.splitext(pdf_path)[1].lower() == ".pdf"

    with open(pdf_path, "rb") as raw_pdf:
        pdf = pypdf.PdfReader(raw_pdf)

        for i, page in enumerate(pdf.pages):
            writer = pypdf.PdfWriter()
            writer.add_page(page)

            save_path = f"_split_{i+1:03d}".join(os.path.splitext(pdf_path))
            with open(save_path, "wb") as f:
                writer.write(f)


if __name__ == "__main__":
    pdf_path = str(input("分割したいPDFファイル："))
    pdf_split(pdf_path)
