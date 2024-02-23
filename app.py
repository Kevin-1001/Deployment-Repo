import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('Classifying Iris Flowers')
st.markdown('Toy model to play to classify iris flowers into \
     (setosa, versicolor, virginica) based on their sepal/petal \
    and length/width.')

[https://www.google.com/url?sa=i&url=https%3A%2F%2Froadsendnaturalist.com%2F2020%2F05%2F04%2Fflower-parts-the-iris-have-it%2F&psig=AOvVaw3Vc_mA3fcDescvhbGs_cj1&ust=1708767722119000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCOCkwof1v4QDFQAAAAAdAAAAABAT]

st.header("Plant Features")
col1, col2 = st.columns(2)

with col1:
    st.text("Sepal characteristics")
    sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5)
    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)

with col2:
    st.text("Pepal characteristics")
    petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)
    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)

st.text('')
if st.button("Predict type of Iris"):
    result = predict(
        np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
    st.text(result[0])



st.text('')
st.text('')
st.markdown(
    '`Create by` [Kevin-1001](https://github.com/Kevin-1001/Kevin-1001) | \
         `Code:` [GitHub](https://github.com/Kevin-1001/Deployment-Repo/blob/main/app.py)')
