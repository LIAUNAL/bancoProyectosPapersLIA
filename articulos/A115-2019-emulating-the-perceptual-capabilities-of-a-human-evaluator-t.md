---
id: A115
titulo: "Emulating the perceptual capabilities of a human evaluator to map the GRB scale for the assessment of voice disorders"
tipo: articulo
temas: [T11, T06]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [trastornos de voz, escala GRB, evaluación perceptual, clasificación ordinal, regresión gaussiana, robustez entre bases de datos]
fuente_resumen: abstract
anio: 2019
revista: "Engineering Applications of Artificial Intelligence"
doi: 10.1016/j.engappai.2019.03.027
citas_openalex: 16
fuentes: [0000043222]
---

# Emulating the perceptual capabilities of a human evaluator to map the GRB scale for the assessment of voice disorders

**Autores:** Jorge A. Gómez-García, Laureano Moro-Velázquez, Janaína Mendes-Laureano, German Castellanos-Dominguez, Juan Ignacio Godino-Llorente  
**Revista:** Engineering Applications of Artificial Intelligence (2019)  
**DOI:** https://doi.org/10.1016/j.engappai.2019.03.027  
**Temas:** T11 Procesamiento de voz, audio y música; T06 Aprendizaje probabilístico y bayesiano  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Evaluación automática de la calidad de voz en trastornos vocales según la escala GRB.

## Problema de investigación
Las evaluaciones perceptuales de la voz son subjetivas y discretas; se requiere emular al evaluador humano.

## Propuesta o novedad
Se propone una metodología con múltiples conjuntos de características, clasificación ordinal y regresión gaussiana, que identifica un subconjunto reducido de características y convierte la escala perceptual discreta en continua.

## Resultados
En experimentos entre bases de datos, la desviación promedio respecto al experto es de unas 0.5 unidades (escala 0 a 3) para G y B y 0.7 para R. También se realizó una evaluación clínica de las predicciones.

## Conclusiones principales
Es posible extender la escala GRB a un continuo mediante regresión manteniendo la consistencia de los resultados.

## Métodos
- regresión por procesos gaussianos
- clasificación ordinal
- selección de características

## Idea para trabajo futuro
Validar el sistema con más evaluadores clínicos y modelar explícitamente la incertidumbre y desacuerdo entre expertos.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Abstract This paper presents the design of an automatic voice quality analysis system for the assessment of voice pathologies, which emulates the perceptual capabilities of a human evaluator according the GRB scale. For this purpose, a novel methodology based on multiple sets of characteristics, ordinal classification and Gaussian regression is proposed. In particular, a reduced subset of characteristics is identified, and the regressor is used to convert the discrete perceptual scale to a continuum, more in agreement to the nature of the problem under study. The robustness of the system is evaluated in several cross-dataset experiments. Similarly, a clinical evaluation of the predictions provided by the system is carried out. Results indicate that the proposed methodology is proficient in modelling the perceptual capabilities of the human evaluator. They also show that it is possible to extend the GRB scale to a continuum through regression techniques while maintaining the consistency of the results. On average, the deviation between the labels assessed by the expert and the ones provided by the system is of about 0.5 units (in a scale from 0 to 3) for G and B, and of 0.7 units for R. Similarly, the deviation of the labels predicted by the system in the clinical assessment trials is about 0.3 units for G, 0.4 units for B, and 0.5 units for R.

</details>
