from flask import Flask, render_template, request, session, redirect, url_for
from student_performance_analyzer import StudentPerformanceAnalyzer
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Used for session management

# Global variable to store the current analyzer
current_analyzer = None

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route to upload CSV file
    """
    global current_analyzer
    
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error='No file uploaded')
        
        file = request.files['file']
        
        # Check if filename is empty
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        
        # Save the uploaded file
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        
        # Initialize analyzer
        try:
            current_analyzer = StudentPerformanceAnalyzer(file_path)
            
            # Get list of student names
            student_names = current_analyzer.get_student_names()
            
            return render_template('select_student.html', students=student_names)
        
        except Exception as e:
            return render_template('index.html', error=str(e))
    
    return render_template('index.html')

@app.route('/student_report', methods=['GET', 'POST'])
def student_report():
    """
    Generate report for a selected student
    """
    global current_analyzer
    
    if current_analyzer is None:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        student_name = request.form.get('student')
        
        try:
            # Get student performance
            performance = current_analyzer.get_student_performance(student_name)
            
            # Generate pie chart
            pie_chart = current_analyzer.generate_student_pie_chart(student_name)
            
            # Get overall performance analysis
            performance_summary = current_analyzer.overall_performance_analysis()
            
            return render_template('student_report.html', 
                                   student_name=student_name,
                                   performance=performance, 
                                   pie_chart=pie_chart,
                                   performance_summary=performance_summary)
        
        except Exception as e:
            return render_template('select_student.html', 
                                   students=current_analyzer.get_student_names(), 
                                   error=str(e))
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)