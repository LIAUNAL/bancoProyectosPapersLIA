---
id: A031
titulo: "A Regularized Physics-Informed Neural Network to Support Data-Driven Nonlinear Constrained Optimization"
tipo: articulo
temas: [T09, T07]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [PINN, programación no lineal, regularización, optimización no convexa, optimización robusta, diferenciación automática]
fuente_resumen: abstract
anio: 2024
revista: "Computers"
doi: 10.3390/computers13070176
citas_openalex: 9
fuentes: [0000043222, 0001330950]
---

# A Regularized Physics-Informed Neural Network to Support Data-Driven Nonlinear Constrained Optimization

**Autores:** Diego Armando Pérez-Rosero, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computers (2024)  
**DOI:** https://doi.org/10.3390/computers13070176  
**Temas:** T09 Monitoreo industrial y sistemas de energía; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Optimización no lineal con restricciones guiada por datos para ingeniería, economía e investigación de operaciones.

## Problema de investigación
La optimización no lineal es sensible a la variabilidad de datos y a mediciones ruidosas, y las restricciones no lineales causan soluciones infactibles o subóptimas.

## Propuesta o novedad
RPINN, una red neuronal informada por la física regularizada, con funciones de activación personalizadas y penalizaciones de regularización. Calcula las variables de optimización a partir de pesos y características aprendidas, y entrena con diferenciación automática por lotes.

## Resultados
En tareas supervisadas y no supervisadas, RPINN ofrece soluciones competitivas frente a solucionadores del estado del arte y es robusta a mediciones ruidosas.

## Conclusiones principales
La base en redes neuronales aporta flexibilidad y escalabilidad útiles donde la información fluctúa.

## Métodos
- PINN
- regularización
- diferenciación automática

## Idea para trabajo futuro
Aplicar RPINN a problemas de despacho energético con incertidumbre y comparar costo computacional con solvers comerciales.

## Relacionados (similitud semántica)
- derivado del proyecto: [[H53871-2021-gestion-de-operaciones-logisticas-aplicada-al-sector-de-alim]] — Gestión de operaciones logísticas aplicada al sector de alimentos.

<details><summary>Abstract</summary>

Nonlinear optimization (NOPT) is a meaningful tool for solving complex tasks in fields like engineering, economics, and operations research, among others. However, NOPT has problems when it comes to dealing with data variability and noisy input measurements that lead to incorrect solutions. Furthermore, nonlinear constraints may result in outcomes that are either infeasible or suboptimal, such as non-convex optimization. This paper introduces a novel regularized physics-informed neural network (RPINN) framework as a new NOPT tool for both supervised and unsupervised data-driven scenarios. By using custom activation functions and regularization penalties in an artificial neural network (ANN), RPINN can handle data variability and noisy inputs. Besides, it uses physics principles to build the network architecture, computing the optimization variables based on network weights and learned features. In addition, it uses automatic differentiation training to make the system scalable and cut down on computation time through batch-based back-propagation. The test results for both supervised and unsupervised NOPT tasks show that our RPINN can provide solutions that are competitive compared to state-of-the-art solvers. In turn, RPINN’s robustness against noisy input measurements makes it particularly valuable in environments with fluctuating information. Additionally, RPINN’s ANN-based foundation offers significant flexibility and scalability.

</details>
