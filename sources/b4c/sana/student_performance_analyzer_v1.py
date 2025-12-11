import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

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
    
    def identify_improvement_areas(self):
        """
        Identify subjects where students need improvement
        
        Returns:
        dict: Recommendations for each subject
        """
        recommendations = {}
        
        # Performance thresholds
        performance_thresholds = {
            'Low': 40,
            'Medium': 60,
            'High': 80
        }
        
        for subject in self.subjects:
            # Calculate percentage of students in different performance bands
            low_performers = (self.df[subject] < performance_thresholds['Low']).mean() * 100
            medium_performers = ((self.df[subject] >= performance_thresholds['Low']) & 
                                 (self.df[subject] < performance_thresholds['High'])).mean() * 100
            high_performers = (self.df[subject] >= performance_thresholds['High']).mean() * 100
            
            # Develop recommendations based on performance
            improvement_strategies = []
            if low_performers > 30:
                improvement_strategies.extend([
                    "Implement targeted remedial classes",
                    "Develop personalized learning plans",
                    "Provide additional study resources and tutoring"
                ])
            
            if medium_performers > 50:
                improvement_strategies.extend([
                    "Conduct peer study groups",
                    "Use interactive learning methods",
                    "Provide practice tests and mock exams"
                ])
            
            recommendations[subject] = {
                'Low Performers (%)': round(low_performers, 2),
                'Medium Performers (%)': round(medium_performers, 2),
                'High Performers (%)': round(high_performers, 2),
                'Improvement Strategies': improvement_strategies
            }
        
        return recommendations