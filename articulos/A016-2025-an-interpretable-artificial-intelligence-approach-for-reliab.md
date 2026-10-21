---
id: A016
titulo: "An Interpretable Artificial Intelligence Approach for Reliability and Regulation-Aware Decision Support in Power Systems"
tipo: articulo
temas: [T09, T07]
cluster: "C07 IA aplicada a salud, agro y territorio"
palabras_clave: [confiabilidad eléctrica, SAIFI, TabNet, cumplimiento regulatorio, IA explicable, redes de media tensión]
fuente_resumen: abstract
anio: 2025
revista: "Computation"
doi: 10.3390/computation14010002
citas_openalex: 3
fuentes: [0001330950]
---

# An Interpretable Artificial Intelligence Approach for Reliability and Regulation-Aware Decision Support in Power Systems

**Autores:** Diego Armando Pérez-Rosero, Santiago Pineda-Quintero, Juan Carlos Álvarez-Barreto, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computation (2025)  
**DOI:** https://doi.org/10.3390/computation14010002  
**Temas:** T09 Monitoreo industrial y sistemas de energía; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C07 IA aplicada a salud, agro y territorio

## Aplicación
Gestión de confiabilidad y cumplimiento regulatorio en redes de distribución de media tensión en Colombia.

## Problema de investigación
Los enfoques analíticos no entregan a la vez precisión predictiva, interpretabilidad y trazabilidad para índices como SAIFI (IEEE 1366) bajo regulación.

## Propuesta o novedad
CRITAIR combina un módulo predictivo basado en TabNet que estima SAIFI con datos de interrupciones, activos y meteorología, una etapa agéntica de recuperación y razonamiento que fundamenta recomendaciones en RETIE y NTC 2050, y grafos de razonamiento interpretables.

## Resultados
Con datos operativos reales, logra desempeño predictivo comparable a Random Forest y XGBoost, con transparencia por atención dispersa. El módulo regulatorio obtiene alta alineación semántica (BERTScore) e interpretabilidad calificada por expertos.

## Conclusiones principales
CRITAIR conecta la analítica predictiva con la gobernanza regulatoria con una solución auditable.

## Métodos
- TabNet
- razonamiento agéntico/RAG
- BERTScore
- grafos de razonamiento

## Idea para trabajo futuro
Validar CRITAIR con operadores de red de otras regiones y ante cambios normativos para medir su adaptabilidad.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Modern medium-voltage (MV) distribution networks face increasing reliability challenges driven by aging assets, climate variability, and evolving operational demands. In Colombia and across Latin America, reliability metrics, such as the System Average Interruption Frequency Index (SAIFI), standardized under IEEE 1366, serve as key indicators for regulatory compliance and service quality. However, existing analytical approaches struggle to jointly deliver predictive accuracy, interpretability, and traceability required for regulated environments. Here, we introduce CRITAIR (Criticality Analysis through Interpretable Artificial Intelligence-based Recommendations), an integrated framework that combines predictive modeling, explainable analytics, and regulation-aware reasoning to enhance reliability management in MV networks. CRITAIR unifies three components: (i) a TabNet-based predictive module that estimates SAIFI using outage, asset, and meteorological data while producing global and local attributions; (ii) an agentic retrieval-and-reasoning stage that grounds recommendations in regulatory evidence from RETIE and NTC 2050; and (iii) interpretable reasoning graphs that map decision pathways. Evaluations conducted on real operational data demonstrate that CRITAIR achieves competitive predictive performance—comparable to Random Forest and XGBoost—while maintaining transparency through sparse attention and sequential feature explainability. Also, our regulation-aware reasoning module exhibits coherent and verifiable recommendations, achieving high semantic alignment scores (BERTScore) and expert-rated interpretability. Overall, CRITAIR bridges the gap between predictive analytics and regulatory governance, offering a transparent, auditable, and deployment-ready solution for digital transformation in electric distribution systems.

</details>
