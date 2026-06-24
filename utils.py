import os, io, datetime as dt
from flask import send_file
import pandas as pd
from xhtml2pdf import pisa
from flask import render_template_string


def export_offerte_excel(rows, filename="offerte.xlsx"):
    df = pd.DataFrame([{
        # Identificativi RFQ
        "Cliente": r.rfq.nome_cliente,
        "Progetto": r.rfq.nome_progetto,
        "Rev. RFQ": f"Rev.{r.rfq.numero_revisione}",
        "Anno SOP": r.rfq.anno_sop,
        "Stato RFQ": r.rfq.stato,
        "Motivo Non Gestita": r.rfq.motivo_non_gestione or "",
        "RFQ Inserita Il": r.rfq.created_at.strftime("%Y-%m-%d %H:%M") if r.rfq.created_at else "",
        # Offerta
        "Rev. Offerta": r.id_offerta_rev,
        "Versione": r.versione,
        "Stato Offerta": r.stato,
        "Data Offerta": r.data_offerta.isoformat() if r.data_offerta else "",
        "Offerta Inserita Il": r.created_at.strftime("%Y-%m-%d %H:%M") if r.created_at else "",
        # Prezzi / Volumi / Fatturati
        "SOP Prezzo": r.prezzo_sop,   "SOP Vol": r.vol_sop,   "SOP Fatt": r.fatt_sop,
        "SOP+1 Prezzo": r.prezzo_sop1, "SOP+1 Vol": r.vol_sop1, "SOP+1 Fatt": r.fatt_sop1,
        "SOP+2 Prezzo": r.prezzo_sop2, "SOP+2 Vol": r.vol_sop2, "SOP+2 Fatt": r.fatt_sop2,
        "SOP+3 Prezzo": r.prezzo_sop3, "SOP+3 Vol": r.vol_sop3, "SOP+3 Fatt": r.fatt_sop3,
        "SOP+4 Prezzo": r.prezzo_sop4, "SOP+4 Vol": r.vol_sop4, "SOP+4 Fatt": r.fatt_sop4,
        # GM
        "GM SOP %": r.gm_sop,  "GM SOP+1 %": r.gm_sop1, "GM SOP+2 %": r.gm_sop2,
        "GM SOP+3 %": r.gm_sop3, "GM SOP+4 %": r.gm_sop4,
    } for r in rows])

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Offerte")
    output.seek(0)
    return send_file(
        output, as_attachment=True, download_name=filename,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def render_pdf_from_html(html, filename="report.pdf"):
    pdf_io = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(html), dest=pdf_io)
    pdf_io.seek(0)
    return send_file(pdf_io, as_attachment=True, download_name=filename, mimetype="application/pdf")
