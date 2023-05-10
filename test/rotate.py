import os

import pypdf


def pdf_rotate(pdf_path, angle):
    assert os.path.splitext(pdf_path)[1].lower() == ".pdf"

    with open(pdf_path, "rb") as raw_pdf:
        pdf = pypdf.PdfReader(raw_pdf)
        writer = pypdf.PdfWriter()

        for page in pdf.pages:
            page.rotate(angle)
            writer.add_page(page)

        save_path = "_roll".join(os.path.splitext(pdf_path))
        with open(save_path, "wb") as f:
            writer.write(f)


if __name__ == "__main__":
    pdf_path = str(input("回転したいPDFファイル："))
    angle = int(input("回転する角度（右回り）: "))
    pdf_rotate(pdf_path, angle)
