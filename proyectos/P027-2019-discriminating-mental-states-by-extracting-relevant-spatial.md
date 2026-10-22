---
id: P027
titulo: "DISCRIMINATING MENTAL STATES BY EXTRACTING RELEVANT SPATIAL PATTERNS UNDER NON-STATIONARY AND SUBJECT-INDEPENDENT CONSTRAINTS"
tipo: proyecto
temas: [T01, T05]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [interfaces cerebro-computador, imaginación motora, EEG, no estacionariedad, patrones espaciales, independencia del sujeto]
fuente_resumen: resumen
inicio: 2019
fin: 2021
codigo_hermes: 41918
quipu: 201010014169
estado_hermes: 
origen: CvLAC
tipo_proyecto: Investigación y desarrollo
---

# DISCRIMINATING MENTAL STATES BY EXTRACTING RELEVANT SPATIAL PATTERNS UNDER NON-STATIONARY AND SUBJECT-INDEPENDENT CONSTRAINTS

**Periodo:** 2019–2021  
**Código Hermes:** 41918 · QUIPU 201010014169  
**Convocatoria (Hermes):** CONVOCATORIA 727 DE COLCIENCIAS PARA DOCTORADOS NACIONALES 2015  
**Financiador:** No reportado en CvLAC  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Interfaces cerebro-computador por EEG basadas en imaginación motora, para discapacidad motora y otras aplicaciones.

## Problema de investigación
Las señales EEG son no estacionarias por artefactos, fatiga o atención, lo que rompe los supuestos de las técnicas convencionales y genera sobreajuste.

## Propuesta o novedad
Desarrollar una metodología de caracterización de cambios de actividad cerebral que discrimine estados mentales de imaginación motora aprovechando la no estacionariedad y restricciones independientes del sujeto.

## Resultados
El resumen plantea la pregunta de investigación y no reporta resultados cuantitativos.

## Conclusiones principales
La propuesta se centra en las etapas de adquisición y discriminación de una ICC.

## Productos tecnológicos principales
- Metodología de extracción de patrones espaciales para BCI

## Estrategia de apropiación social
No reportada en CvLAC

## Aliados
- No reportados en CvLAC (verificar en Hermes)

## Idea para trabajo futuro
Evaluar el enfoque en una ICC en línea con usuarios nuevos sin calibración previa.

## Relacionados (similitud semántica)
- produjo: [[A105-2019-relevance-of-common-spatial-patterns-ranked-by-kernel-pca-in]] — Relevance of common spatial patterns ranked by kernel PCA in motor imagery classification
- produjo: [[A110-2019-subject-oriented-dynamic-characterization-of-motor-imagery-t]] — Subject-Oriented Dynamic Characterization of Motor Imagery Tasks Using Complexity Analysis
- produjo: [[A081-2020-entropy-based-estimation-of-event-related-de-synchronization]] — Entropy-based Estimation of Event-Related De/Synchronization in Motor Imagery Using Vector-Quantized Patterns
- produjo: [[A075-2020-cnn-based-framework-using-spatial-dropping-for-enhanced-inte]] — CNN-based framework using spatial dropping for enhanced interpretation of neural activity in motor imagery classification

<details><summary>Resumen original (CvLAC)</summary>

Las interfaces cerebro-computadora (ICC) son sistemas que utilizan las medidas de funciones cerebrales para proporcionar un nuevo canal de comunicación no muscular que envíe mensajes y comandos a dispositivos externos. Las ICC, tradicionalmente han centrado sus esfuerzos en mejorar la vida de las personas con discapacidad motora, ya sea generada por problemas físicos o por neuropatologías degenerativas como la 
Esclerosis Lateral Amiotrófica y la Distrofia Muscular. Recientemente, han ganado atención en nuevas aplicaciones como educación, marketing, 
asistencia y seguridad, así como juegos y entretenimiento, impulsados por los sistemas de adquisición portátiles modernos. En general, una ICC está compuesta por tres etapas: i) Adquisición de la actividad cerebral, ii) Discriminación de la actividad cerebral y iii) Traducción de esta información en un comando a la salida del dispositivo. Dado el enfoque investigativo de la presente propuesta, sólo serán consideradas las etapasuno y dos. 
Con respecto a la primera etapa, la información cerebral que proporcionan las señales de electroencefalografía (EEG) ha sido ampliamente utilizada para estudiar la dinámica cerebral en diversas aplicaciones debida a su alta resolución temporal, bajo costo, mínimo riesgo y alta portabilidad de los sistemas de adquisición. Una aplicación de las ICC a partir de EEG se basa en el paradigma de neurociencia cognitiva 
denominado imaginación motora (IM), que corresponde a los patrones de actividad cerebral de la imaginación de una acción motora sin involucrar actividades musculares. Este tipo de ICC emplea las señales cerebrales, bajo la suposición que la imaginación de la ejecución del movimiento atenúa los ritmos sensorio motores del cerebro. Puesto que una tarea en particular produce sus propios patrones y exige sus propios métodos de procesamiento, el desarrollo de ICC debe considerar los protocolos experimentales de adquisición de registros de EEG. Por ejemplo, en el análisis 
de potenciales evocados P300 no pueden usarse los mismos algoritmos que en IM, ya que el primero evoca una forma de onda detectable y el segundo no siempre la presenta. Por lo tanto, el protocolo de adquisición de los registros de EEG debe considerar el patrón actividad cerebral a analizar dentro del paradigma de IM. 
En la segunda etapa, la decodificación de la información cerebral relacionada a estados mentales requiere un análisis de datos apropiado para 
alcanzar el rendimiento requerido para las aplicaciones del mundo real. Desde el punto de vista del reconocimiento de patrones, el desarrollo de ICC también incluye metodologías de representación o extracción de características que tengan en cuenta las características de la señal de EEG. Por ejemplo, las señales de EEG son conocidas por su naturaleza no estacionaria asociada a variaciones en las propiedades de la señal a lo largo del tiempo y a la mezcla de múltiples fuentes con diferentes escalas de tiempo. Estos fenómenos pueden estar relacionados con artefactos como electrodos sueltos, movimientos musculares, parpadeo, movimiento de los dientes, cambios repentinos de atención, efectos del cansancio, o los efectos de aprendizaje. Las anteriores condiciones rompen las suposiciones iniciales de las técnicas de caracterización convencionales aumentando su variabilidad y generando soluciones sobre-entrenadas. Dado que la naturaleza de la señal no se puede cambiar, surge la pregunta de 
investigación: ¿Cómo desarrollar una metodología de caracterización de los cambios en la actividad cerebral que permita la discriminación de estados mentales de imaginación motora explotando la estructura de no estacionalidad inherente de las señales cerebrales?

</details>
