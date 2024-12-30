from Pages import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def generate_pdf(year: int) -> None:
    """
    Generate the planner for the given year
    """
    file_name: str = f'{year}_planner.pdf'
    document_title: str = f'{year}_planer'

    pdf = canvas.Canvas(file_name)

    pdf.setTitle(document_title)

    pdfmetrics.registerFont(TTFont('UniSans', 'UniSansDemo-ThinCAPS.ttf'))
    pdfmetrics.registerFont(TTFont('UniSansHeavy', 'UniSansDemo-HeavyCAPS.ttf'))

    print_title_page(pdf, str(year))
    for i in range(1, 13):
        print_month_page(pdf, i, year)
        days_in_month = calendar.monthrange(year, i)[1]
        for day in range(1, days_in_month + 1):
            print_day_page(pdf, year, i, day)
    #testPage(pdf)
    sticker_page(pdf)
    pdf.save()

def main() -> None:
    year_str: str = input('Insert the year to generate the planner: ')
    if year_str.isdigit():
        year: int = int(year_str)
        generate_pdf(year)
    else:
        print('The year must be a number')
        main()

if __name__ == "__main__":
    main()
