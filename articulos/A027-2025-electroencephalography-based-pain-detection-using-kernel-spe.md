---
id: A027
titulo: "Electroencephalography-based pain detection using kernel spectral connectivity network with preserved spatio-frequency interpretability"
tipo: articulo
temas: [T04, T02, T07]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [dolor crónico, EEG, conectividad funcional, class activation mapping, generalización entre sujetos, pacientes no verbales]
fuente_resumen: abstract
anio: 2025
revista: "Applied Sciences"
doi: 10.20944/preprints202503.1899.v1
citas_openalex: 2
fuentes: [0001330950]
---

# Electroencephalography-based pain detection using kernel spectral connectivity network with preserved spatio-frequency interpretability

**Autores:** Santiago Buitrago-Osorio, Julián Gil-González, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, Alvaro Angel Orozco  
**Revista:** Applied Sciences (2025)  
**DOI:** https://doi.org/10.20944/preprints202503.1899.v1  
**Temas:** T04 Bioseñales y soporte al diagnóstico clínico; T02 Conectividad cerebral e imagen de fuentes neuronales; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Detección de dolor crónico con EEG, incluso en pacientes no verbales.

## Problema de investigación
La evaluación del dolor es subjetiva y los métodos clínicos pueden ser imprecisos con pacientes no verbales; el EEG sufre ruido, conducción de volumen y variabilidad intersujeto.

## Propuesta o novedad
Marco con tres componentes: KCS-FCnet (Kernel Cross-Spectral Gaussian Functional Connectivity Network) para codificar dependencias entre canales, una estrategia de class activation mapping en frecuencia para interpretabilidad espacio-frecuencia y un análisis entre sujetos que agrupa individuos por desempeño, conectividad, sexo y edad.

## Resultados
Se evaluó en el conjunto Brain Mediators of Pain, mostrando robustez en tareas de detección de dolor dependientes del sujeto y de generalización entre sujetos. El resumen no entrega cifras.

## Conclusiones principales
El marco conserva interpretabilidad espacio-frecuencia y aborda la variabilidad entre sujetos.

## Métodos
- KCS-FCnet
- CAM en frecuencia
- conectividad espectral cruzada
- clustering de sujetos

## Idea para trabajo futuro
Validar KCS-FCnet en pacientes no verbales reales, con anotaciones clínicas de dolor, para evaluar su utilidad en la práctica.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Chronic pain leads to not only physical discomfort but also psychological challenges, such as depression and anxiety, which contribute to a substantial healthcare burden. Still, pain detection and assessment remains a challenge due to its subjective nature. Indeed, current clinical methods may be inaccurate or unfeasible for non-verbal patients. Then, Electroencephalography (EEG) has emerged as a promising non-invasive tool for pain detection. However, EEG-based pain detection faces challenges such as noise, volume conduction effects, and high inter-subject variability. Deep Learning (DL) models have shown potential in overcoming these challenges by extracting nonlinear and discriminative patterns. Despite advancements, these models often require a subject-dependent approach and lack of interpretability. To address these limitations, we propose a threefold DL-based framework for coding EEG-based pain detection patterns. i) We employ the Kernel Cross-Spectral Gaussian Functional Connectivity Network (KCS-FCnet) to code pairwise channel dependencies for pain detection. ii) Furthermore, we introduce a frequency-based strategy for class activation mapping to visualize pertinent pain EEG features, thereby enhancing visual interpretability through spatio-frequency patterns. iii) Further, to account for subject variability, we conduct cross-subject analysis and grouping, clustering individuals based on similar pain detection performance, functional connectivity patterns, sex, and age. We evaluate our model using the Brain Mediators of Pain dataset and demonstrate its robustness through subject-dependent and cross-subject generalization tasks for pain detection on non-verbal patients.

</details>
