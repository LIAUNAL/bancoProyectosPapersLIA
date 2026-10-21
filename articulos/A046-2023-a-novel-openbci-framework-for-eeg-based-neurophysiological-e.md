---
id: A046
titulo: "A novel OpenBCI framework for EEG-based neurophysiological experiments"
tipo: articulo
temas: [T01, T04]
cluster: "C04 EEG, TDAH y soporte diagnóstico"
palabras_clave: [OpenBCI, EEG, hardware abierto, BCI en tiempo real, controladores, cómputo distribuido]
fuente_resumen: abstract
anio: 2023
revista: "Sensors"
doi: 10.3390/s23073763
citas_openalex: 22
fuentes: [0000043222, 0001330950]
---

# A novel OpenBCI framework for EEG-based neurophysiological experiments

**Autores:** Yeison Nolberto Cardona-Álvarez, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, Germán Albeiro Castaño Duque, German Castellanos-Dominguez  
**Revista:** Sensors (2023)  
**DOI:** https://doi.org/10.3390/s23073763  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T04 Bioseñales y soporte al diagnóstico clínico  
**Clúster:** C04 EEG, TDAH y soporte diagnóstico

## Aplicación
Adquisición de EEG de bajo costo para experimentos neurofisiológicos con la placa Cyton de OpenBCI.

## Problema de investigación
OpenBCI tiene limitaciones de comunicación computador-periférico y poca flexibilidad para protocolos neurofisiológicos rápidos.

## Propuesta o novedad
Un marco OpenBCI flexible y escalable con controladores actualizados para la placa Cyton (ADS1299) que gestiona cómputo distribuido, varias tasas de muestreo y protocolos, ubicación libre de electrodos y sincronización por marcador único, con configuración automática y widgets de estímulos.

## Resultados
Una prueba de imaginación motora en lazo cerrado muestra transmisión en tiempo real dentro de rangos de latencia y jitter requeridos.

## Conclusiones principales
El marco es una solución prometedora para procesamiento neurofisiológico a medida.

## Métodos
- OpenBCI Cyton
- ADS1299
- sincronización de marcadores
- cómputo distribuido

## Idea para trabajo futuro
Validar el marco con protocolos clínicos de estimulación y medir su equivalencia con equipos de EEG comerciales.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

An Open Brain-Computer Interface (OpenBCI) provides unparalleled freedom and flexibility through open-source hardware and firmware at a low-cost implementation. It exploits robust hardware platforms and powerful software development kits to create customized drivers with advanced capabilities. Still, several restrictions may significantly reduce the performance of OpenBCI. These limitations include the need for more effective communication between computers and peripheral devices and more flexibility for fast settings under specific protocols for neurophysiological data. This paper describes a flexible and scalable OpenBCI framework for electroencephalographic (EEG) data experiments using the Cyton acquisition board with updated drivers to maximize the hardware benefits of ADS1299 platforms. The framework handles distributed computing tasks and supports multiple sampling rates, communication protocols, free electrode placement, and single marker synchronization. As a result, the OpenBCI system delivers real-time feedback and controlled execution of EEG-based clinical protocols for implementing the steps of neural recording, decoding, stimulation, and real-time analysis. In addition, the system incorporates automatic background configuration and user-friendly widgets for stimuli delivery. Motor imagery tests the closed-loop BCI designed to enable real-time streaming within the required latency and jitter ranges. Therefore, the presented framework offers a promising solution for tailored neurophysiological data processing.

</details>
