---
id: A077
titulo: "A machine learning approach to support deep brain stimulation programming"
tipo: articulo
temas: [T03, T04]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [estimulación cerebral profunda, volumen de tejido activado, aprendizaje de métrica, vecinos más cercanos, regresión]
fuente_resumen: abstract
anio: 2020
revista: "Revista Facultad de Ingeniería Universidad de Antioquia"
doi: 10.17533/udea.redin.20190729
citas_openalex: 4
fuentes: [0001330950]
---

# A machine learning approach to support deep brain stimulation programming

**Autores:** Viviana Gómez-Orozco, Iván De La Pava Panche, Andrés Marino Álvarez-Meza, Mauricio A. Álvarez, Alvaro Angel Orozco  
**Revista:** Revista Facultad de Ingeniería Universidad de Antioquia (2020)  
**DOI:** https://doi.org/10.17533/udea.redin.20190729  
**Temas:** T03 Imagen médica y neuroimagen; T04 Bioseñales y soporte al diagnóstico clínico  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Programación de estimulación cerebral profunda (DBS) en pacientes, apoyando el ajuste de parámetros.

## Problema de investigación
El ajuste de parámetros DBS se hace por ensayo y error aun con visualización del volumen de tejido activado (VTA).

## Propuesta o novedad
Se propone un enfoque en dos etapas: deformación basada en K vecinos más cercanos para definir un VTA objetivo viable y estimación de parámetros con aprendizaje de métrica y regresión/clasificación.

## Resultados
La metodología permite estimar los parámetros DBS para producir un VTA objetivo bajo restricciones biofísicas.

## Conclusiones principales
El aprendizaje automático puede reducir el ensayo y error en la programación DBS.

## Métodos
- K-NN
- aprendizaje de métrica
- regresión

## Idea para trabajo futuro
Validar con pacientes reales comparando la respuesta clínica entre parámetros sugeridos y ajuste manual.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Adjusting the stimulation parameters is a challenge in deep brain stimulation (DBS) therapy due to the vast number of different configurations available. As a result, systems based on the visualization of the volume of tissue activated (VTA) produced by a particular stimulation setting have been developed. However, the medical specialist still has to search, by trial and error, for a DBS set-up that generates the desired VTA. Therefore, our goal is developing a DBS parameter tuning strategy for current clinical devices that allows defining a target VTA under biophysically viable constraints. We propose a machine learning approach that allows estimating the DBS parameter values for a given VTA, which comprises two main stages: i) A K-nearest neighbors-based deformation to define a target VTA preserving biophysically viable constraints. ii) A parameter estimation stage that consists of a data projection using metric learning to highlight relevant VTA properties, and a regression/classification algorithm to estimate the DBS parameters that generate the target VTA. Our methodology allows setting a biophysically compliant target VTA and accurately predicts the required configuration of stimulation parameters. Also, the performance of our approach is stable for both isotropic and anisotropic tissue conductivities. Furthermore, the computational cost of the trained system is acceptable for real-world implementations.

</details>
