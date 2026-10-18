# Guía de Referencia Operativa: Flujos de Trabajo Agénticos, TDD y Debugging Sistemático

Este documento detalla las directivas metodológicas, listas de verificación y plantillas formales de la skill `superpowers`, inspirada en los estándares de desarrollo disciplinado para agentes de software de alta autonomía.

---

## 1. El Ciclo Riguroso de TDD (Test-Driven Development)

El principio rector del desarrollo guiado por pruebas en entornos agénticos es: **"Ninguna línea de código de producción debe existir sin un test automatizado previo que haya fallado legítimamente y demostrado su necesidad"**.

### 1.1. Las Tres Fases Inmutables

```
   ┌─────────────────────────────────────────────────────────────┐
   │                                                             │
   ▼                                                             │
┌──────────────┐       ┌────────────────┐       ┌────────────┐   │
│   1. RED     │ ────> │   2. GREEN     │ ────> │ 3. REFACTOR│ ──┘
│ (Fallo Real) │       │ (Paso Mínimo)  │       │ (Limpieza) │
└──────────────┘       └────────────────┘       └────────────┘
```

1. **Fase RED (Rojo Observable):**
   - Escribir una prueba unitaria o de integración puntual que describa un comportamiento o invariante esperado.
   - Ejecutar la prueba inmediatamente mediante la herramienta de ejecución de tests del proyecto con el proxy `rtk` (ej. `rtk test <cmd>`, `rtk pytest`, `rtk cargo test`, `rtk vitest`).
   - **Verificación obligatoria del oráculo:** Constatar que la prueba efectivamente falle. Si la prueba pasa antes de escribir el código de producción, el test es redundante, inválido o tautológico (prueba obviedades o mocks desconectados).
   - Constatar que falle por la razón exacta prevista (ej. `MethodNotFound`, `AssertionError: expected X but received Y`), y no por un error de sintaxis del propio archivo de prueba.

2. **Fase GREEN (Verde Quirúrgico):**
   - Escribir únicamente el código mínimo y necesario para que el test pase.
   - Prohibido en esta fase anticipar requerimientos futuros, crear interfaces genéricas o implementar ramas no cubiertas por el test actual.
   - Ejecutar el test con `rtk` y confirmar que se ponga en verde.

3. **Fase REFACTOR (Refactorización Segura):**
   - Examinar el código recién escrito para eliminar duplicación, mejorar la legibilidad de variables y funciones, optimizar complejidad algorítmica y cumplir principios de arquitectura limpia.
   - Ejecutar nuevamente la suite completa de pruebas para garantizar que no existan regresiones.

### 1.2. Patrones de Diseño de Tests

- **Estructura Arrange-Act-Assert (AAA):**
  - *Arrange:* Configurar el estado inicial y los datos de prueba indispensables.
  - *Act:* Ejecutar la acción o invocar el método bajo prueba exactamente una vez.
  - *Assert:* Verificar el resultado observable, estado o mutación. Un concepto o invariante por test.
- **Uso Controlado de Dobles de Prueba:**
  - Preferir *Fakes* en memoria (ej. repositorio SQLite en memoria) sobre *Mocks* frágiles acoplados a detalles de implementación.
  - Nunca mockear lo que no te pertenece (librerías de terceros complejas); encapsularlas primero tras un adaptador delgado de dominio y probar dicho adaptador.
- **Detección de Anti-patrones de Testing:**
  - *Test Tautológico:* Verifica la configuración del mock en lugar del comportamiento (`verify(service.doSomething())` cuando el método bajo prueba solo llama a `doSomething()`).
  - *Test Frágil:* Falla por cambios cosméticos o de formato interno no funcionales.
  - *Sleep/Delays arbitrarios:* Usar mecanismos reactivos o `await`-polling con timeouts en lugar de `sleep(2000)`.

---

## 2. Protocolo de Debugging Sistemático de 4 Pasos

Cuando se detecta un fallo, un test roto o un comportamiento errático en producción, queda terminantemente prohibido formular conjeturas al azar, modificar código a ciegas o introducir soluciones parche ("workarounds"). Se debe aplicar el siguiente protocolo de 4 pasos:

### 2.1. Las 4 Fases de Depuración

| Fase | Nombre | Objetivo Clave | Prohibiciones Estrictas |
|---|---|---|---|
| **Fase 1** | **Reproducción Determinista** | Lograr reproducir el error bajo demanda de forma 100% predecible en un script o test mínimo. | No modificar código de la aplicación. No adivinar la causa antes de ver el error reproducido. |
| **Fase 2** | **Aislamiento de Causa Raíz** | Formular hipótesis científicas, inspeccionar stack traces, trazar flujo de datos e identificar la línea/invariante rota. | No aceptar correlación temporal como causalidad. No cambiar múltiples variables a la vez. |
| **Fase 3** | **Corrección Quirúrgica** | Solucionar la causa fundamental del problema en el origen, no en los síntomas. | Prohibido silenciar errores con `try/catch` vacíos, `any`, `ignore-lint` o conversiones forzadas. |
| **Fase 4** | **Test de Regresión** | Agregar un test automatizado que falle con el bug original y pase con el fix, garantizando permanencia. | No dar por cerrado el bug sin un test de regresión automatizado integrado en la suite. |

