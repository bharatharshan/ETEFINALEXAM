import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from data_generator_final import generate_data
from PIL import Image
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def main():
    st.title("Hackathon Event Analysis Dashboard")
    st.markdown("Welcome to the Hackathon Event Analysis Dashboard! Here you can analyze data and process images.")

    # Generate the random dataset using the data generator function
    data = generate_data()

    # Display the generated data in a table
    st.header("Generated Dataset")
    st.dataframe(data)

    # Filters for user interactivity on the main screen
    st.header("Filters")
    selected_domain = st.selectbox("Select Domain", data['Domain'].unique())
    selected_state = st.selectbox("Select State", data['State'].unique())
    selected_college = st.selectbox("Select College", data['College'].unique())

    filtered_data = data[(data['Domain'] == selected_domain) & 
                         (data['State'] == selected_state) & 
                         (data['College'] == selected_college)]

    # App mode selection on the main screen
    app_mode = st.selectbox("Choose an option", ["Data Analysis", "Image Processing"])

    if app_mode == "Data Analysis":
        st.header("Data Analysis")
        
        if st.button("Analyze Data"):
            try:
                # Visualizations
                st.subheader("Participation Trends")
                
                # Domain-wise participation (Pie Chart)
                domain_counts = data['Domain'].value_counts()
                plt.figure(figsize=(10, 5))
                plt.pie(domain_counts, labels=domain_counts.index, autopct='%1.1f%%', startangle=140)
                plt.title('Domain-wise Participation')
                st.pyplot(plt)

                # Day-wise participation (Line Chart)
                plt.figure(figsize=(10, 5))
                day_counts = data['Date'].value_counts().sort_index()
                sns.lineplot(x=day_counts.index, y=day_counts.values)
                plt.title('Day-wise Participation')
                st.pyplot(plt)

                # College-wise participation (Horizontal Bar Chart)
                plt.figure(figsize=(10, 5))
                college_counts = data['College'].value_counts()
                sns.barplot(y=college_counts.index, x=college_counts.values, orient='h')
                plt.title('College-wise Participation')
                st.pyplot(plt)

                # State-wise participation (Donut Chart)
                state_counts = data['State'].value_counts()
                plt.figure(figsize=(10, 5))
                plt.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%', startangle=140, pctdistance=0.85)
                centre_circle = plt.Circle((0,0),0.70,fc='white')
                fig = plt.gcf()
                fig.gca().add_artist(centre_circle)
                plt.title('State-wise Participation')
                st.pyplot(plt)

                # Overall trends (e.g., scores) (Scatter Plot)
                plt.figure(figsize=(10, 5))
                sns.scatterplot(data=data, x='Participant ID', y='Score')
                plt.title('Overall Score Trends')
                st.pyplot(plt)

                # Generate Word Cloud for Domain-wise Feedback using NLTK
                st.subheader("Word Cloud for Feedback")
                feedback_data = data[data['Domain'] == selected_domain]['Feedback']
                feedback_text = ' '.join(feedback_data)

                # Text processing with NLTK
                tokens = word_tokenize(feedback_text)
                tokens = [word.lower() for word in tokens if word.isalpha()]  # Remove punctuation
                stop_words = set(stopwords.words('english'))
                filtered_tokens = [word for word in tokens if word not in stop_words]

                # Generate word cloud
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_tokens))
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                st.pyplot(plt)

            except Exception as e:
                st.error(f"Error analyzing data: {e}")

    elif app_mode == "Image Processing":
        st.header("Image Processing")
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
        day = st.selectbox("Select Day", [1, 2, 3])  # Example days
        if uploaded_file is not None:
            try:
                # Use Pillow to process the image
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)

                # Example processing: Convert to grayscale
                gray_image = image.convert("L")
                st.image(gray_image, caption="Processed Image (Grayscale)", use_column_width=True)

            except Exception as e:
                st.error(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
