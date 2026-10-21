---
id: A074
titulo: "Short-time/-angle spectral analysis for vibration monitoring of bearing failures under variable speed"
tipo: articulo
temas: [T09]
cluster: "C06 Diagnóstico de fallas y sistemas de energía"
palabras_clave: [fallas de rodamientos, vibraciones, velocidad variable, análisis espectral de corto plazo, entropía espectral]
fuente_resumen: abstract
anio: 2021
revista: "Applied Sciences"
doi: 10.3390/app11083369
citas_openalex: 12
fuentes: [0000043222]
---

# Short-time/-angle spectral analysis for vibration monitoring of bearing failures under variable speed

**Autores:** Edgar F. Sierra-Alonso, Julián Caicedo-Acosta, Alvaro Angel Orozco, Héctor Fabio Quintero Riaza, German Castellanos-Dominguez  
**Revista:** Applied Sciences (2021)  
**DOI:** https://doi.org/10.3390/app11083369  
**Temas:** T09 Monitoreo industrial y sistemas de energía  
**Clúster:** C06 Diagnóstico de fallas y sistemas de energía

## Aplicación
Monitoreo de vibraciones de fallas en rodamientos de maquinaria rotativa bajo velocidad variable.

## Problema de investigación
Con velocidad variable los eventos impulsivos de corta duración se diluyen y se pierde información de cambios de frecuencia.

## Propuesta o novedad
Se propone un estimador espectral de corto plazo con dos ventanas deslizantes (una corta para impulsos y una larga para el nivel de fondo) y un estimador de orden alto basado en entropía espectral para procesos ciclo-no-estacionarios.

## Resultados
Se evalúa con inspección visual y desempeño de clasificadores frente a la kurtosis espectral ampliamente usada.

## Conclusiones principales
El estimador resalta fallas impulsivas de rodamientos bajo velocidad variable.

## Métodos
- análisis espectral de corto plazo
- entropía espectral
- ventanas deslizantes

## Idea para trabajo futuro
Incorporar compensación angular para variación de velocidad en el estimador y probar en bancos con fallas reales.

## Relacionados (similitud semántica)
- extiende: [[A107-2019-filtered-evelope-spectrum-using-short-periodograms-for-beari]] — Filtered evelope spectrum using short periodograms for bearing fault identification under variable speed

<details><summary>Abstract</summary>

Vibration-condition monitoring aims to detect bearing damages of rotating machinery’s incipient failures mainly through time–frequency methods because of their efficient analysis of nonstationary signals. However, by having failures with impulse behavior, short-term events have a tendency to be diluted under variable-speed conditions, while information on frequency changes tends to be lost. Here, we introduce an approach to highlighting bearing impulsive failures by measuring short-term spectral components to deal with variable-speed vibrations. The short-term estimator employs two sliding windows: a small one that measures the instantaneous amplitude level and tracks impulsive components and a large interval that evaluates the average background amplitude. Aiming to characterize cyclo-non-stationary processes with impulsive behavior, the emphasizing high-order-based estimator based on the principle of spectral entropy is introduced. For evaluation, both visual inspection and classifier performance are assessed, contrasting the spectral-entropy estimator with the widely used spectral-kurtosis approach for dealing with impulsive signals. The validation of short-time/-angle spectral analysis performed on three datasets at variable speed showed that the proposed spectral-entropy estimator is a promising indicator for emphasizing bearing failures with impulse behavior.

</details>
