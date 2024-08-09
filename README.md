# Streamlit_tutorial

# Cars Dataset Streamlit Web App

This is a simple Streamlit web application that allows users to explore and visualize the "Cars" dataset. The app provides various functionalities such as viewing tabular data, statistical summaries, correlation graphs, and different types of plots. Additionally, users can predict car prices based on engine capacity (CC).

## Features

- **Home Page:**
  - Display a header image of cars.
  - View the tabular data of the first 150 rows of the dataset.
  - View the statistical summary of the dataset.
  - Display a correlation graph (heatmap) of numeric columns.
  - Visualize the data using Scatter Plot, Bar Graph, or Histogram.

- **Vehicle Name Page:**
  - Predict car prices based on engine capacity (CC) using a simple linear regression model.

## Installation

To run this application locally, follow these steps:

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Clone the Repository

Install the Required Packages
pip install -r requirements.txt

Required Packages

streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn

Run the Application
streamlit run app.py

File Structure

app.py: Main application file that contains the Streamlit code.
requirements.txt: List of required Python packages.
cars.jpg: Image displayed on the home page.
Car data.csv: Dataset used in the application.
Dataset
The dataset used in this application is Car data.csv, which contains various features related to cars, such as engine capacity (CC), type, and minimum price (in Lakh).

Usage

The user can navigate between the "Home" and "Vehicle Name" pages using the sidebar menu.
In the "Home" page, users can explore the dataset through various visualizations.
In the "Vehicle Name" page, users can input the engine capacity (CC) of a car to predict its minimum price.

