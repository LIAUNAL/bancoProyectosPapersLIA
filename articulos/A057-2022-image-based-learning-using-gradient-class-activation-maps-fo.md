---
id: A057
titulo: "Image-based learning using gradient class activation maps for enhanced physiological interpretability of motor imagery skills"
tipo: articulo
temas: [T01, T07]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, BCI, Grad-CAM, EEG, redes convolucionales, variabilidad interindividual]
fuente_resumen: abstract
anio: 2022
revista: "Applied Sciences"
doi: 10.3390/app12031695
citas_openalex: 9
fuentes: [0000043222, 0001330950]
---

# Image-based learning using gradient class activation maps for enhanced physiological interpretability of motor imagery skills

**Autores:** Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Applied Sciences (2022)  
**DOI:** https://doi.org/10.3390/app12031695  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Interfaces cerebro-computador basadas en imaginación motora con EEG, con foco en interpretabilidad fisiológica.

## Problema de investigación
La alta variabilidad inter e intra-sujeto de las señales EEG limita el desempeño de los BCI y dificulta entender las habilidades individuales.

## Propuesta o novedad
Se desarrolla una red convolucional Deep and Wide alimentada con topoplots de EEG multicanal, y se aplica GradCam++ en distintos intervalos de la tarea para visualizar la dinámica espacial; los mapas se agrupan entre sujetos para entender la coordinación MI-BCI.

## Resultados
El enfoque mejora la exactitud de la discriminación de tareas MI y permite interpretar la contribución espacial en el tiempo.

## Conclusiones principales
Los mapas de activación de clase aportan una lectura fisiológica de las habilidades MI y de su variabilidad entre sujetos.

## Métodos
- CNN Deep&Wide
- GradCam++
- topoplots
- agrupamiento

## Idea para trabajo futuro
Usar los mapas de relevancia por sujeto para diseñar protocolos de entrenamiento MI personalizados para usuarios de bajo desempeño.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Brain activity stimulated by the motor imagery paradigm (MI) is measured by Electroencephalography (EEG), which has several advantages to be implemented with the widely used Brain–Computer Interfaces (BCIs) technology. However, the substantial inter/intra variability of recorded data significantly influences individual skills on the achieved performance. This study explores the ability to distinguish between MI tasks and the interpretability of the brain’s ability to produce elicited mental responses with improved accuracy. We develop a Deep and Wide Convolutional Neuronal Network fed by a set of topoplots extracted from the multichannel EEG data. Further, we perform a visualization technique based on gradient-based class activation maps (namely, GradCam++) at different intervals along the MI paradigm timeline to account for intra-subject variability in neural responses over time. We also cluster the dynamic spatial representation of the extracted maps across the subject set to come to a deeper understanding of MI-BCI coordination skills. According to the results obtained from the evaluated GigaScience Database of motor-evoked potentials, the developed approach enhances the physiological explanation of motor imagery in aspects such as neural synchronization between rhythms, brain lateralization, and the ability to predict the MI onset responses and their evolution during training sessions.

</details>
