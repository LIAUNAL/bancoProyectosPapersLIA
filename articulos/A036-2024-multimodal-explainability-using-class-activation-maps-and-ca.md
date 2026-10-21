---
id: A036
titulo: "Multimodal Explainability Using Class Activation Maps and Canonical Correlation for MI-EEG Deep Learning Classification"
tipo: articulo
temas: [T01, T07]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, EEG, class activation maps, correlación canónica, BCI, explicabilidad multimodal]
fuente_resumen: abstract
anio: 2024
revista: "Applied Sciences"
doi: 10.3390/app142311208
citas_openalex: 5
fuentes: [0001330950]
---

# Multimodal Explainability Using Class Activation Maps and Canonical Correlation for MI-EEG Deep Learning Classification

**Autores:** Marcos Loaiza-Arias, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, Alvaro Angel Orozco, German Castellanos-Dominguez  
**Revista:** Applied Sciences (2024)  
**DOI:** https://doi.org/10.3390/app142311208  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Interpretación multimodal de clasificación MI-EEG en BCI, relacionando desempeño con cuestionarios fisiológicos.

## Problema de investigación
El EEG es ruidoso, varía entre personas por factores genéticos y cognitivos, y dificulta soluciones independientes del sujeto.

## Propuesta o novedad
MEDL (Multimodal and Explainable Deep Learning): evalúa modelos profundos de MI-EEG dependientes del sujeto, usa Class Activation Mapping para visualizar características relevantes y QMIP-CCA (Questionnaire-MI Performance Canonical Correlation Analysis) para interpretabilidad multidominio.

## Resultados
En el conjunto GIGAScience MI, las redes superficiales clasifican bien el MI-EEG, el método CAM halla patrones espacio-frecuencia y QMIP-CCA correlaciona datos fisiológicos con el desempeño.

## Conclusiones principales
El marco ofrece una solución interpretable mejorada para BCI.

## Métodos
- CAM
- CCA
- redes superficiales
- QMIP-CCA

## Idea para trabajo futuro
Predecir tempranamente el desempeño BCI de un usuario a partir de cuestionarios y diseñar protocolos de entrenamiento personalizados.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Brain-Computer Interfaces (BCIs) are essential in advancing medical diagnosis and treatment by providing non-invasive tools to assess neurological states. Among these, Motor Imagery (MI), where patients mentally simulate motor tasks without physical movement, has proven to be an effective paradigm for diagnosing and monitoring neurological conditions. Electroencephalography (EEG) is widely used for MI data collection due to its high temporal resolution, cost-effectiveness, and portability. However, EEG signals can be noisy from a number of sources, including physiological artifacts and electromagnetic interference. They can also vary from person to person, which makes it harder to extract features and understand the signals. Additionally, this variability, influenced by genetic and cognitive factors, presents challenges for developing subject-independent solutions. To address these limitations, this paper presents a Multimodal and Explainable Deep Learning (MEDL) approach for MI-EEG classification and physiological interpretability. Our approach involves: i) evaluating different deep learning (DL) models for subject-dependent MI-EEG discrimination; ii) employing Class Activation Mapping (CAM) to visualize relevant MI-EEG features; and iii) utilizing a Questionnaire-MI Performance Canonical Correlation Analysis (QMIP-CCA) to provide multidomain interpretability. On the GIGAScience MI dataset, experiments show that shallow neural networks are good at classifying MI-EEG data, while the CAM-based method finds spatio-frequency patterns. Moreover, the QMIP-CCA framework successfully correlates physiological data with MI-EEG performance, offering an enhanced, interpretable solution for BCIs.

</details>
