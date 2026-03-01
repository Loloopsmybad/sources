import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io
import base64

class StudentPerformanceAnalyzer:
    def __init__(self, csv_file):
        """
        Initialize the analyzer with student data
        
        Parameters:
        csv_file (str): Path to the CSV file containing student marks
        """
        # Read the CSV file
        self.df = pd.read_csv(csv_file)
        
        # List of subjects
        self.subjects = ['Science', 'English', 'History', 'Maths']
    
    def get_student_names(self):
        """
        Retrieve list of student names
        
        Returns:
        list: Names of students in the dataset
        """
        return self.df['Name'].tolist() if 'Name' in self.df.columns else []
    
    def get_student_performance(self, student_name):
        """
        Get performance details for a specific student
        
        Parameters:
        student_name (str): Name of the student
        
        Returns:
        dict: Performance details for the student
        """
        # Find the student's row
        student_row = self.df[self.df['Name'] == student_name]
        
        if student_row.empty:
            raise ValueError(f"Student {student_name} not found")
        
        # Prepare performance summary
        performance = {}
        for subject in self.subjects:
            performance[subject] = student_row[subject].values[0]
        
        return performance
    
    def generate_student_pie_chart(self, student_name):
        """
        Generate pie chart for student's subject performance
        
        Parameters:
        student_name (str): Name of the student
        
        Returns:
        str: Base64 encoded image of the pie chart
        """
        # Get student performance
        performance = self.get_student_performance(student_name)
        
        # Create pie chart
        plt.figure(figsize=(10, 7))
        plt.pie(list(performance.values()), 
                labels=list(performance.keys()), 
                autopct='%1.1f%%')
        plt.title(f'{student_name} - Subject Performance')
        
        # Save to a bytes buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        
        # Encode the image to base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_base64
    
    def overall_performance_analysis(self):
        """
        Analyze overall performance across subjects
        
        Returns:
        dict: Summary of performance statistics
        """
        # Calculate mean, median, and standard deviation for each subject
        performance_summary = {}
        for subject in self.subjects:
            performance_summary[subject] = {
                'Mean': round(self.df[subject].mean(), 2),
                'Median': round(self.df[subject].median(), 2),
                'Std Dev': round(self.df[subject].std(), 2),
                'Min': round(self.df[subject].min(), 2),
                'Max': round(self.df[subject].max(), 2)
            }
        
        return performance_summary
    
    def visualize_subject_performance(self, output_dir='static'):
        """
        Create visualizations of subject performance
        
        Parameters:
        output_dir (str): Directory to save visualization images
        """
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Box plot to show distribution of marks in each subject
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.df[self.subjects])
        plt.title('Distribution of Marks Across Subjects')
        plt.ylabel('Marks')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'subject_performance_boxplot.png'))
        plt.close()
        
        # Histogram for each subject
        plt.figure(figsize=(15, 10))
        for i, subject in enumerate(self.subjects, 1):
            plt.subplot(2, 2, i)
            sns.histplot(self.df[subject], kde=True)
            plt.title(f'{subject} Marks Distribution')
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'subject_marks_distribution.png'))
        plt.close()