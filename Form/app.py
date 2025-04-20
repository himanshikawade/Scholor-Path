from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the scholarship application form


@app.route('/')
def home():
    return render_template('scholarship_form.html')

@app.route('/scholarship', methods=['GET', 'POST'])
def scholarship_form():
    if request.method == 'POST':
        # Get form data
        form_data = {
    'fullname': request.form['fullname'],                  # Student Name
    'dob': request.form['date'],                            # Date of Birth
    'gender': request.form['gender'],                      # Gender
    'contact': request.form['contactNumber'],                    # Contact Number
    'address': request.form['address'],                    # Address
    'name_of_institute': request.form.get('institution'),  # Caste Education Institute
    'course': request.form['course'],                      # Course
    'year_of_study': request.form['year'],        # Year for Study
    'scholorship_applying_for': request.form['scholarship'],  # Scholarship Applying For
    'state': request.form['state'],                        # State of Domicile
    'nationality': request.form['nationality'],            # Nationality
    'caste_certificate': request.form['caste'], # Caste Certificate
    'aadhar_card': request.form['aadhar'],            # Aadhar Card
    'income_certificate': request.form['income'],  # Income Certificate
    'domicile_certificate': request.form['domicile'], # Domicile Certificate
}

        # Pass form data to the certificate page
        return redirect(url_for('certificate', **form_data))
    return render_template('scholarship_form.html')

# Route for the scholarship eligibility certificate


@app.route('/certificate')
def certificate():
    # Retrieve data passed from the form
    return render_template('certificate.html', data=request.args)


if __name__ == '__main__':
    app.run(debug=True)
