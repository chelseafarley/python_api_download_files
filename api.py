from flask import Flask, Response, request
import pdfkit

app = Flask(__name__)

@app.route('/generate-pdf', methods=['GET'])
def generate_pdf():
    name = request.args.get('name')
    email = request.args.get('email')

    html = f"<html><body><h1>Hi {name}</h1><h2>Your email is {email}</h2></body></html>"
    pdf = pdfkit.from_string(html, False)

    headers = {
        'Content-Type': 'application/pdf',
        'Content-Disposition': f"attachment;filename={name}.pdf"
    }

    response = Response(pdf, headers=headers)
    return response

app.run();