---
id: A101
titulo: "AKL-ABC: An Automatic Approximate Bayesian Computation Approach Based on Kernel Learning"
tipo: articulo
temas: [T06, T05]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [inferencia bayesiana aproximada, aprendizaje de kernel, selección automática, alineamiento de kernel centrado, teoría de grafos]
fuente_resumen: abstract
anio: 2019
revista: "Entropy"
doi: 10.3390/e21100932
citas_openalex: 3
fuentes: [0001330950]
---

# AKL-ABC: An Automatic Approximate Bayesian Computation Approach Based on Kernel Learning

**Autores:** Wilson González-Vanegas, Andrés Álvarez-Meza, José Alberto Hernández-Muriel, Alvaro Angel Orozco  
**Revista:** Entropy (2019)  
**DOI:** https://doi.org/10.3390/e21100932  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Inferencia bayesiana sin verosimilitud explícita en problemas sintéticos y reales.

## Problema de investigación
ABC depende de la selección de parámetros libres con costosa sintonización.

## Propuesta o novedad
Se propone AKL-ABC con etapa de aprendizaje de kernel que codifica similitudes mediante CKA automatizado por aprendizaje teórico-informacional, más selección de vecindad local (LNS) con grafos.

## Resultados
Resultados en datos sintéticos y reales muestran un método competitivo frente a ABC no automáticos.

## Conclusiones principales
AKL-ABC automatiza ABC con kernel learning.

## Métodos
- ABC
- CKA
- aprendizaje teórico-informacional
- LNS

## Idea para trabajo futuro
Aplicar AKL-ABC a modelos dinámicos complejos en biología o neurociencia.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Bayesian statistical inference under unknown or hard to asses likelihood functions is a very challenging task. Currently, approximate Bayesian computation (ABC) techniques have emerged as a widely used set of likelihood-free methods. A vast number of ABC-based approaches have appeared in the literature; however, they all share a hard dependence on free parameters selection, demanding expensive tuning procedures. In this paper, we introduce an automatic kernel learning-based ABC approach, termed AKL-ABC, to automatically compute posterior estimations from a weighting-based inference. To reach this goal, we propose a kernel learning stage to code similarities between simulation and parameter spaces using a centered kernel alignment (CKA) that is automated via an Information theoretic learning approach. Besides, a local neighborhood selection (LNS) algorithm is used to highlight local dependencies over simulations relying on graph theory. Attained results on synthetic and real-world datasets show our approach is a quite competitive method compared to other non-automatic state-of-the-art ABC techniques.

</details>
