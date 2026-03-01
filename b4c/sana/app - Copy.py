from flask import Flask, render_template, request
from student_performance_analyzer import StudentPerformanceAnalyzer
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route to upload CSV file and generate performance report
    """
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
        
        # Analyze the uploaded file
        try:
            analyzer = StudentPerformanceAnalyzer(file_path)
            
            # Generate performance analysis
            performance_summary = analyzer.overall_performance_analysis()
            improvement_areas = analyzer.identify_improvement_areas()
            
            # Create visualizations
            analyzer.visualize_subject_performance()
            
            return render_template('report.html', 
                                   performance_summary=performance_summary, 
                                   improvement_areas=improvement_areas)
        
        except Exception as e:
            return render_template('index.html', error=str(e))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)