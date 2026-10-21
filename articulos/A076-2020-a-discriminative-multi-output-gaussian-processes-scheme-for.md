---
id: A076
titulo: "A discriminative multi-output gaussian processes scheme for brain electrical activity analysis"
tipo: articulo
temas: [T06, T01]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [procesos gaussianos multi-salida, actividad eléctrica cerebral, EEG, kernel espectral, clasificación discriminativa]
fuente_resumen: abstract
anio: 2020
revista: "Applied Sciences"
doi: 10.3390/app10196765
citas_openalex: 5
fuentes: [0001330950]
---

# A discriminative multi-output gaussian processes scheme for brain electrical activity analysis

**Autores:** Cristian A. Torres-Valencia, Alvaro Angel Orozco, David  Augusto Cardenas Peña, Andrés Marino Álvarez-Meza, Mauricio A. Álvarez  
**Revista:** Applied Sciences (2020)  
**DOI:** https://doi.org/10.3390/app10196765  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T01 Interfaces cerebro-computador y decodificación EEG  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Análisis de actividad eléctrica cerebral con EEG para discriminar condiciones cognitivas.

## Problema de investigación
Se requieren modelos generativos que cuantifiquen relaciones entre canales y permitan discriminar condiciones.

## Propuesta o novedad
Se propone un esquema discriminativo con procesos gaussianos multi-salida (MOGP) con el kernel de mezcla multiespectral (MOSM), con canales como salidas y discriminación por verosimilitud de los modelos entrenados por clase.

## Resultados
El esquema modela adecuadamente las señales EEG y permite cuantificar relaciones entre canales.

## Conclusiones principales
Los MOGP con kernel espectral son una herramienta generativa para clasificar condiciones cerebrales.

## Métodos
- MOGP
- kernel MOSM
- verosimilitud

## Idea para trabajo futuro
Aplicar el esquema a EEG con muchos canales usando aproximaciones esparsas para escalar el MOGP.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

The study of brain electrical activity (BEA) from different cognitive conditions has attracted a lot of interest in the last decade due to the high number of possible applications that could be generated from it. In this work, a discriminative framework for BEA via electroencephalography (EEG) is proposed based on multi-output Gaussian Processes (MOGPs) with a specialized spectral kernel. First, a signal segmentation stage is executed, and the channels from the EEG are used as the model outputs. Then, a novel covariance function within the MOGP known as the multispectral mixture kernel (MOSM) allows us to find and quantify the relationships between different channels. Several MOGPs are trained from different conditions grouped in bi-class problems, and the discrimination is performed based on the likelihood score of the test signals against all the models. Finally, the mean likelihood is computed to predict the correspondence of new inputs with each class’s existing models. Results show that this framework allows us to model the EEG signals adequately using generative models and allows analyzing the relationships between channels of the EEG for a particular condition. At the same time, the set of trained MOGPs is well suited to discriminate new input data.

</details>
