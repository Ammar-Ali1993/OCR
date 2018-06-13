import cv2
import pytesseract
import xlsxwriter
from os import listdir
from os.path import isfile, join


#created by Ammar M.Ali



class Ocr:
  def __init__(self,indir,outdir,filename):
      self.indir = indir     #directory where the images you wanna read are at
      self.outdir = outdir   #directory where output excel file is at
      self.filename = filename   #excel file name


  def exec(self):



    #retrieve all images in the designated directory
    images = [f for f in listdir(self.indir) if isfile(join(self.indir, f))]

    nos = []    #an array to store the output in
    for k in images:   #loop through the images

       image = self.indir+k
       img = cv2.imread(image,0)
       retval = pytesseract.image_to_string(img)  #get the values
       myvalue = ''

    for i in retval:  #filter to only allow digits
           if i.isdigit() is True:
               myvalue = myvalue + i

    nos = nos +[myvalue]



       #write in the output excel file
    workbook = xlsxwriter.Workbook(self.outdir+self.filename)
    worksheet = workbook.add_worksheet()


    row = 0


    for no in (nos):
           worksheet.write(row, 0,no)
           row += 1



    workbook.close()



#testing the code
obj = Ocr('images/','excel/','myfile.xlsx')

obj.exec()
