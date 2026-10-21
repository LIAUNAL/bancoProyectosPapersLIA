---
id: A090
titulo: "Information potential variability for hyperparameter selection in the MMD distance"
tipo: articulo
temas: [T05]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [selección de hiperparámetros, discrepancia media máxima, ventana de Parzen, series de tiempo, separabilidad]
fuente_resumen: abstract
anio: 2019
revista: "Lecture notes in computer science"
doi: 10.1007/978-3-030-13469-3_33
citas_openalex: 0
fuentes: [0001330950]
---

# Information potential variability for hyperparameter selection in the MMD distance

**Autores:** Cristhian K. Valencia, Andrés Marino Álvarez-Meza, Edgar Alirio Valencia, Mauricio A. Álvarez, Alvaro Angel Orozco  
**Revista:** Lecture notes in computer science (2019)  
**DOI:** https://doi.org/10.1007/978-3-030-13469-3_33  
**Temas:** T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Selección de hiperparámetros de kernel para distancia MMD en clasificación de series de tiempo.

## Problema de investigación
Elegir un RKHS adecuado depende del hiperparámetro global del kernel.

## Propuesta o novedad
Se optimiza el hiperparámetro de kernel a través de la variabilidad del potencial de información (IPV) desde un estimador de densidad Parzen.

## Resultados
La estrategia estima RKHS favoreciendo separabilidad de los datos y logra exactitud promedio competitiva.

## Conclusiones principales
IPV es un criterio útil para seleccionar el kernel en MMD.

## Métodos
- MMD
- Parzen
- potencial de información

## Idea para trabajo futuro
Extender IPV a kernels multiescala con hiperparámetros por característica.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

This work searches for an RKHS by optimizing the global kernel hyperparameter which describes the information potential variations (IPV) from a Parzen-based probability density estimator, and shows that this strategy allows estimating suitable RK HSs favoring data separability and achieving competitive results in terms of the average classification accuracy.

</details>
