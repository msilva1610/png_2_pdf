directory_path = '/Users/4431/dash/novo_dash_st/arquivos/scr'
images = [i for i in os.listdir(directory_path) if i.endswith(".png")]
images.sort()
# pdf_path = f"/Users/4431/dash/novo_dash_st/arquivos/scr/final_file2.pdf"
# file = open(pdf_path, "wb")
image_files = []
for img in images:
    img_path = f"/Users/4431/dash/novo_dash_st/arquivos/scr/{img}"
    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)
    pdf_name = str(image.filename).replace('png', 'pdf')
    pdf_path = f"{pdf_name}"
    file = open(pdf_path, "wb")    
    file.write(pdf_bytes)
    image.close()
file.close()
print("Successfully made pdf file")
# img_path = f"/Users/4431/dash/novo_dash_st/arquivos/scr/{images[0]}"
