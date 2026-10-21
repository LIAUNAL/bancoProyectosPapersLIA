---
id: H69693
titulo: "Sistema de inteligencia artificial portable para la identificación de patrones de depresión asociados a estrés postraumático en estudiantes universitarios afectados por el sismo"
tipo: proyecto
temas: [T04, T11, T07]
cluster: "C04 EEG, TDAH y soporte diagnóstico"
palabras_clave: [depresión, estrés postraumático, habla, PHQ-8, aprendizaje múltiple-instancia, salud mental]
fuente_resumen: hermes
inicio: 2026
fin: 
codigo_hermes: 69693
quipu: 
estado_hermes: No_cumplio_requisitos
origen: Hermes
tipo_proyecto: Hermes
---

# Sistema de inteligencia artificial portable para la identificación de patrones de depresión asociados a estrés postraumático en estudiantes universitarios afectados por el sismo

**Periodo:** 2026–?  
**Código Hermes:** 69693  
**Convocatoria (Hermes):** INVITACIÓN NACIONAL FOCALIZADA - RESPUESTA A EMERGENCIAS Y DESASTRES: INVESTIGACIÓN PARA LA GESTIÓN DEL RIESGO, LA SALUD PÚBLICA, LA INFRAESTRUCTURA RESILIENTE Y LA RESPUESTA HUMANITARIA  
**Estado en Hermes:** No cumplió requisitos  
**Financiador:** Invitación Nacional Focalizada - Respuesta a Emergencias y Desastres (gestión del riesgo, salud pública, infraestructura resiliente y respuesta humanitaria)  
**Temas:** T04 Bioseñales y soporte al diagnóstico clínico; T11 Procesamiento de voz, audio y música; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C04 EEG, TDAH y soporte diagnóstico

## Aplicación
Tamizaje de depresión asociada a estrés postraumático en estudiantes universitarios afectados por el sismo del 10 de agosto de 2026.

## Problema de investigación
Los cuestionarios psicométricos aislados sobreestiman la severidad o dan falsos positivos y hay escasez de talento en salud mental, con bienestar universitario desbordado.

## Propuesta o novedad
Sistema de IA móvil con inferencia local que alinea segmentos del habla de entrevistas semiestructuradas con los ocho ítems del PHQ-8 mediante aprendizaje múltiple-instancia con supervisión débil.

## Resultados
Se espera validación cruzada por sujeto, contraste con DAIC-WOZ y E-DAIC, una cohorte local de 80 estudiantes y madurez de TRL 4 a TRL 6.

## Conclusiones principales
Se espera apoyar la alerta temprana sin reemplazar el juicio clínico, con operación sin conectividad.

## Productos tecnológicos principales
- Sistema de IA portable para dispositivos móviles
- Modelo de alineación semántica habla-PHQ-8

## Estrategia de apropiación social
No descrita en Hermes

## Aliados
- Universidad Tecnológica de Pereira (UTP)

## Idea para trabajo futuro
Extender la validación a otras poblaciones afectadas por desastres con apoyo de servicios de bienestar.

## Relacionados (similitud semántica)
- produjo: [[A004-2026-text-conditioned-semantic-aggregation-for-audio-based-multip]] — Text-Conditioned Semantic Aggregation for Audio-Based Multiple-Instance Learning in Depression Detection

<details><summary>Resumen original (CvLAC)</summary>

