import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

st.title('Cars')

# Image
st.image("cars.jpg",width=500)

st.title('Cars Dataset')

data = pd.read_csv("Car data.csv")
st.write("shape of a dataset",data.shape)
menu=st.sidebar.radio("Menu",["Home","Vehicle Name"])
if menu=="Home":
    st.image("22222.jpg",width=550)
    st.header("Tabular Data of a Vehicle")
    if st.checkbox("Tabular Data"):
        st.table(data.head(150))
    st.header("Statistical summary of a Dataframe")
    if st.checkbox("Statistics"):
        st.table(data.describe())
    
    st.header("Correlation Graph")
    if st.checkbox("Correlation Graph"):
        # Select only numeric columns for correlation
        numeric_data = data.select_dtypes(include=[np.number]).copy()
        
        # Ensure all data is numeric and coerce errors to NaN
        numeric_data = numeric_data.apply(pd.to_numeric, errors='coerce')
        
        # Drop any columns with all NaN values
        numeric_data = numeric_data.dropna(axis=1, how='all')
        
        # Calculate correlation matrix
        corr_matrix = numeric_data.corr()
        
        # Check if the correlation matrix is empty or contains only NaN values
        if corr_matrix.empty or corr_matrix.isnull().all().all():
            st.write("No valid numeric data available for correlation.")
        else:
            # Debug: Output the cleaned numeric data
            st.write("Cleaned numeric data used for correlation:")
            st.write(numeric_data)
            
            # Plot the heatmap
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
            
            # Display the plot in Streamlit
            st.pyplot(fig)
    st.title("Graphs")
    graph=st.selectbox("Different tyoes of graphs",["Scatter Plot","Bar Graph", "Histogram"])

    if graph=="Scatter Plot":
        value=st.slider("Filter data using carat",0,300)
        data=data.loc[data["CC"]>=value]
        fig,ax=plt.subplots(figsize=(10,5))
        sns.scatterplot(data=data,x="Name",y="CC",hue="Type")
        st.pyplot(fig)

    if graph=="Bar Graph":
        fig,ax=plt.subplots(figsize=(3.5,2))
        sns.barplot(x="Type",y=data.Type.index,data=data)
        st.pyplot(fig)
    if graph=="Histogram":
        fig,ax=plt.subplots(figsize=(5,3))
        sns.displot(data.Type,kde=True)
        st.pyplot(fig)

if menu == "Vehicle Name":
    st.title("Prediction of Car Prices")

    # Prepare the data for linear regression
    lr = LinearRegression()
    X = np.array(data["CC"]).reshape(-1, 1)  # Reshape to 2D array (n_samples, 1)
    y = np.array(data["Min Price (Lakh)"]).reshape(-1, 1)  # Reshape to 2D array (n_samples, 1)
    lr.fit(X, y)

    value = st.number_input("CC Value", min_value=int(X.min()), max_value=int(X.max()), step=1)
    value = np.array(value).reshape(1, -1)  # Reshape to 2D array (1, 1) for prediction
    prediction = lr.predict(value)
    if st.button("Price Prediction($)"):
        st.write(f"{prediction}")

    st.write(f"Predicted Min Price (Lakh): {prediction[0][0]:.2f}")