### 2.2. Checklist Operativo de Diagnóstico

- [ ] **Lectura Completa del Error:** Leer detenidamente el mensaje de error completo, tipo de excepción y traza de pila (stack trace) de abajo hacia arriba.
- [ ] **Aislar la Entrada Mínima:** Identificar el caso de entrada más pequeño posible que dispara el defecto (fuzzing inverso o bisección de datos).
- [ ] **Comprobación de Supuestos:** Verificar tipos reales de variables en tiempo de ejecución, valores `null`/`undefined`, encodings UTF-8, variables de entorno y zonas horarias.
- [ ] **Trazabilidad de Estado:** Confirmar si el error proviene de una mutación inesperada de estado compartido o concurrencia.
- [ ] **Validación de la Corrección:** Re-ejecutar el test de reproducción para confirmar estado verde, seguido de la suite completa.

---

## 3. Planificación de Tareas Atómicas (Bite-sized Plan)

Toda tarea técnica que requiera más de 5 minutos de ejecución o afecte múltiples archivos debe descomponerse en un plan estructurado de pasos atómicos.

### 3.1. Requisitos de una Tarea Atómica (2 a 5 Minutos)

1. **Rutas Exactas:** Debe especificar los archivos objetivos con sus rutas absolutas o relativas canónicas.
2. **Acción Concreta:** Verbos operativos unívocos (`Crear`, `Modificar`, `Eliminar`, `Verificar`).
3. **Comando de Verificación Determinista:** Comando que cualquier agente puede ejecutar inmediatamente para certificar si la tarea fue exitosa (ej. `$env:PYTHONUTF8 = '1'; rtk pytest tests/test_auth.py::test_jwt_validation`).
4. **Independencia o Dependencia Explícita:** Debe indicar claramente si bloquea a otras tareas o si puede ejecutarse de forma aislada.

### 3.2. Formato Canónico de Plan de Tarea

```markdown
### Tarea [ID]: [Nombre Conciso del Paso]
- **Archivo Objetivo:** `src/services/payment_gateway.py`
- **Líneas/Componente:** Clase `PaymentGateway`, método `process_refund`
- **Acción:** Implementar validación de idempotencia de reembolsos contra el repositorio local.
- **Comando de Verificación:** `rtk test pytest tests/unit/test_payment_gateway.py -k "test_process_refund_idempotent"`
- **Criterio de Éxito:** Salida en código de salida 0 con aserción de excepción `DuplicateRefundError`.
- **Dependencias:** Requiere Tarea 02 (Migración de esquema de reembolsos).
```

---

## 4. Orquestación y Despacho de Subagentes

Para maximizar la precisión, evitar la contaminación de contexto y proteger ventanas de cuota de modelos de razonamiento profundo, `superpowers` define las siguientes directivas de delegación:

### 4.1. Patrones de Especialización de Subagentes

1. **Exploración Rápida (`explorer-low`):**
   - Tareas: `grep`, búsqueda de archivos, inspección de dependencias, filtrado de logs pesados.
   - Modelo: `flash_lite` o `flash`.
   - Directiva: Nunca invocar razonamiento complejo para búsquedas mecánicas. Devolver rutas exactas y líneas de interés.
2. **Implementación Precisa (`code-executor`):**
   - Tareas: Aplicar cambios de código atómicos siguiendo un plan previamente validado, ejecutar tests y compilar reportes de verificación.
   - Modelo: `flash`.
   - Directiva: Apego estricto al plan. No inventar arquitectura.
3. **Revisión de Código Pre-merge (`code-reviewer` / Auditor):**
   - Tareas: Auditar diffs contra la especificación original, evaluar seguridad (OWASP Top 10), performance, complejidad ciclomática y ausencia de sobreingeniería.

### 4.2. Compuerta de Revisión Pre-Merge (Review Gate)

Antes de fusionar código o marcar una sesión como finalizada:
- [ ] ¿El código implementado cumple exactamente con el contrato funcional acordado en la Fase 1?
- [ ] ¿Todos los tests nuevos y preexistentes corren en verde (`rtk test <cmd>`)?
- [ ] ¿Se añadieron tests de regresión para cualquier bug corregido?
- [ ] ¿Hay advertencias de linter, tipos estáticos rotos o código muerto introducido?
- [ ] ¿Se introdujeron dependencias externas innecesarias que violan el principio de simplicidad?
