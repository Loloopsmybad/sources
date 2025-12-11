import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import matplotlib.backends.backend_tkagg as tkagg

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import matplotlib.backends.backend_tkagg as tkagg

class StudentPerformanceAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def overall_performance_analysis(self):
        performance_summary = {}
        for subject in ['Science', 'English', 'History', 'Maths']:
            performance_summary[subject] = {
                'Mean': self.df[subject].mean(),
                'Median': self.df[subject].median(),
                'Standard Deviation': self.df[subject].std(),
                'Max': self.df[subject].max(),
                'Min': self.df[subject].min()
            }
        return performance_summary

    def identify_improvement_areas(self):
        recommendations = {}
        for subject in ['Science', 'English', 'History', 'Maths']:
            low_performers = (self.df[subject] < 50).mean() * 100
            medium_performers = ((self.df[subject] >= 50) & (self.df[subject] < 75)).mean() * 100
            high_performers = (self.df[subject] >= 75).mean() * 100
            
            recommendations[subject] = {
                'Low Performers (%)': low_performers,
                'Medium Performers (%)': medium_performers,
                'High Performers (%)': high_performers,
                'Improvement Strategies': [
                    "Provide additional tutoring",
                    "Encourage group study sessions",
                    "Implement regular assessments"
                ]
            }
        return recommendations


class StudentPerformanceAnalyzerApp:
    def __init__(self, master):
        """
        Initialize the UI for Student Performance Analyzer
        
        Parameters:
        master (tk.Tk): Main window of the application
        """
        self.master = master
        master.title("Student Performance Analyzer")
        master.geometry("800x600")

        # File selection
        self.file_frame = tk.Frame(master)
        self.file_frame.pack(pady=10)

        self.file_label = tk.Label(self.file_frame, text="Select CSV File:")
        self.file_label.pack(side=tk.LEFT)

        self.file_path = tk.StringVar()
        self.file_entry = tk.Entry(self.file_frame, textvariable=self.file_path, width=50)
        self.file_entry.pack(side=tk.LEFT, padx=10)

        self.browse_button = tk.Button(self.file_frame, text="Browse", command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT)

        # Analysis Buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        analysis_buttons = [
            ("Overall Performance", self.show_overall_performance),
            ("Visualize Performance", self.show_performance_visualization),
            ("Improvement Areas", self.show_improvement_recommendations)
        ]

        for text, command in analysis_buttons:
            btn = tk.Button(self.button_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=5)

        # Results Display Area
        self.results_frame = tk.Frame(master)
        self.results_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.results_text = tk.Text(self.results_frame, wrap=tk.WORD)
        self.results_text.pack(expand=True, fill=tk.BOTH)

        # Subjects and Analyzer
        self.subjects = ['Science', 'English', 'History', 'Maths']
        self.analyzer = None

    def browse_file(self):
        """
        Open file dialog to select CSV file
        """
        filename = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")]
        )
        if filename:
            self.file_path.set(filename)
            try:
                self.analyzer = StudentPerformanceAnalyzer(filename)
                messagebox.showinfo("Success", "File loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {str(e)}")

    def show_overall_performance(self):
        """
        Display overall performance analysis
        """
        if not self.analyzer:
            messagebox.showwarning("Warning", "Please load a CSV file first!")
            return

        self.results_text.delete(1.0, tk.END)
        performance_summary = self.analyzer.overall_performance_analysis()
        
        result_str = "OVERALL PERFORMANCE ANALYSIS\n" + "=" * 50 + "\n"
        for subject, stats in performance_summary.items():
            result_str += f"\n{subject} Performance:\n"
            for stat_name, stat_value in stats.items():
                result_str += f"  {stat_name}: {stat_value:.2f}\n"
        
        self.results_text.insert(tk.END, result_str)

    def show_performance_visualization(self):
        """
        Create and display performance visualizations
        """
        if not self.analyzer:
            messagebox.showwarning("Warning", "Please load a CSV file first!")
            return

        # Create a new window for visualizations
        viz_window = tk.Toplevel(self.master)
        viz_window.title("Performance Visualizations")
        viz_window.geometry("1000x800")

        # Create matplotlib figures
        fig1, (ax1, ax2, ax3, ax4) = plt.subplots(2, 2, figsize=(15, 12))
        fig1.suptitle('Subject Marks Distribution')

        # Histograms for each subject
        for i, subject in enumerate(self.subjects):
            row = i // 2
            col = i % 2
            ax = [ax1, ax2, ax3, ax4][i]
            sns.histplot(self.analyzer.df[subject], kde=True, ax=ax)
            ax.set_title(f'{subject} Marks Distribution')
            ax.set_xlabel('Marks')
            ax.set_ylabel('Frequency')

        plt.tight_layout()

        # Embed matplotlib figure in Tkinter window
        canvas = tkagg.FigureCanvasTkAgg(fig1, master=viz_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def show_improvement_recommendations(self):
        """
        Display improvement recommendations
        """
        if not self.analyzer:
            messagebox.showwarning("Warning", "Please load a CSV file first!")
            return

        self.results_text.delete(1.0, tk.END)
        recommendations = self.analyzer.identify_improvement_areas()
        
        result_str = "SUBJECT IMPROVEMENT RECOMMENDATIONS\n" + "=" * 50 + "\n"
        for subject, data in recommendations.items():
            result_str += f"\n{subject} Performance Breakdown:\n"
            result_str += f"  Low Performers: {data['Low Performers (%)']}%\n"
            result_str += f"  Medium Performers: {data['Medium Performers (%)']}%\n"
            result_str += f"  High Performers: {data['High Performers (%)']}%\n"
            result_str += "  Improvement Strategies:\n"
            for strategy in data['Improvement Strategies']:
                result_str += f"    - {strategy}\n"
        
        self.results_text.insert(tk.END, result_str)



def main():
            root = tk.Tk()
            app = StudentPerformanceAnalyzerApp(root)
            root.mainloop()

if __name__ == "__main__":
         main()