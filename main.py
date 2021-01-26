# Importando bibliotecas

import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

OUTPUT_WIDTH = 500


def main():
    our_image = Image.open("empty.png")
    
    #Main
    st.title("Masterclass Visão Computacional")
    st.markdown("My first project in **streamlit!**")
    st.text("Aplicações de OpenCV com Kernel para a montagem de uma ferramenta de filtros para imagens.")
    st.sidebar.title("Barra lateral")

    #Menu com opções de páginas
    opcoes_menu = ["Filtros","Sobre"]
    escolha = st.sidebar.selectbox("Escolha as opções",opcoes_menu)

    if escolha == 'Filtros':
        #Imagem inicial
        Image_file = st.file_uploader("Upload da foto para aplicar um filtro no menu lateral",type=['jpg','png','jpeg'])


        if Image_file is not None:
            our_image = Image.open(Image_file)
            st.text("Imagem Original")
            st.sidebar.image(our_image,width=150)

        #Filtros que podem ser aplicados

        filtros = st.sidebar.radio("Filtros",['Original','Grayscale','Desenho','Sépia','Canny','Blur'
            ,'Contraste','Brightness'])

        if filtros == 'Grayscale':
            converted_image = np.array(our_image.convert('RGB'))
            gray_image = cv2.cvtColor(converted_image,cv2.COLOR_RGB2GRAY)
            st.image(gray_image,width=OUTPUT_WIDTH)


        elif filtros == 'Desenho':
            converted_image = np.array(our_image.convert('RGB'))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
            inv_gray_image = 255 - gray_image
            blur_image = cv2.GaussianBlur(inv_gray_image,(21,21),0,0)
            sketch_image = cv2.divide(gray_image,255 - blur_image,scale=256)
            st.image(sketch_image,width=OUTPUT_WIDTH)


        elif filtros == 'Sépia':
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image,cv2.COLOR_RGB2BGR)
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            sepia_filter = cv2.filter2D(converted_image, -1, kernel)
            st.image(sepia_filter,channels= "BGR", width=OUTPUT_WIDTH)

        elif filtros == 'Blur':
            b_amout = st.sidebar.slider("Kernel (n x n)",3,81,9,step=2)
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image,cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (b_amout,b_amout),0,0)
            st.image(blur_image, channels="BGR", width=OUTPUT_WIDTH)


        elif filtros == 'Canny':
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            blur = cv2.GaussianBlur(converted_image, (11, 11), 0)
            canny_image = cv2.Canny(blur, 40, 100)
            st.image(canny_image, width=OUTPUT_WIDTH)


        elif filtros== 'Contraste':
            c_amount = st.sidebar.slider("Contraste",0.0,2.0,1.0)
            enhancer = ImageEnhance.Contrast(our_image)
            contrast_image = enhancer.enhance(c_amount)
            st.image(contrast_image,width=OUTPUT_WIDTH)

        elif filtros== 'Brightness':
            c_amount = st.sidebar.slider("Brightness",0.0,2.0,1.0)
            enhancer = ImageEnhance.Brightness(our_image)
            brightness_image = enhancer.enhance(c_amount)
            st.image(brightness_image,width=OUTPUT_WIDTH)

        elif filtros=='Original':
            st.image(our_image, width=OUTPUT_WIDTH)
        else:
            st.image(our_image, width=OUTPUT_WIDTH)

    elif escolha == 'Sobre':
         st.subheader("Este é um projeto da Masterclass do curso sigmoidal")
         st.markdown("Assim como esse projeto, temos outros tipos de aplicações e projetos em python no https://github.com/egustavo20/dataset_datascience")

if __name__ == '__main__':
    main()