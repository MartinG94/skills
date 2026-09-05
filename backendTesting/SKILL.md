---
name: backend-testing
description: >-
  Diseña, implementa o audita pruebas automatizadas de backend a partir del
  comportamiento, los riesgos y el stack existentes. Selecciona el nivel de prueba y
  los dobles adecuados sin imponer porcentajes, frameworks ni arquitectura; escribe y
  ejecuta tests solo cuando el usuario pide cambios sobre un proyecto concreto.
---

# Estrategia y pruebas automatizadas de backend

## Responsabilidad y modos

Esta skill es downstream: consume requisitos, casos de uso, contratos y código ya
existentes. No crea comportamiento de negocio para poder probarlo ni rediseña la
arquitectura salvo que el usuario pida expresamente una refactorización.

Elegir un modo:

- **Estrategia**: proponer cobertura priorizada y criterios de aceptación técnica.
- **Implementación**: agregar o corregir pruebas en el stack existente.
- **Auditoría**: detectar cobertura engañosa, fragilidad, lentitud o aislamiento
  incorrecto sin modificar archivos.
- **Diagnóstico**: reproducir y explicar un test fallido o intermitente.

No iniciar una suite completa cuando el pedido solo requiere revisar un plan, ni
generar ejemplos en varios lenguajes. En implementación, usar exclusivamente el
lenguaje, framework y convenciones del repositorio.

## Entradas

Confirmar lo disponible de:

- comportamiento observable, invariantes y escenarios de error;
- código y límites de los componentes;
- contrato HTTP/eventos/esquema cuando corresponda;
- framework de pruebas, comandos y utilidades ya adoptados;
- dependencias externas y entorno de CI;
- riesgo, historial de fallos y restricciones de tiempo.

Si no hay código o stack, puede entregarse una estrategia neutral. No inventar firmas,
DTOs, entidades, repositorios, datos productivos ni dependencias para producir tests
aparentemente ejecutables.

## Selección del nivel de prueba

Elegir el nivel más bajo que observe el riesgo real sin replicar la implementación:

| Nivel | Valida principalmente | Dependencias reales habituales |
|---|---|---|
| unitaria | reglas puras, invariantes y decisiones locales | ninguna o dobles mínimos |
| componente/servicio | colaboración dentro de un límite desplegable | adaptadores controlados |
| integración | mapeos, consultas, serialización o integración con infraestructura | implementación representativa |
| contrato | compatibilidad entre productor y consumidor | contrato y ambas expectativas |
| end-to-end | pocos recorridos críticos del sistema completo | sistema integrado |

Las pruebas de contrato no son sinónimo de end-to-end. No imponer una pirámide con
porcentajes fijos: la distribución depende de riesgo, arquitectura, costo de ejecución
y confianza aportada. Evitar verificar el mismo detalle en todas las capas.

## Flujo de trabajo

### 1. Construir una matriz de riesgo y cobertura

| Comportamiento/riesgo | Evidencia de origen | Nivel elegido | Oráculo observable | Prioridad |
|---|---|---|---|---|

Derivar casos de reglas aprobadas, ejemplos, Gherkin, contratos o defectos reales.
Incluir caminos felices, límites y fallos que cambien el resultado; no crear una
combinatoria exhaustiva sin valor. Cuando un requisito sea ambiguo, marcar el test
como pendiente en vez de convertir una suposición en comportamiento esperado.

### 2. Definir el oráculo antes de implementar

Especificar qué salida, estado, evento o interacción externa demuestra el resultado.
Probar la API pública y efectos observables. Verificar una interacción interna solo
cuando ella sea el contrato relevante, por ejemplo publicar exactamente un evento.

Usar Arrange–Act–Assert o Given–When–Then si coincide con la convención del proyecto;
la separación conceptual importa más que comentarios o nombres obligatorios.

### 3. Elegir dependencias reales y dobles

- **Dummy**: completa un parámetro que no participa.
- **Stub**: suministra una respuesta controlada.
- **Spy**: registra llamadas o argumentos.
- **Mock**: expresa una expectativa de interacción.
- **Fake**: implementación ligera con comportamiento útil.

Preferir objetos reales para datos y reglas cuando sean baratos y deterministas.
Mockear una entidad o DTO no está universalmente prohibido, pero suele ocultar su
comportamiento; justificarlo si es el límite correcto. Evitar cadenas de mocks que
copian la estructura interna.

Abstraer reloj, azar, red u otros factores no deterministas cuando el escenario deba
controlarlos. No exigir inyección de cada detalle si la plataforma ya ofrece un
mecanismo estable y verificable.

### 4. Preparar el entorno proporcional

- Para lógica pura, evitar I/O.
- Para persistencia o comportamiento dependiente del motor, usar una base compatible
  y datos aislados. Testcontainers es una opción, no un requisito.
- Para clientes externos, elegir stub local, simulador, sandbox o prueba de contrato
  según el riesgo; no acceder a producción.
- Controlar puertos, zona horaria, locale, orden, concurrencia y limpieza solo cuando
  influyan en el caso.

No fijar presupuestos universales como “menos de 10 ms”. Registrar y actuar sobre la
duración cuando exista un objetivo de CI o una regresión medible.

### 5. Implementar en el stack existente

En modo Implementación:

1. localizar suites, fixtures, factories y comandos actuales;
2. agregar la mínima prueba que falle por la causa relevante;
3. mantener nombres y organización del proyecto;
4. evitar cambiar producción salvo que el usuario también haya pedido el fix;
5. ejecutar primero la prueba enfocada y luego la suite proporcional al cambio.

No añadir una librería de assertions, mocks o contenedores si las herramientas
presentes cubren el caso. Si una dependencia nueva aporta valor material, explicarla
antes de incorporarla.

### 6. Auditar calidad, no solo cobertura

Detectar especialmente:

- tests que pasan sin comprobar el resultado;
- aserciones acopladas a detalles internos;
- estado compartido u orden dependiente;
- esperas fijas, red, reloj o datos no controlados;
- fixtures enormes que ocultan la condición relevante;
- mocks que reimplementan el sistema;
- pruebas duplicadas que no agregan una clase de fallo;
- métricas de cobertura usadas como sustituto de comportamiento crítico.

Una cobertura alta no demuestra suficiencia. Priorizar fallos que la suite puede
detectar y la claridad del diagnóstico cuando falla.

## Verificación y finalización

Reportar el comando ejecutado y su resultado real. Si no fue posible ejecutar,
explicar la causa y no afirmar que la suite está en verde. Ante un test intermitente,
reproducir bajo condiciones controladas y aislar la fuente antes de ampliar reintentos
o timeouts.

Finalizar cuando:

- cada riesgo priorizado tiene una prueba, una justificación de exclusión o un
  pendiente explícito;
- las pruebas agregadas fallan por el defecto esperado y pasan con el comportamiento
  correcto cuando esa comprobación es posible;
- no se introdujeron comportamientos o dependencias no solicitados.

## Contrato de salida

Por defecto entregar:

1. contexto y modo aplicado;
2. matriz breve de riesgo/cobertura;
3. archivos modificados, solo en modo Implementación;
4. comandos y resultados de verificación;
5. riesgos no cubiertos y datos pendientes.

Incluir código completo solo cuando forma parte de la entrega solicitada.
