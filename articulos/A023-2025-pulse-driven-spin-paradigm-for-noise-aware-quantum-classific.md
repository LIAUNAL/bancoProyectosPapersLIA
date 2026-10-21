---
id: A023
titulo: "Pulse-Driven Spin Paradigm for Noise-Aware Quantum Classification"
tipo: articulo
temas: [T05, T07]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [aprendizaje automático cuántico, re-carga de datos, qubits de espín, ruido NISQ, control por pulsos, pérdida por divergencia]
fuente_resumen: abstract
anio: 2025
revista: "Computers"
doi: 10.3390/computers14110475
citas_openalex: 0
fuentes: [0001330950]
---

# Pulse-Driven Spin Paradigm for Noise-Aware Quantum Classification

**Autores:** Carlos Riascos-Moreno, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computers (2025)  
**DOI:** https://doi.org/10.3390/computers14110475  
**Temas:** T05 Métodos kernel y aprendizaje basado en teoría de la información; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Clasificación cuántica con circuitos de re-carga de datos (DRU) en procesadores cuánticos basados en espín, en la era NISQ.

## Problema de investigación
No existen implementaciones de DRU en procesadores cuánticos de espín, y el ruido, los errores de compuerta y la decoherencia exigen estrategias conscientes del ruido.

## Propuesta o novedad
Un marco a nivel de pulso: compila circuitos DRU en controles temporales derivados del hamiltoniano de Loss-DiVincenzo, incorpora ruido coherente e incoherente (perturbaciones de pulso y canales de Lindblad) y propone un entrenamiento consciente del ruido con funciones de pérdida de teoría de la información.

## Resultados
Las simulaciones reproducen la dinámica a nivel de compuerta con fidelidades cercanas a uno y caracterizan mejor el error bajo ruido realista (configuraciones de uno, dos y cuatro espines). Las pérdidas basadas en divergencia mejoran la exactitud y robustez frente a las basadas en fidelidad.

## Conclusiones principales
El marco es una vía práctica para DRU en plataformas de espín y motiva trabajo en entrenamiento atento al error.

## Métodos
- Data Re-Uploading
- hamiltoniano de Loss-DiVincenzo
- canales de Lindblad
- pérdidas por divergencia

## Idea para trabajo futuro
Validar el marco con parámetros de ruido medidos en hardware real de puntos cuánticos de espín.

## Relacionados (similitud semántica)
- derivado del proyecto: [[H62836-2025-aprendizaje-de-maquina-cuantico-utilizando-espines-electroni]] — Aprendizaje de máquina cuántico utilizando espines electrónicos

<details><summary>Abstract</summary>

Quantum machine learning (QML) integrates quantum computing with classical machine learning. Within this domain, QML-CQ classification tasks, where classical data is processed by quantum circuits, have attracted particular interest for their potential to exploit high-dimensional feature maps, entanglement-enabled correlations, and non-classical priors. Yet, practical realizations remain constrained by the Noisy Intermediate-Scale Quantum (NISQ) era, where limited qubit counts, gate errors, and coherence losses necessitate frugal, noise-aware strategies. The Data Re-Uploading (DRU) algorithm has emerged as a strong NISQ-compatible candidate, offering universal classification capabilities with minimal qubit requirements. While DRU has been experimentally demonstrated on ion-trap, photonic, and superconducting platforms, no implementations exist for spin-based quantum processing units (QPU-SBs), despite their scalability potential via CMOS-compatible fabrication and recent demonstrations of multi-qubit processors. Here, we present a pulse-level, noise-aware DRU framework for spin-based QPUs, designed to bridge the gap between gate-level models and realistic spin-qubit execution. Our approach includes (i) compiling DRU circuits into hardware-proximate, time-domain controls derived from the Loss–DiVincenzo Hamiltonian, (ii) explicitly incorporating coherent and incoherent noise sources through pulse perturbations and Lindblad channels, (iii) enabling systematic noise-sensitivity studies across one-, two-, and four-spin configurations via continuous-time simulation, and (iv) developing a noise-aware training pipeline that benchmarks gate-level baselines against spin-level dynamics using information-theoretic loss functions. Numerical experiments show that our simulations reproduce gate-level dynamics with fidelities near unity while providing a richer error characterization under realistic noise. Moreover, divergence-based losses significantly enhance classification accuracy and robustness compared to fidelity-based metrics. Together, these results establish the proposed framework as a practical route for advancing DRU on spin-based platforms and motivate future work on error-attentive training and spin–quantum-dot noise modeling.

</details>
