---
id: A073
titulo: "Adaptive classification using incremental learning for seismic-volcanic signals with concept drift"
tipo: articulo
temas: [T04, T09]
cluster: "C06 Diagnóstico de fallas y sistemas de energía"
palabras_clave: [deriva conceptual, aprendizaje incremental, señales sismo-volcánicas, ensamble de clasificadores, volcán Villarrica]
fuente_resumen: abstract
anio: 2021
revista: "Journal of Volcanology and Geothermal Research"
doi: 10.1016/j.jvolgeores.2021.107211
citas_openalex: 12
fuentes: [0000043222]
---

# Adaptive classification using incremental learning for seismic-volcanic signals with concept drift

**Autores:** Paola Alexandra Castro-Cabrera, German Castellanos-Dominguez, Carlos Mera, Luis Franco, Mauricio Orozco‐Alzate  
**Revista:** Journal of Volcanology and Geothermal Research (2021)  
**DOI:** https://doi.org/10.1016/j.jvolgeores.2021.107211  
**Temas:** T04 Bioseñales y soporte al diagnóstico clínico; T09 Monitoreo industrial y sistemas de energía  
**Clúster:** C06 Diagnóstico de fallas y sistemas de energía

## Aplicación
Clasificación de señales sísmico-volcánicas del volcán Villarrica para evaluar la actividad volcánica.

## Problema de investigación
Los clasificadores asumen estacionariedad, ignorando el cambio de los fenómenos volcánicos en el tiempo (concept drift).

## Propuesta o novedad
Se propone una estrategia adaptativa de aprendizaje incremental que identifica y aprende deriva conceptual en flujos de datos sísmicos, usando un ensamble que maneja estados recurrentes y clasifica aun sin etiquetas verdaderas disponibles.

## Resultados
Se realizaron experimentos con datos sísmicos del volcán Villarrica con un protocolo distinto al usual del estado del arte.

## Conclusiones principales
El ensamble incremental permite adaptarse a la no estacionariedad de la actividad volcánica.

## Métodos
- aprendizaje incremental
- ensamble de clasificadores
- detección de deriva

## Idea para trabajo futuro
Integrar el sistema en monitoreo en tiempo real con alertas de cambio de régimen volcánico.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Abstract The accurate labeling of the volcanic earthquake signals is a crucial task in order to estimate the increase in volcanic activity (among other parameters), which contributes to determine a state of volcanic unrest (as a possible precursor of an eruption). Several automatic classification approaches have been proposed in different computer science areas in order to complement the exhaustive human task of manually labeling volcano-seismic events. However, most of these approaches have been designed under the assumption of stationarity; that is, by discarding the changing nature of the volcanic phenomenon that evolves over time. In this work, an adaptive classification strategy based on incremental learning is proposed, which identifies and learns concept drifts of data streams coming from seismic recordings. The proposed strategy uses a classifier ensemble in order to handle recurrent states and classifies data even while true labels are not yet available. Unlike usual experimental protocols in the state–of–the–art, we carried out experiments with seismic data from Villarrica volcano, considering the chronological order of the data during a long period (more than 4 years of registration) to achieve the detection of drifts. The results show that the proposed classification strategy satisfactorily counteracts the changes, in contrast to standard classifiers trained within a traditional learning scheme. The proposed strategy keeps a stable classification accuracy and achieves a reduction of up to 0.28 of the absolute error in episodes of abrupt changes.

</details>
