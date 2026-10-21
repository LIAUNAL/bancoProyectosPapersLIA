---
id: A024
titulo: "Artificial Intelligence-Driven Mobile Platform for Thermographic Imaging to Support Maternal Health Care"
tipo: articulo
temas: [T03, T04, T07]
cluster: "C09 Termografía y analgesia obstétrica"
palabras_clave: [termografía infrarroja, analgesia epidural, segmentación semántica, U-Net, MobileNetV3, despliegue móvil]
fuente_resumen: abstract
anio: 2025
revista: "Computers"
doi: 10.3390/computers14110466
citas_openalex: 1
fuentes: [0001330950]
---

# Artificial Intelligence-Driven Mobile Platform for Thermographic Imaging to Support Maternal Health Care

**Autores:** Lucas Miguel Iturriago-Salas, Jeison Andres Mesa-Sarmiento, Paola Alexandra Castro-Cabrera, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computers (2025)  
**DOI:** https://doi.org/10.3390/computers14110466  
**Temas:** T03 Imagen médica y neuroimagen; T04 Bioseñales y soporte al diagnóstico clínico; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C09 Termografía y analgesia obstétrica

## Aplicación
Monitoreo de analgesia epidural en trabajo de parto mediante termografía infrarroja en teléfono inteligente.

## Problema de investigación
El monitoreo convencional de la analgesia epidural es subjetivo, indirecto y dependiente del operador, y la termografía enfrenta limitaciones clínicas y de hardware.

## Propuesta o novedad
Una plataforma móvil con IA que integra segmentación semántica ligera (U-Net con backbone MobileNetV3), registro no rígido de dermatomas con deformación de forma libre (FFD) basada en B-splines e inferencia en el dispositivo con TensorFlow Lite.

## Resultados
U-Net con MobileNetV3 fue la arquitectura óptima, con Dice de 0.97, 4.5% de ganancia en IoU frente a backbones más pesados y 73% más eficiencia en parámetros. La inferencia en el teléfono toma unos dos segundos por imagen.

## Conclusiones principales
El sistema ofrece una herramienta cuantitativa y automatizada para reemplazar o complementar valoraciones clínicas subjetivas en anestesia obstétrica.

## Métodos
- U-Net
- MobileNetV3
- FFD B-spline
- TensorFlow Lite

## Idea para trabajo futuro
Realizar un estudio clínico prospectivo que relacione la evolución del mapa térmico con la calidad del bloqueo y el dolor reportado.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P001-2023-sistema-de-vision-artificial-para-el-monitoreo-y-seguimiento]] — Sistema de visión artificial para el monitoreo y seguimiento de efectos analgésicos y anestésicos administrados vía neuroaxial epidural en población obstétrica durante labores de parto para el fortalecimiento de servicios de salud materna del Hospital Uni

<details><summary>Abstract</summary>

Maternal health care during labor requires the continuous and reliable monitoring of analgesic procedures, yet conventional systems are often subjective, indirect, and operator-dependent. Infrared thermography (IRT) offers a promising non-invasive approach for labor epidural analgesia (LEA) monitoring, but its practical implementation is hindered by clinical and hardware limitations. This work presents a novel artificial intelligence-driven mobile platform to overcome these hurdles. The proposed solution integrates a lightweight deep learning model for semantic segmentation, a B-spline-based free-form deformation (FFD) approach for non-rigid dermatome registration, and efficient on-device inference. Our analysis identified a U-Net with a MobileNetV3 backbone as the optimal architecture, achieving a high Dice score of 0.97 and a 4.5% intersection over union (IoU) gain over heavier backbones while being 73% more parameter-efficient. The entire AI pipeline is deployed on a commercial smartphone via TensorFlow Lite, achieving an on-device inference time of approximately two seconds per image. Deployed within a user-friendly interface, our approach provides straightforward feedback to support decision making in labor management. By integrating thermal imaging with deep learning and mobile deployment, the proposed system provides a practical solution to enhance maternal care. By offering a quantitative, automated tool, this work demonstrates a viable pathway to augment or replace subjective clinical assessments with objective, data-driven monitoring, bridging the gap between advanced AI research and point-of-care practice in obstetric anesthesia.

</details>
