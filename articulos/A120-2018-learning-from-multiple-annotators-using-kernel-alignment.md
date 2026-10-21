---
id: A120
titulo: "Learning from multiple annotators using kernel alignment"
tipo: articulo
temas: [T06, T05]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [múltiples anotadores, ruido en etiquetas, alineamiento de kernel, agregación de etiquetas, experticia del anotador]
fuente_resumen: abstract
anio: 2018
revista: "Pattern Recognition Letters"
doi: 10.1016/j.patrec.2018.10.005
citas_openalex: 19
fuentes: [0001330950]
---

# Learning from multiple annotators using kernel alignment

**Autores:** Julián Gil-González, Andrés Marino Álvarez-Meza, Alvaro Angel Orozco  
**Revista:** Pattern Recognition Letters (2018)  
**DOI:** https://doi.org/10.1016/j.patrec.2018.10.005  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Aprendizaje supervisado con etiquetas ruidosas de múltiples anotadores.

## Problema de investigación
Sin etiqueta de referencia, métodos triviales como el voto mayoritario asumen anotadores homogéneos.

## Propuesta o novedad
Se introduce KAAR, un análisis de relevancia de anotadores basado en alineamiento de kernel que codifica la experticia de cada anotador como el ajuste promedio entre las características de entrada y las etiquetas; la etiqueta nueva se predice como combinación convexa de clasificadores ponderados por KAAR.

## Resultados
Los experimentos muestran que se puede estimar el desempeño de los anotadores incluso sin patrón de oro, superando técnicas del estado del arte.

## Conclusiones principales
El alineamiento de kernel es una vía efectiva para valorar anotadores y agregar etiquetas.

## Métodos
- KAAR
- alineamiento de kernel
- combinación convexa de clasificadores

## Idea para trabajo futuro
Modelar la experticia dependiente de la instancia y probar el método en anotación médica real.

## Relacionados (similitud semántica)
- extendido por: [[A072-2021-learning-from-multiple-inconsistent-and-dependent-annotators]] — Learning from multiple inconsistent and dependent annotators to support classification tasks

<details><summary>Abstract</summary>

Abstract In a typical supervised learning scenario, it is supposed that there is an oracle who gives the correct label (also known as gold standard or ground truth) for each instance available in the training set. Nevertheless, for many real-world problems, instead of the gold standard, we have access to some annotations (possibly noisy) provided by multiple annotators with different unknown levels of expertise. Then, it is not appropriate to use trivial methods, i.e., majority voting, to estimate the actual label from the annotations due to this way assumes homogeneity in the performance of the labelers. Here, we introduce a new kernel alignment-based annotator relevance analysis–(KAAR) approach to code each annotator expertise as an averaged matching between the input features and the expert labels. So, a new sample label is predicted as a convex combination of classifiers adopting the achieved KAAR-based coding. Experimental results show that our methodology can estimate the performance of annotators even if the gold standard is not available, defeating state-of-the-art techniques.

</details>
