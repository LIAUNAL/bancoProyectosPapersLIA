---
id: P034
titulo: "Desarrollo de un sistema de monitoreo de condición y diagnóstico de fallas en línea de sistemas de generación de energía hidroeléctrica empleando una red de sensores inalámbricos de datos de alta resolución"
tipo: proyecto
temas: [T09]
cluster: "C06 Diagnóstico de fallas y sistemas de energía"
palabras_clave: [generación hidroeléctrica, sensores inalámbricos, mantenimiento predictivo, diagnóstico de fallas, vibración, monitoreo de condición]
fuente_resumen: resumen
inicio: 2016
fin: 2018
codigo_hermes: 31681
quipu: No
estado_hermes: 
origen: CvLAC
tipo_proyecto: Investigación y desarrollo
---

# Desarrollo de un sistema de monitoreo de condición y diagnóstico de fallas en línea de sistemas de generación de energía hidroeléctrica empleando una red de sensores inalámbricos de datos de alta resolución

**Periodo:** 2016–2018  
**Código Hermes:** 31681 · QUIPU No  
**Convocatoria (Hermes):** Convocatoria externa  
**Financiador:** No reportado en CvLAC  
**Temas:** T09 Monitoreo industrial y sistemas de energía  
**Clúster:** C06 Diagnóstico de fallas y sistemas de energía

## Aplicación
Monitoreo de condición y diagnóstico de fallas en sistemas hidroeléctricos para mantenimiento predictivo.

## Problema de investigación
Las paradas inesperadas generan altos costos en la industria energética colombiana y el sector requiere sistemas que fortalezcan el mantenimiento predictivo.

## Propuesta o novedad
Desarrollar en tres fases un prototipo de monitoreo con nodos inalámbricos (caudal, temperatura, velocidad y vibración), un sistema de información para visualización y algoritmos de caracterización de señales para detectar fallas tempranas.

## Resultados
Se describen nodos de medición, por ejemplo de caudal por tiempo de vuelo y temperatura con termocupla tipo J; no se reportan resultados cuantitativos.

## Conclusiones principales
El diseño busca responder a los requerimientos del sector y a la detección de fallas en estado temprano.

## Productos tecnológicos principales
- Red de sensores inalámbricos de alta resolución
- Nodos de medición de caudal, temperatura, velocidad y vibración
- Sistema de información de visualización para mantenimiento

## Estrategia de apropiación social
No reportada en CvLAC

## Aliados
- No reportados en CvLAC (verificar en Hermes)

## Idea para trabajo futuro
Desplegar la red de sensores en una central en operación continua y evaluar el desempeño de los algoritmos de alerta temprana.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Resumen original (CvLAC)</summary>

Un sistema de monitoreo y diagnóstico de fallas en sistemas de generación hidroeléctrica es de gran importancia para el sector energía, ya que este permite reducir paradas inesperadas que conllevan altos costos para la industria colombiana, y además, resulta de gran interés para las empresas del sector contar con sistema que fortalezca las estrategias de mantenimiento predictivo. En tal sentido, el proyecto que se encuentra en desarrollo se fundamenta en el diseño e implementación de un sistema que cumpla con los requerimientos y necesidades que tiene el sector, con lo cual el sistema a desarrollar se comprende de tres fases indispensables: diseño e implementación de un prototipo de monitoreo, diseño de un sistema de información que incluya manejo de datos y visualización de resultados que sean fáciles de interpretar por el personal de mantenimiento, y diseño e implementación de algoritmos robustos que permitan la caracterización de diferentes señales para el diagnóstico del estado del sistema de generación hidroeléctrica e identificación fallas en estado temprano que permita a los usuarios tomar decisiones pertinentes y en un tiempo prudente. A continuación se realiza una breve reseña de los desarrollos realizados en cada etapa: Diseño de sistema prototipo de monitoreo del par turbina-generador empleando redes de sensores y transmisión de señales de alta resolución: El sistema se compone de 5 nodos distribuidos en: 1 nodo tipo A que se ubica en la tubería de entrada del sistema y 4 nodos tipo B que se ubican en los rodamientos de apoyo del sistema, dando cobertura completa al sistema de generación hidroeléctrica. 1. Nodo tipo A (Monitoreo de caudal y presión): El modulo cuenta con un sensor de presión donde su acondicionamiento consiste en un convertidor de corriente de entrada a tensión. La señal de entrada de 4 mA a 20 mA se convierte en una tensión por una resistencia de 120Ω y una corriente de entrada de 4 mA a 20 mA, la tensión de entrada al circuito de desplazamiento de nivel es de 0,48 V a 2,4 V. El circuito cuenta con un diodo de protección contra una conexión inversa accidental de la fuente de corriente de entrada. El voltaje a través de la resistencia de 120Ω es nivelado y atenuado por el amplificador operacional. La salida del amplificador operacional es de 0,1 V a 2,4 V. El voltaje acondicionado va a una entrada análoga del microcontrolador con resolución de 10 bits y frecuencia de muestreo programada y temporizada de 1 muestra por segundo. El otro modulo integrado es el de caudal que usa transductores ultrasónico con frecuencia de 1MHz para tubería de 10cm a 6m estos van conectados a un AFE (Analog Front End) que cuenta con dos canales de transmisión y de recepción cada sensor va conectado a cada canal, cuando se le da un pulso de arranque, el AFE le envía al primer sensor una señal cuadrada, el tiempo que tarda el segundo sensor en recibir la señal se llama tiempo de vuelo y al obtener este se repite el proceso pero empezando desde el segundo sensor y primer sensor lo recibe, con los dos tiempos de vuelo (DOWN & UP) se calcula el delta de tiempo y remplazando en las formulas se obtiene el caudal que pasa por la tubería, los tiempos se miden con un conversor digital de tiempo. 2. Nodo tipo B (Monitoreo de temperatura, velocidad y vibración): El módulo de temperatura se conecta una termocupla tipo J para realizar mediciones en rangos de 0°C hasta 120°C en chumaceras y monitorear el estado de los rodamientos, este módulo cuenta con un circuito integrado que tiene internamente una unión de temperatura de unión en frio como referencia además de acondicionar y muestrear la señal, los datos los entrega en formato digital.

</details>
