# Password Protected PDF Decryptor
##  by - TheLegend


from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

#This is Password Breaker
def decrypt_pdf(input_path, output_path, password):
  try:
    with open(input_path, 'rb') as input_file, \
      open(output_path, 'wb') as output_file:
      reader = PdfFileReader(input_file)
      reader.decrypt(password)

      writer = PdfFileWriter()

      for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))

      writer.write(output_file)
      print(input_path+" has been cracked successfully")
      print("The password is : "+password)
    
  except:
    print(password+" failed!")


#This is Main Program Start
if __name__ == '__main__':
  # example usage:
  if len(sys.argv) != 4 :
    print ("Usage : "+sys.argv[0]+" encoded.pdf decoded.pdf password")
    sys.exit(1)
  
  try:
    pdf=open(sys.argv[1])
    pdf.close()
  except:
    print(sys.argv[1]+" pdf file does not exists")
    sys.exit(1)
  
  try:  
    fhandle = open(sys.argv[3])
    for word in fhandle:
      decrypt_pdf(sys.argv[1], sys.argv[2], word)
  except:
    print(sys.argv[3]+" wordlist not found.")
    sys.exit(1);