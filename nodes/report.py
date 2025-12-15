from fpdf import FPDF
from core.state import AgentState

def pdf_node(state:AgentState) -> None:
    """
    Takes the final report and save it as a PDF.
    """

    print("Generating PDF....")
    
    report_text = state['final_report']
    filename = f"{state['topic'].replace(' ', '_')}_Report.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    #Add Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt= f"Research Report: {state['topic']}", ln=1, align='C')


    #Body
    pdf.set_font("Arial", size=12)
    # multi_cell to handle text wrapping automatically
    # encode/decode to strip non-latin characters avoiding basic FPDF crash
    safe_text = report_text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 10, txt=safe_text)
    
    pdf.output(filename)
    print(f"Success! PDF Saved: {filename}")
    return


