from fpdf import FPDF

pdf = FPDF(orientation='P',  # portrait
           unit='pt',  # points used in mobile phones, 1 point = 0.353 mm
           format='A4')  # A4 sheet

# to add a page
pdf.add_page()

# add some text
pdf.set_font(family='Times',  # type
             style='B',  # Bold
             size=24
             )

# cell is a rectangle drew on w and h and display given txt inside it
pdf.cell(w= 0, # w = 0 takes entire width of page
         h= 80,
         txt= 'Flatmates Bill',
         border= 1, # 1 - rectangle, 0 - no rectangle
         align= 'C', # center
         ln= 1 # next cell 0 - to right, 1 - beginning of next line == 2 - below
         )

pdf.cell(w= 100, h= 40, txt= 'Period', border= 1)
pdf.cell(w= 200, h= 40, txt= 'January 2022', border= 1)

# to save a pdf
pdf.output(name= 'Bill.pdf')