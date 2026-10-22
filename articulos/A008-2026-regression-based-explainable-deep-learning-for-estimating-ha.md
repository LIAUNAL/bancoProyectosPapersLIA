---
id: A008
titulo: "Regression-based explainable deep learning for estimating Hamiltonian parameters from magnetic nanodot images"
tipo: articulo
temas: [T07, T13, T17]
cluster: "C13 Materiales, celdas solares y física computacional"
palabras_clave: [nanodiscos magnéticos, interacción Dzyaloshinskii-Moriya, skyrmions, recocido simulado, mapas de activación de regresión, Vision Transformer]
fuente_resumen: abstract
anio: 2026
revista: "Materials & Design"
doi: 10.1016/j.matdes.2026.116816
citas_openalex: 0
fuentes: [0001330950]
---

# Regression-based explainable deep learning for estimating Hamiltonian parameters from magnetic nanodot images

**Autores:** Juan Sebastián Méndez-Rondón, María Isabel García-Quimbayo, Andrés Marino Álvarez-Meza, Jorge Montes-Monsalve, J.D. Agudelo-Giraldo  
**Revista:** Materials & Design (2026)  
**DOI:** https://doi.org/10.1016/j.matdes.2026.116816  
**Temas:** T07 Aprendizaje profundo y explicabilidad; T13 Representación de datos, reducción de dimensión y agrupamiento; T17 Materiales y celdas solares  
**Clúster:** C13 Materiales, celdas solares y física computacional

## Aplicación
Estimación de parámetros del hamiltoniano de Heisenberg extendido a partir de imágenes de magnetización de nanodiscos magnéticos.

## Problema de investigación
Inferir parámetros atomísticos a partir de imágenes 2D es un problema inverso mal planteado, con texturas ruidosas y simulaciones lentas; los estimadores profundos son cajas negras.

## Propuesta o novedad
Una metodología de regresión explicable: una descomposición matricial del hamiltoniano permite Monte Carlo Metropolis-Hastings con recocido simulado acelerado por GPU, y los Regression Activation Maps (RAM), una métrica de atribución basada en error, vuelven al modelo una caja gris trazable.

## Resultados
Regresores convolucionales y Vision Transformer recuperan de forma fiable los parámetros físicos en imágenes simuladas, aunque las constantes de intercambio de orden superior quedan limitadas por la identificabilidad de la proyección sz. Los RAM aíslan paredes de dominio quirales y núcleos de skyrmion.

## Conclusiones principales
La combinación de simulación acelerada y atribución por RAM permite estimación de parámetros más transparente y eficiente.

## Métodos
- CNN
- Vision Transformer
- Monte Carlo Metropolis-Hastings
- Regression Activation Maps

## Idea para trabajo futuro
Validar los RAM con imágenes experimentales y analizar la identificabilidad de los parámetros de orden superior con más proyecciones de espín.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Magnetic nanodots host topological spin textures whose stability is dictated by an extended Heisenberg Hamiltonian combining symmetric exchange, the Dzyaloshinskii–Moriya interaction, magnetocrystalline anisotropy, and the Zeeman field. Inferring these atomistic parameters from two-dimensional magnetization images underpins the design of functional magnetic materials, yet it remains an ill-posed inverse problem: under certain external conditions and transient states, configurations relax into noisy, weakly discriminative textures that render the dataset ill-conditioned. Deep-learning estimators act as opaque black boxes and rely on slow atomistic simulations. We propose an explainable regression methodology whose novelty lies in data generation and interpretability: a matrix decomposition of the extended Hamiltonian enables GPU-accelerated Metropolis–Hastings Monte Carlo with simulated annealing, accelerating computation without altering the underlying physics, while Regression Activation Maps (RAMs), a novel error-based attribution metric, turn the network into a traceable gray-box model. Trained on several configurations, convolutional and Vision Transformer regressors reliably recover the physical parameters from simulated nanodot images, while the higher-order exchange constants remain bounded by the intrinsic identifiability limits of the s z projection. Comparing both families through their attention maps and accuracy-versus-size trade-off, RAMs isolate the chiral domain walls and skyrmion cores driving predictions.

</details>
