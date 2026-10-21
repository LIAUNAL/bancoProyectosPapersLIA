---
id: A001
titulo: "Detecting the unseen poor in multidimensional poverty assessment using Bayesian approaches"
tipo: articulo
temas: [T06, T14]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [pobreza multidimensional, método Alkire-Foster, error de clasificación, modelo jerárquico bayesiano, vulnerabilidad, política social]
fuente_resumen: abstract
anio: 2026
revista: "Quality & Quantity"
doi: 10.1007/s11135-026-02776-0
citas_openalex: 0
fuentes: [0001330950]
---

# Detecting the unseen poor in multidimensional poverty assessment using Bayesian approaches

**Autores:** Carlos Andrés Pérez-Aguirre, Guberney Muñetón-Santa, Andrés Marino Álvarez-Meza  
**Revista:** Quality & Quantity (2026)  
**DOI:** https://doi.org/10.1007/s11135-026-02776-0  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T14 Educación, sociedad y analítica de datos  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Medición de pobreza multidimensional y vulnerabilidad con datos de hogares de Medellín, Colombia.

## Problema de investigación
Los métodos deterministas como Alkire-Foster asumen cero errores de clasificación, lo que distorsiona sistemáticamente las estimaciones de pobreza y vulnerabilidad. Se requiere un enfoque que incorpore la incertidumbre de medición.

## Propuesta o novedad
Un marco jerárquico bayesiano que integra tasas de falsos positivos y falsos negativos en el proceso de medición de pobreza multidimensional. Replantea la pobreza como un proceso inherentemente probabilístico y no determinista.

## Resultados
Al aplicarlo a datos de hogares de Medellín, ignorar la incertidumbre de clasificación subestima la privación social. Errores de apenas 1-2% pueden inflar la prevalencia real de pobreza en cerca de 16%, y la vulnerabilidad futura puede subestimarse hasta en 290%.

## Conclusiones principales
El modelo ofrece a los formuladores de política estimaciones más robustas para asignar recursos e identificar hogares estadísticamente invisibles.

## Métodos
- modelo jerárquico bayesiano
- Alkire-Foster
- tasas de falsos positivos/negativos

## Idea para trabajo futuro
Extender el modelo a tasas de error dependientes de covariables de hogar y validarlo con otras encuestas nacionales.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Abstract This study introduces a hierarchical Bayesian framework designed to enhance multidimensional poverty measurement by explicitly accounting for classification errors often ignored in conventional methodologies. Traditional deterministic approaches, such as the Alkire-Foster method, assume zero measurement errors (i.e., data collection and, more importantly, unfulfiled assumptions), leading to systematic distortions in poverty estimates and vulnerability assessments.To address this methodological limitation, we develop a probabilistic model that integrates false positive and false negative rates into the measurement process. Applying this framework to household data from Medellín, Colombia, we demonstrate that ignoring classification uncertainty results in substantial underestimation of social deprivation. Our findings indicate that even modest error rates (1–2%) can inflate true poverty prevalence by approximately 16%, while vulnerability assessments are even more sensitive, potentially underestimating future risk by up to 290%. By reconceptualizing poverty measurement as an inherently probabilistic process, this paper offers a rigorous statistical tool for correcting these biases. The proposed model provides policymakers with more robust estimates for resource allocation, ensuring that statistically “invisible” households are accurately identified. This contribution aligns with the need for methodological precision in social indicators, offering a flexible solution to improve the quality of data used for equitable social policy design.

</details>
