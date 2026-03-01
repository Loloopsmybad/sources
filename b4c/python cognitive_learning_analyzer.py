import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.cluster import KMeans
import plotly.graph_objs as go
import plotly.express as px
import joblib
import os

class CognitiveLearningAnalyzer:
    def __init__(self, csv_file):
        """
        Initialize the Cognitive Learning Analyzer
        
        Parameters:
        csv_file (str): Path to the CSV file containing student data
        """
        # Read the CSV file
        self.df = pd.read_csv(csv_file)
        
        # List of subjects
        self.subjects = ['Science', 'English', 'History', 'Maths']
        
        # Prepare directory for saving models and visualizations
        self.setup_directories()
    
    def setup_directories(self):
        """
        Create necessary directories for saving models and outputs
        """
        os.makedirs('models', exist_ok=True)
        os.makedirs('visualizations', exist_ok=True)
    
    def preprocess_data(self):
        """
        Preprocess the data for machine learning models
        
        Returns:
        tuple: Preprocessed features and targets
        """
        # Add feature engineering
        self.df['total_score'] = self.df[self.subjects].sum(axis=1)
        self.df['average_score'] = self.df[self.subjects].mean(axis=1)
        
        # Create learning difficulty indicator
        learning_difficulty = []
        for _, row in self.df.iterrows():
            # Calculate variance in scores to determine learning consistency
            score_variance = np.var(row[self.subjects])
            difficulty = 'High' if score_variance > 100 else 'Medium' if score_variance > 50 else 'Low'
            learning_difficulty.append(difficulty)
        
        self.df['learning_difficulty'] = learning_difficulty
        
        # Prepare features and targets
        features = self.df[self.subjects + ['total_score', 'average_score']]
        target_improvement = self.df[self.subjects].apply(lambda x: x.max() - x.min(), axis=1)
        
        return features, target_improvement
    
    def train_improvement_predictor(self):
        """
        Train machine learning models to predict learning improvement areas
        
        Returns:
        dict: Model performance metrics
        """
        # Preprocess data
        X, y = self.preprocess_data()
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Random Forest Regressor for improvement prediction
        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_model.fit(X_train_scaled, y_train)
        
        # Predict improvements
        y_pred = rf_model.predict(X_test_scaled)
        
        # Save models
        joblib.dump(rf_model, 'models/improvement_predictor.joblib')
        joblib.dump(scaler, 'models/scaler.joblib')
        
        # Model performance
        mse = mean_squared_error(y_test, y_pred)
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': rf_model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return {
            'mean_squared_error': mse,
            'feature_importance': feature_importance
        }
    
    def cognitive_learning_clustering(self):
        """
        Perform clustering to identify student learning groups
        
        Returns:
        pd.DataFrame: Clustered student data
        """
        # Prepare features for clustering
        cluster_features = self.df[self.subjects + ['total_score', 'average_score']]
        
        # Scale features
        scaler = StandardScaler()
        cluster_features_scaled = scaler.fit_transform(cluster_features)
        
        # K-means clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        self.df['learning_cluster'] = kmeans.fit_predict(cluster_features_scaled)
        
        return self.df
    
    def generate_personalized_recommendations(self):
        """
        Generate personalized learning recommendations
        
        Returns:
        dict: Recommendations for each student
        """
        recommendations = {}
        
        for _, student in self.df.iterrows():
            student_recommendations = []
            
            # Analyze individual subject performance
            for subject in self.subjects:
                subject_score = student[subject]
                
                # Provide subject-specific recommendations
                if subject_score < 50:
                    student_recommendations.append(f"{subject} - Urgent Intervention Needed")
                    student_recommendations.append(f"  - One-on-one tutoring")
                    student_recommendations.append(f"  - Foundational concept review")
                elif 50 <= subject_score < 70:
                    student_recommendations.append(f"{subject} - Moderate Support Required")
                    student_recommendations.append(f"  - Additional practice materials")
                    student_recommendations.append(f"  - Supplementary online resources")
                else:
                    student_recommendations.append(f"{subject} - Maintaining Strong Performance")
                    student_recommendations.append(f"  - Advanced learning materials")
                    student_recommendations.append(f"  - Challenging problem sets")
            
            # Add cluster-based recommendations
            cluster = student['learning_cluster']
            if cluster == 0:
                student_recommendations.append("Overall Learning Approach: Structured Learning")
                student_recommendations.append("  - Create detailed study schedules")
                student_recommendations.append("  - Use active recall techniques")
            elif cluster == 1:
                student_recommendations.append("Overall Learning Approach: Adaptive Learning")
                student_recommendations.append("  - Explore multiple learning resources")
                student_recommendations.append("  - Practice interdisciplinary connections")
            else:
                student_recommendations.append("Overall Learning Approach: Personalized Support")
                student_recommendations.append("  - Identify and address specific learning gaps")
                student_recommendations.append("  - Use diagnostic learning tools")
            
            recommendations[student['Name']] = student_recommendations
        
        return recommendations
    
    def visualize_learning_insights(self):
        """
        Create comprehensive visualizations of learning insights
        """
        # 1. Subject Performance Heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.df[self.subjects], cmap='YlGnBu', annot=True, fmt='.2f')
        plt.title('Student Performance Heatmap')
        plt.tight_layout()
        plt.savefig('visualizations/subject_performance_heatmap.png')
        plt.close()
        
        # 2. Learning Cluster Distribution
        plt.figure(figsize=(10, 6))
        cluster_distribution = self.df['learning_cluster'].value_counts()
        cluster_distribution.plot(kind='bar')
        plt.title('Distribution of Learning Clusters')
        plt.xlabel('Cluster')
        plt.ylabel('Number of Students')
        plt.tight_layout()
        plt.savefig('visualizations/learning_cluster_distribution.png')
        plt.close()
        
        # 3. Interactive Scatter Plot with Plotly
        fig = px.scatter(
            self.df, 
            x='average_score', 
            y='total_score', 
            color='learning_cluster',
            hover_data=self.subjects + ['Name'],
            title='Student Performance Clusters'
        )
        fig.write_html('visualizations/performance_clusters.html')
    
    def generate_comprehensive_report(self):
        """
        Generate a comprehensive learning improvement report
        """
        print("=" * 50)
        print("COGNITIVE LEARNING IMPROVEMENT ANALYSIS")
        print("=" * 50)
        
        # Train improvement predictor
        print("\nTraining Improvement Prediction Model...")
        model_performance = self.train_improvement_predictor()
        print("\nModel Performance:")
        print(f"Mean Squared Error: {model_performance['mean_squared_error']:.4f}")
        
        print("\nFeature Importance for Learning Improvement:")
        print(model_performance['feature_importance'])
        
        # Perform clustering
        print("\nPerforming Learning Cluster Analysis...")
        self.cognitive_learning_clustering()
        
        # Generate personalized recommendations
        print("\nGenerating Personalized Learning Recommendations...")
        recommendations = self.generate_personalized_recommendations()
        
        # Create visualizations
        print("\nGenerating Learning Insights Visualizations...")
        self.visualize_learning_insights()
        
        # Save recommendations to a file
        with open('learning_recommendations.txt', 'w') as f:
            for student, recs in recommendations.items():
                f.write(f"Recommendations for {student}:\n")
                for rec in recs:
                    f.write(f"{rec}\n")
                f.write("\n")
        
        print("\nComprehensive report generated successfully!")
        print("Check the following files for detailed insights:")
        print("1. learning_recommendations.txt")
        print("2. visualizations/ directory")
        print("3. models/ directory")

def main():
    # Initialize the analyzer with the CSV file
    analyzer = CognitiveLearningAnalyzer('student_data.csv')
    
    # Generate comprehensive report
    analyzer.generate_comprehensive_report()

if __name__ == "__main__":
    main()