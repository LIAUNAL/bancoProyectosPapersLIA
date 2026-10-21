---
id: A019
titulo: "Uncertainty-Aware Deep Learning for Robust and Interpretable MI EEG Using Channel Dropout and LayerCAM Integration"
tipo: articulo
temas: [T01, T07, T06]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, EEG, Monte Carlo dropout, LayerCAM, incertidumbre, BCI]
fuente_resumen: abstract
anio: 2025
revista: "Applied Sciences"
doi: 10.3390/app15148036
citas_openalex: 3
fuentes: [0001330950]
---

# Uncertainty-Aware Deep Learning for Robust and Interpretable MI EEG Using Channel Dropout and LayerCAM Integration

**Autores:** Óscar Wladimir Gómez Morales, Sofia Escalante-Escobar, Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Applied Sciences (2025)  
**DOI:** https://doi.org/10.3390/app15148036  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad; T06 Aprendizaje probabilístico y bayesiano  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Clasificación de imaginación motora (MI) con EEG para BCI y neurorrehabilitación.

## Problema de investigación
La variabilidad espaciotemporal y la baja interpretabilidad limitan la clasificación MI; el dropout puede eliminar canales críticos sensoriomotores.

## Propuesta o novedad
Un marco que integra channel dropout (variante de Monte Carlo dropout) con mapas de activación de clase (LayerCAM) para tratar la incertidumbre espaciotemporal y dar interpretabilidad neurofisiológica fina. Evalúa ShallowConvNet, EEGNet y TCNet Fusion.

## Resultados
En un conjunto MI-EEG de 52 sujetos, TCNet Fusion logró el pico de 74.4% con 32 canales y ShallowConvNet el menor, 72.7%. MCD mejoró la consistencia, con ganancias de hasta 10% en EEGNet y TCNet Fusion en sujetos de bajo desempeño, y topografías más focalizadas.

## Conclusiones principales
El enfoque unifica clasificación consciente de incertidumbre e interpretabilidad en MI.

## Métodos
- Monte Carlo dropout
- LayerCAM
- EEGNet
- ShallowConvNet
- TCNet Fusion

## Idea para trabajo futuro
Usar la incertidumbre estimada para adaptar en línea la selección de canales por sujeto en BCI.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Motor Imagery (MI) classification plays a crucial role in enhancing the performance of brain–computer interface (BCI) systems, thereby enabling advanced neurorehabilitation and the development of intuitive brain-controlled technologies. However, MI classification using electroencephalography (EEG) is hindered by spatiotemporal variability and the limited interpretability of deep learning (DL) models. To mitigate these challenges, dropout techniques are employed as regularization strategies. Nevertheless, the removal of critical EEG channels, particularly those from the sensorimotor cortex, can result in substantial spatial information loss, especially under limited training data conditions. This issue, compounded by high EEG variability in subjects with poor performance, hinders generalization and reduces the interpretability and clinical trust in MI-based BCI systems. This study proposes a novel framework integrating channel dropout—a variant of Monte Carlo dropout (MCD)—with class activation maps (CAMs) to enhance robustness and interpretability in MI classification. This integration represents a significant step forward by offering, for the first time, a dedicated solution to concurrently mitigate spatiotemporal uncertainty and provide fine-grained neurophysiologically relevant interpretability in motor imagery classification, particularly demonstrating refined spatial attention in challenging low-performing subjects. We evaluate three DL architectures (ShallowConvNet, EEGNet, TCNet Fusion) on a 52-subject MI-EEG dataset, applying channel dropout to simulate structural variability and LayerCAM to visualize spatiotemporal patterns. Results demonstrate that among the three evaluated deep learning models for MI-EEG classification, TCNet Fusion achieved the highest peak accuracy of 74.4% using 32 EEG channels. At the same time, ShallowConvNet recorded the lowest peak at 72.7%, indicating TCNet Fusion’s robustness in moderate-density montages. Incorporating MCD notably improved model consistency and classification accuracy, especially in low-performing subjects where baseline accuracies were below 70%; EEGNet and TCNet Fusion showed accuracy improvements of up to 10% compared to their non-MCD versions. Furthermore, LayerCAM visualizations enhanced with MCD transformed diffuse spatial activation patterns into more focused and interpretable topographies, aligning more closely with known motor-related brain regions and thereby boosting both interpretability and classification reliability across varying subject performance levels. Our approach offers a unified solution for uncertainty-aware, and interpretable MI classification.

</details>
