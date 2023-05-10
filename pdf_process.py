import os
import glob
import pypdf


def pdf_merge(folder_path: str) -> bool:
    pdf_list = glob.glob(os.path.join(folder_path, "*.pdf"))

    if len(pdf_list) == 0:
        return False

    with pypdf.PdfMerger() as merger:
        try:
            for page in sorted(pdf_list):
                merger.append(page)
            merger.write(folder_path + ".pdf")
        except Exception:
            return False

    return True


def pdf_split(pdf_path: str) -> bool:
    if os.path.splitext(pdf_path)[-1].lower() != ".pdf":
        return False

    with open(pdf_path, "rb") as file:
        pdf = pypdf.PdfReader(file)

        for i, page in enumerate(pdf.pages):
            writer = pypdf.PdfWriter()
            writer.add_page(page)

            save_path = f"_split_{i+1:03d}".join(os.path.splitext(pdf_path))
            with open(save_path, "wb") as f:
                writer.write(f)

    return True


def pdf_rotate(pdf_path: str, angle: int) -> bool:
    if os.path.splitext(pdf_path)[-1].lower() != ".pdf":
        return False

    with open(pdf_path, "rb") as file:
        pdf = pypdf.PdfReader(file)
        writer = pypdf.PdfWriter()

        for i, page in enumerate(pdf.pages):
            page.rotate(angle)
            writer.add_page(page)

        save_path = "_roll".join(os.path.splitext(pdf_path))
        with open(save_path, "wb") as f:
            writer.write(f)

    return True
