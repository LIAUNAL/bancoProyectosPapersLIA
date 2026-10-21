---
id: A020
titulo: "EEG Signal prediction for motor imagery classification in brain-computer interfaces"
tipo: articulo
temas: [T01]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, BCI, elastic net, reducción de electrodos, predicción de señal EEG, extracción de características]
fuente_resumen: abstract
anio: 2025
revista: "Sensors"
doi: 10.3390/s25072259
citas_openalex: 11
fuentes: [0001330950]
---

# EEG Signal prediction for motor imagery classification in brain-computer interfaces

**Autores:** Óscar Wladimir Gómez Morales, Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2025)  
**DOI:** https://doi.org/10.3390/s25072259  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Clasificación MI en BCI con pocos electrodos, reduciendo costo y tiempo de preparación.

## Problema de investigación
Los BCI de MI requieren muchos electrodos, lo que implica preparación larga, costo y riesgo de perder información si un electrodo falla.

## Propuesta o novedad
Un método de predicción de señal con regresión elastic net que estima 22 canales completos a partir de solo 8 canales centrales, y luego extrae características y clasifica con las señales predichas.

## Resultados
Alcanzó 78.16% de exactitud promedio, superando el enfoque tradicional con pocos canales y el de canal completo. La exactitud por sujeto varía de 62.30% a 95.24%.

## Conclusiones principales
Es viable obtener estimaciones precisas con un conjunto reducido de electrodos, favoreciendo BCI prácticos.

## Métodos
- elastic net
- predicción de EEG
- CSP/características
- clasificación MI

## Idea para trabajo futuro
Reemplazar la regresión lineal por modelos no lineales o generativos para reconstruir canales y comparar con interpolación espacial.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Brain-computer interfaces (BCIs) based on motor imagery (MI) generally require EEG signals recorded from a large number of electrodes distributed across the cranial surface to achieve accurate MI classification. Not only does this entail long preparation times and high costs, but it also carries the risk of losing valuable information when an electrode is damaged, further limiting its practical applicability. In this study, a signal prediction-based method is proposed to achieve high accuracy in MI classification using EEG signals recorded from only a small number of electrodes. The signal prediction model was constructed using the elastic net regression technique, allowing for the estimation of EEG signals from 22 complete channels based on just 8 centrally located channels. The predicted EEG signals from the complete channels were used for feature extraction and MI classification. The results obtained indicate a notable efficacy of the proposed prediction method, showing an average performance of 78.16% in classification accuracy. The proposed method demonstrated superior performance compared to the traditional approach that used few-channel EEG and also achieved better results than the traditional method based on full-channel EEG. Although accuracy varies among subjects, from 62.30% to an impressive 95.24%, these data indicate the capability of the method to provide accurate estimates from a reduced set of electrodes. This performance highlights its potential to be implemented in practical MI-based BCI applications, thereby mitigating the time and cost constraints associated with systems that require a high density of electrodes.

</details>
