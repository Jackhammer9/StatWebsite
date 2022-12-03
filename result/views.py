from django.http import HttpResponse , HttpResponseNotFound
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import csv
from fpdf import FPDF
import os

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo.png', 60, 85, 100)
        # Arial bold 15
        self.set_font('Times', 'B', 24)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(40, 15, 'Scorecard', 'U' , 1, 0, 'C')
        # Line break
        self.ln(30)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

@csrf_exempt
def GetData(request):
    usn = request.POST.get('usn', False)

    filename = "sem1csv.csv"

    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    for row in rows:
        if str(row[1]) == str(usn):
            Name = row[2]
            subject1 = row[4]
            subject2 = row[7]
            subject3 = row[10]
            subject4 = row[13]
            subject5 = row[16]
            subject6 = row[19]
            subject7 = row[22]
            cc = row[24]
            sgpa = row[25]
            cgpa = row[26]

            cr1 = row[3]
            cr2 = row[6]
            cr3 = row[9]
            cr4 = row[12]
            cr5 = row[15]
            cr6 = row[18]
            cr7 = row[21]

            gp1 = row[5]
            gp2 = row[8]
            gp3 = row[11]
            gp4 = row[14]
            gp5 = row[17]
            gp6 = row[20]
            gp7 = row[23]

            return render(request, 'result.html', {'name':Name , 'usn': usn , 's1':subject1 , 's2':subject2 , 's3':subject3 , 's4':subject4 , 's5':subject5 , 's6':subject6 , 's7':subject7 , 'cc':cc , 'sgpa':sgpa , 'cgpa':cgpa , 'cr1':cr1 , 'cr2':cr2 , 'cr3':cr3 , 'cr4':cr4 , 'cr5' : cr5 , 'cr6':cr6 , 'cr7':cr7 , 'gp1':gp1 , "gp2":gp2 , 'gp3':gp3 , 'gp4':gp4 , 'gp5':gp5 , 'gp6':gp6 , 'gp7':gp7})
    return render(request, '404page.html')

def DownloadPDF(request):
    Name = request.POST.get('name',False)
    USN = request.POST.get('usn',False)
    s1  = request.POST.get('s1',False)
    s2  = request.POST.get('s2',False)
    s3  = request.POST.get('s3',False)
    s4  = request.POST.get('s4',False)
    s5  = request.POST.get('s5',False)
    s6  = request.POST.get('s6',False)
    s7  = request.POST.get('s7',False)

    gp1  = request.POST.get('gp1',False)
    gp2  = request.POST.get('gp2',False)
    gp3  = request.POST.get('gp3',False)
    gp4  = request.POST.get('gp4',False)
    gp5  = request.POST.get('gp5',False)
    gp6  = request.POST.get('gp6',False)
    gp7  = request.POST.get('gp7',False)

    cr1  = request.POST.get('cr1',False)
    cr2  = request.POST.get('cr2',False)
    cr3  = request.POST.get('cr3',False)
    cr4  = request.POST.get('cr4',False)
    cr5  = request.POST.get('cr5',False)
    cr6  = request.POST.get('cr6',False)
    cr7  = request.POST.get('cr7',False)

    cc  = request.POST.get('cc',False)
    sgpa = request.POST.get('sgpa',False)
    cgpa = request.POST.get('cgpa',False)
    if Name+".pdf" not in os.listdir():
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()

        pdf.set_font("TImes", "I" , size = 20)
        pdf.cell(200,10,txt="Name: " + Name , ln=1 , align='C')
        pdf.cell(200,10,txt="USN: " + USN , ln=2 , align='C')

        pdf.set_font("Times", size = 18)
        pdf.cell(200,10,txt="" , ln=3 , align='C')
        pdf.cell(200,10,txt="" , ln=4 , align='C')
        pdf.cell(200,10,txt="" , ln=5 , align='C')

        pdf.cell(200,10,txt="Subject       "+"CR" + "    GR" + "    GP" , ln=6 , align='C')

        pdf.cell(200,10,txt="21MA11 : " + cr1+ "     " + s1 + "     " + gp1, ln=9 , align='C')
        pdf.cell(200,10,txt="21CH12 : "+ cr2+ "     " + s2 + "     " + gp2 , ln=10 , align='C')
        pdf.cell(200,10,txt="21CS13 : "+ cr3+ "     " + s3 + "     " + gp3 , ln=11 , align='C')
        pdf.cell(200,10,txt="21ME14 : "+ cr4+ "     " + s4 + "     " + gp4 , ln=12 , align='C')
        pdf.cell(200,10,txt="21EC15 : "+ cr5+ "     " + s5 + "     " + gp5 , ln=13 , align='C')
        pdf.cell(200,10,txt="21HSY16 : "+ cr6+ "     " + s6 + "     " + gp6 , ln=14 , align='C')
        pdf.cell(200,10,txt="21HSE17 : "+ cr7+ "     " + s7 + "     " + gp7 , ln=15 , align='C')
        pdf.cell(200,10,txt="CUM Credit : "+cc , ln=13 , align='C')
        pdf.cell(200,10,txt="SGPA : "+sgpa , ln=14 , align='C')
        pdf.cell(200,10,txt="CGPA : "+cgpa , ln=15 , align='C')

        pdf.output(Name+".pdf") 

    try:    
        with open(Name+".pdf", 'rb') as f:
            file_data = f.read()
            response = HttpResponse(file_data, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + Name + ".pdf"

    except IOError:
        response = HttpResponseNotFound('<h1>Something Went Wrong File does not exist</h1>')
    
    return response
