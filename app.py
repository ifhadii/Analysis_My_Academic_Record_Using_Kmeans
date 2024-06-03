from flask import Flask, request, render_template
import os
import csv
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        if file:
            # Save the PDF file
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            # Convert PDF to CSV
            convert_to_csv(file_path)
            # Read data from CSV
            data, marks_data = read_csv(file_path.replace('.pdf', '.csv'))
            return render_template('index.html', message='File uploaded and processed successfully', data=data, marks_data=marks_data)
    return render_template('index.html')

def convert_to_csv(pdf_filename):
    # Open the PDF file
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # Extract text from each page
        text = ''
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
    # Write extracted text to CSV file
    with open(pdf_filename.replace('.pdf', '.csv'), 'w', newline='', encoding='utf-8') as csv_file:
        csv_file.write(text)

def read_csv(csv_filename):
    # Read data from CSV file
    with open(csv_filename, 'r', encoding='utf-8') as data_file:
        csv_reader = csv.reader(data_file)
        data = list(csv_reader)
        data_s = ''.join([','.join(row) for row in data]) # Convert list of lists to a single comma-separated string
    marks_data = process_data(data_s)
    return data, marks_data

def process_data(data_s):
    # Process data from CSV file
    data = data_s.split(',')
    A_plus = []
    A = []
    B_plus = []
    B = []
    C_plus = []
    C = []
    D_plus = []
    D = []
    F = []

    for i in data:
        if i == 'A+':
            A_plus.append(i)
        elif i == 'A':
            A.append(i)
        elif i == 'B+':
            B_plus.append(i)
        elif i == 'B':
            B.append(i)
        elif i == 'C+':
            C_plus.append(i)
        elif i == 'C':
            C.append(i)
        elif i == 'D+':
            D_plus.append(i)
        elif i == 'D':
            D.append(i)
        elif i == 'F':
            F.append(i)

    marks_data = {
        'A+': len(A_plus),
        'A': len(A),
        'B+': len(B_plus),
        'B': len(B),
        'C+': len(C_plus),
        'C': len(C),
        'D+': len(D_plus),
        'D': len(D),
        'F': len(F)
    }
    return marks_data

if __name__ == "__main__":
    app.run(debug=True)
