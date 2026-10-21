---
id: A033
titulo: "Optimization of Interconnected Natural Gas and Power Systems Using Mathematical Programs with Complementarity Constraints"
tipo: articulo
temas: [T09]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [gas natural, ecuación de Weymouth, restricciones de complementariedad, optimización no convexa, generación térmica, redes interconectadas]
fuente_resumen: abstract
anio: 2024
revista: "Mathematics"
doi: 10.3390/math12142224
citas_openalex: 1
fuentes: [0001330950]
---

# Optimization of Interconnected Natural Gas and Power Systems Using Mathematical Programs with Complementarity Constraints

**Autores:** Cristian Alejandro Blanco-Martínez, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez, David  Augusto Cardenas Peña, Alvaro Angel Orozco  
**Revista:** Mathematics (2024)  
**DOI:** https://doi.org/10.3390/math12142224  
**Temas:** T09 Monitoreo industrial y sistemas de energía  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Operación coordinada de redes interconectadas de gas natural y electricidad (sistemas colombianos incluidos).

## Problema de investigación
La ecuación de Weymouth no convexa que rige flujos y presiones en tuberías dificulta la programación óptima de la operación.

## Propuesta o novedad
Un enfoque MPCC (Mathematical Programming with Complementarity Constraints) que aproxima la ecuación de Weymouth reformulando la función signo discontinua que relaciona presiones y flujos. Evita programación entera mixta, mejorando aproximaciones lineales y cónicas de segundo orden.

## Resultados
Se probó en sistemas de 9 buses/8 nodos, 118 buses/48 nodos y 96 buses/63 nodos del sistema colombiano de transporte de gas. MPCC logró errores de aproximación de Weymouth menores o iguales a Taylor y relajaciones cónicas, con costos operativos algo mayores en los casos grandes.

## Conclusiones principales
MPCC equilibra fidelidad de aproximación, complejidad y optimalidad para redes gas-electricidad.

## Métodos
- MPCC
- aproximación de Weymouth
- optimización no convexa

## Idea para trabajo futuro
Incorporar incertidumbre en la demanda y generación renovable para el despacho conjunto gas-electricidad con MPCC.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P010-2021-desarrollo-de-una-herramienta-para-la-planeacion-a-largo-pla]] — Desarrollo de una herramienta para la planeación a largo plazo de la operación del sistema de transporte de gas natural de Colombia
- extiende: [[A055-2023-approximation-of-weymouth-equation-using-mathematical-progra]] — Approximation of Weymouth Equation Using Mathematical Programs with Complementarity Constraints for Natural Gas Transportation

<details><summary>Abstract</summary>

The demand for thermal power generation from natural gas has risen worldwide owing to its cleaner burning properties compared to other fossil fuels. Such an increasing demand requires an optimized management of gas transportation infrastructure. However, the operation scheduling for the interconnected power and gas networks faces several optimization challenges. One of the main challenges relies on the nonconvex Weymouth equation constraining gas flow and pressures in pipelines. This paper proposes a Mathematical Programming with Complementarity Constraints (MPCC) approach to approximate the Weymouth equation and ease the optimization. Specifically, the complementarity constraints reformulate the discontinuous sign function relating nodal pressures with pipeline flows to make continuous variables behave as binary. The MPCC-based approach avoids solving mixed-integer programming while improving conventional linear and second-order approximations. We tested the proposed Weymouth approximation on three interconnected systems: a 9-bus/8-node network, a 118-bus/48-node grid from previous works, and a 96-bus/63-node model from real Colombia's national gas transportation system. Results showed that the MPCC-based approach uniformly achieved lower or equal Weymouth approximation errors compared to prominent alternatives, including Taylor series and second-order cone relaxations. Despite slightly higher operational costs in the larger-scale cases, MPCC consistently delivered superior accuracy essential for reliable optimization. The proposed approach balances approximation fidelity, problem complexity, and solution optimality. Overall, exploiting complementarity constraints via MPCC provides an effective optimization platform for interconnected gas and electricity networks facing escalating demands and environmental pressures.

</details>
