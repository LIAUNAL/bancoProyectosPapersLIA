---
id: A059
titulo: "Image-based animal recognition based on transfer learning"
tipo: articulo
temas: [T08, T10]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [reconocimiento de animales, transfer learning, redes convolucionales, imágenes de baja calidad, detección de vacas]
fuente_resumen: abstract
anio: 2021
revista: "Scientia et technica"
doi: 10.22517/23447214.24538
citas_openalex: 4
fuentes: [0001330950]
---

# Image-based animal recognition based on transfer learning

**Autores:** Diego Fabián Collazos-Huertas, Gloria Stephany Gómez Gómez, Andrés Marino Álvarez-Meza  
**Revista:** Scientia et technica (2021)  
**DOI:** https://doi.org/10.22517/23447214.24538  
**Temas:** T08 Visión por computador y análisis de video; T10 Agricultura de precisión, ambiente y teledetección  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Reconocimiento de animales (por ejemplo vacas) en imágenes de granjas para apoyar la gestión agropecuaria.

## Problema de investigación
El aprendizaje profundo exige grandes bases de datos y ajuste de hiperparámetros, y las imágenes de granja suelen ser ruidosas y de baja calidad.

## Propuesta o novedad
Se propone un enfoque de transfer learning que ajusta una CNN preentrenada para clasificar animales en imágenes ruidosas y de baja calidad.

## Resultados
Se probó una tarea perro vs. gato sobre CIFAR y una base propia vaca vs. no vaca, con desempeño de clasificación competitivo para distintas arquitecturas.

## Conclusiones principales
El transfer learning es una opción viable cuando se dispone de pocos datos y baja calidad de imagen.

## Métodos
- transfer learning
- CNN

## Idea para trabajo futuro
Ampliar la base de vacas a múltiples escenarios y evaluar detección individual y seguimiento en video.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Automatic image-based recognition systems have been widely used to solve different computer vision tasks. In particular, animals' identification in farms is a research field of interest for the computer vision and the agriculture community. It is then necessary to develop robust and precise algorithms to support detection, recognition, and monitoring tasks to enhance farm management. Traditionally, deep learning approaches have been proposed to solve image-based detection tasks. Nonetheless, databases holding many instances are required to achieve competitive performances, not mentioning the hyperparameters tuning issues. In this paper, we propose a transfer learning approach for image-based animal recognition. We enhance a pre-trained Convolutional Neural Network model for animal classification from noisy and low-quality images. First, a dog vs. cat task is tested from the well-known CIFAR database. Further, a cow vs. no cow database is built to test our transfer learning approach. The achieved results show competitive classification performance using different types of architectures compared to state-of-the-art methodologies.

</details>
