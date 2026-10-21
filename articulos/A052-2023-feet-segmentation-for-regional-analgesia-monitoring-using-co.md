---
id: A052
titulo: "Feet Segmentation for Regional Analgesia Monitoring Using Convolutional RFF and Layer-Wise Weighted CAM Interpretability"
tipo: articulo
temas: [T03, T07, T05]
cluster: "C09 Termografía y analgesia obstétrica"
palabras_clave: [analgesia neuroaxial, imágenes térmicas, segmentación semántica, random Fourier features, mapas de activación, parto]
fuente_resumen: abstract
anio: 2023
revista: "Computation"
doi: 10.3390/computation11060113
citas_openalex: 7
fuentes: [0000043222, 0001330950]
---

# Feet Segmentation for Regional Analgesia Monitoring Using Convolutional RFF and Layer-Wise Weighted CAM Interpretability

**Autores:** Juan Carlos Aguirre-Arango, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computation (2023)  
**DOI:** https://doi.org/10.3390/computation11060113  
**Temas:** T03 Imagen médica y neuroimagen; T07 Aprendizaje profundo y explicabilidad; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C09 Termografía y analgesia obstétrica

## Aplicación
Monitoreo de analgesia neuroaxial regional en parto mediante segmentación de pies en imágenes térmicas.

## Problema de investigación
La evaluación adecuada requiere monitoreo continuo tras la colocación del catéter, y los datos térmicos son pocos y variables.

## Propuesta o novedad
CRFFg, un enfoque con Convolutional Random Fourier Features, y mapas de activación ponderados por capas diseñados para segmentación de pies, aplicado para mejorar FCN, UNet y ResUNet.

## Resultados
En un conjunto de imágenes térmicas de pies de mujeres con anestesia epidural, logra resultados competitivos y mejora la explicabilidad del proceso. El resumen no entrega cifras.

## Conclusiones principales
Se mejora tanto la segmentación como su interpretabilidad en monitoreo de analgesia.

## Métodos
- CRFF
- UNet/ResUNet/FCN
- CAM ponderado por capas

## Idea para trabajo futuro
Correlacionar las regiones segmentadas con medidas clínicas de bloqueo sensitivo para validar el monitoreo.

## Relacionados (similitud semántica)
- extiende: [[A060-2021-random-fourier-features-based-deep-learning-improvement-with]] — Random fourier features-based deep learning improvement with class activation interpretability for nerve structure segmentation

<details><summary>Abstract</summary>

Regional neuraxial analgesia for pain relief during labor is a universally accepted, safe, and effective procedure involving administering medication into the epidural. Still, an adequate assessment requires continuous patient monitoring after catheter placement. This research introduces a cutting-edge semantic thermal image segmentation method emphasizing superior interpretability for regional neuraxial analgesia monitoring. Namely, we propose a novel Convolutional Random Fourier Features-based approach, termed CRFFg, and custom-designed layer-wise weighted class-activation maps created explicitly for foot segmentation. Our method aims to enhance three well-known semantic segmentation (FCN, UNet, and ResUNet). We have rigorously evaluated our methodology on a challenging dataset of foot thermal images from pregnant women who underwent epidural anesthesia. Its limited size and significant variability distinguish this dataset. Furthermore, our validation results indicate that our proposed methodology not only delivers competitive results in foot segmentation but also significantly improves the explainability of the process.

</details>