Los sismos de gran escala dejan una carga de morbilidad psicológica que persiste durante años cuando la respuesta institucional tarda. El sismo de magnitud 7,4 del 10 de agosto de 2026, con epicentro en San José del Palmar (Chocó), fue el más intenso del siglo XXI en Colombia y motivó la declaratoria de desastre nacional. En el Eje Cafetero, la suspensión de actividades y los daños materiales agudizaron el estrés postraumático y los cuadros depresivos de los estudiantes de la Universidad Nacional de Colombia Sede Manizales y de la Universidad Tecnológica de Pereira (UTP), y desbordaron a las dependencias de bienestar. Los cuestionarios psicométricos aislados sobreestiman la severidad clínica o arrojan falsos positivos, y la valoración especializada tropieza con la escasez de talento humano en salud mental. El proyecto busca un sistema de inteligencia artificial portable, desplegable en dispositivos móviles, que identifique patrones de depresión asociados a estrés postraumático a partir del habla en entrevistas semiestructuradas. El núcleo metodológico es una alineación semántica entre los segmentos temporales de la entrevista y cada uno de los ocho ítems sintomáticos del PHQ-8, mediante aprendizaje múltiple-instancia con supervisión débil: el estudiante representa la bolsa, las emisiones de habla son las instancias y los reactivos psicométricos guían la predicción. El diseño es cuantitativo, con validación cruzada por sujeto y contraste externo con los corpus DAIC-WOZ y E-DAIC. La evidencia de validez local se apoya en una cohorte propia de 80 estudiantes de la UNAL Sede Manizales y de la UTP vinculados por muestreo de conveniencia, y la inferencia local en el borde asegura el funcionamiento sin conectividad. Con las pruebas de campo en el entorno universitario real, la tecnología pasa de un TRL 4 a un TRL 6 al cierre. El alcance se limita a alertas tempranas de tamizaje y a la derivación hacia las rutas de bienestar institucional: la iniciativa no involucra personal de psiquiatría ni asume atención clínica directa. Tampoco evalúa ni descarta riesgo de conducta suicida; el corpus de entrevistas solo se comparte en formato derivado y desidentificado, sin divulgación del audio crudo. El desarrollo completo de este apartado consta en el documento técnico (ver AnexoDocumentoTecnico.pdf)* Objeto/Objetivo general (Máx. 4000 caracteres):Desarrollar un sistema de inteligencia artificial portable, desplegable sobre dispositivos móviles, que identifique patrones de depresión asociados a estrés postraumático en estudiantes universitarios de la Universidad Nacional de Colombia Sede Manizales y la Universidad Tecnológica de Pereira, afectados por el sismo, a partir del habla de entrevistas semiestructuradas.* OBJETIVOS ESPECÍFICOSObjetivo EspecíficoMedio de verificación1Desarrollar una estrategia de procesado multimodal mediante técnicas de inteligencia artificial que alinee y resalte instancias relevantes del habla con patrones de depresión a partir de entrevistas semiestructuradas.Desarrollar una estrategia de procesado multimodal mediante técnicas de inteligencia artificial que alinee y resalte instancias relevantes del habla con patrones de depresión a partir de entrevistas semiestructuradas.La calidad de la alineación se verifica contra los resultados del banco público de referencia, el corpus DAIC-WOZ y su extensión E-DAIC, y contra la valoración clínica por ítem del subconjunto anotado, mediante concordancia en el nivel de dominio sintomático. El contraste con la cohorte tamizada de la Sede, gestionado con la Dirección Académica y con el apoyo de la Universidad Tecnológica de Pereira, informa si la alineación se sostiene en un habla que el banco no contiene. La contribución de la supervisión por alineación se aísla en ablaciones que comparan la agregación condicionada por ítem con una agregación de atención sin correspondencia explícita, y el desempeño se reporta por sujeto y por subgrupo. El protocolo es común a las tres fases: validación por sujeto, sin hablante compartido entre ajuste y prueba, partición de retención sobre el banco público y ablaciones pieza por pieza. Las métricas se reportan con intervalos de confianza y si Desarrollar un sistema de inteligencia artificial portable, desplegable sobre dispositivos móviles, que identifique patrones de depresión asociados a estrés postraumático en estudiantes universitarios de la Universidad Nacional de Colombia Sede Manizales y la Universidad Tecnológica de Pereira, afectados por el sismo, a partir del habla de entrevistas semiestructuradas.

</details>
