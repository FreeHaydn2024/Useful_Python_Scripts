from PyPDF2 import PdfReader
from docx import Document


def pdf_to_word(pdf_file, output_file):
    """
    pdf 转 word
    :param pdf_file:
    :param output_file:
    :return:
    """
    # 读取 PDF 文件
    pdf_reader = PdfReader(pdf_file)
    pdf_text = ''
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    # 创建 Word 文档
    doc = Document()
    doc.add_paragraph(pdf_text)

    # 保存 Word 文档
    doc.save(output_file)