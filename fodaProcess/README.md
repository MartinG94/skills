# fodaProcess (Matriz FODA del Proceso Operativo — GMP Etapa 2)

Skill atómica especializada para la estructuración, balance y validación de la **Matriz FODA (SWOT)** a nivel de proceso operativo de negocio, en el marco de la **Etapa 2 de Gestión y Mejora de Procesos (GMP / Ciclo PDCA)** de la Universidad Tecnológica Nacional (UTN FRC).

---

## 1. Propósito General

`fodaProcess` formaliza el diagnóstico situacional de un proceso de negocio AS-IS asegurando los principios metodológicos canónicos de cátedra:

1. **Delimitación Estricta de Frontera Interna vs. Externa (Principio de Controlabilidad):**
   - **Factores Internos (Fortalezas y Debilidades):** Atributos o condiciones propias de la organización sobre las cuales los responsables del proceso poseen autoridad directa de gobierno o rediseño (procesos, sistemas internos, personal, procedimientos, infraestructura física propia).
   - **Factores Externos (Oportunidades y Amenazas):** Fuerzas del macroentorno (político, legal, económico, social, tecnológico) o del microentorno (competidores, clientes, proveedores, mercado) ajenas al control directo del proceso, ante las cuales este debe capitalizar ventajas o blindarse frente a riesgos.

2. **Articulación bajo los Tres Ejes de Análisis de Cátedra (`PlanillaMATRICES-TPI 2026` Matriz 3):**
   - **Eje 1: Propósito, Visión y Estrategia:** Cómo contribuye o desvía el factor respecto a la misión, visión y metas institucionales.
   - **Eje 2: Grupos de Interés (Stakeholders):** Quiénes se benefician o son perjudicados (trazable a [`stakeholderMatrix`](file:///c:/Users/Diego/.gemini/config/skills/stakeholderMatrix/SKILL.md)).
   - **Eje 3: Resultados Actuales y Evidencia Forense:** Evidencia cuantitativa o cualitativa de desempeño AS-IS o hallazgo probatorio de auditoría (`processAuditor`).

3. **Trazabilidad Forense Obligatoria de Debilidades:**
   Toda debilidad incorporada a la matriz debe estar fundamentada en evidencias concretas derivadas de la auditoría forense ([`processAuditor`](file:///c:/Users/Diego/.gemini/config/skills/processAuditor/SKILL.md)), matrices de riesgo (RCM), segregación de funciones (SoD), análisis de ruta documental/papel, silos TI o citas trazables de entrevistas de relevamiento (`SRC-...`). Queda prohibida la inclusión de debilidades conjeturales o abstractas.

4. **Cardinalidad Canónica de Cátedra (Regla 4-6):**
   Garantiza un análisis equilibrado forzando entre 4 y 6 factores por cuadrante ($4 \le N \le 6$), evitando tanto la dispersión como el análisis superficial (`SLI_U3_C03_Analisis_FODA.pdf`, diapositiva 6).

---

## 2. Arquitectura Interna del Componente

```
fodaProcess/
├── SKILL.md                          # Contrato operacional consumido por el LLM (instrucciones y límites)
├── README.md                         # Documentación técnica, estándares de gobernanza y guía humana
├── references/                       # Referencias metodológicas y casos oficiales de cátedra
│   └── foda_methodology_guide.md     # Guía detallada con casos oficiales (Municipalidad y Universidad)
├── scripts/                          # Herramientas de automatización y validación algorítmica
│   ├── validate_foda.py              # Validador determinista de cuadrantes, cardinalidad y frontera
│   └── test_validate_foda.py         # Suite completa de pruebas unitarias (unittest)
└── templates/                        # Plantillas institucionales de cátedra
    └── foda_process_template.md      # Plantilla canónica de salida en Markdown ('foda.md')
```

---

## 3. Prerequisitos de Entorno

- **Python:** Python 3.8 o superior (para ejecutar el validador `scripts/validate_foda.py`).
- **Dependencias:** Utiliza exclusivamente la biblioteca estándar de Python (`re`, `sys`, `pathlib`, `argparse`, `unittest`). No requiere instalación de paquetes de terceros vía `pip`.

---

## 4. Ejemplos de Invocación y Casos de Uso

### 4.1 Invocación Automatizada por el Agente (Modo Autónomo o Componible)
Cuando un agente o usuario solicita:
> *"Construye la Matriz FODA para el proceso de Despacho y Distribución a partir del informe de auditoría de processAuditor y la matriz de stakeholders"*

El agente ejecuta `fodaProcess`:
1. Mapea los hallazgos de auditoría (ej: SoD roto en entrega, duplicación de remito papel) y los actores de [`stakeholderMatrix`](file:///c:/Users/Diego/.gemini/config/skills/stakeholderMatrix/SKILL.md).
2. Estructura exactamente entre 4 y 6 factores por cuadrante desplegando los 3 Ejes de cátedra.
3. Aplica el Test de Controlabilidad de cada factor.
4. Genera deterministamente el entregable `foda.md` usando la plantilla oficial [`templates/foda_process_template.md`](file:///c:/Users/Diego/.gemini/config/skills/fodaProcess/templates/foda_process_template.md).

### 4.2 Validación Sintáctica y Metodológica por CLI
```bash
# Validar el entregable foda.md generado
python scripts/validate_foda.py foda.md

# Validar la plantilla institucional
python scripts/validate_foda.py templates/foda_process_template.md

# Ejecutar la suite completa de tests unitarios
python -m unittest discover -s scripts
```

Salida esperada en validación exitosa:
```text
============================================================
VALIDACIÓN DE MATRIZ FODA DE PROCESO (fodaProcess)
============================================================
Archivo analizado: foda.md

[OK] Cuadrante 'Fortalezas': 6 factores detectados (F1, F2, F3, F4, F5, F6).
[OK] Cuadrante 'Debilidades': 6 factores detectados (D1, D2, D3, D4, D5, D6).
[OK] Cuadrante 'Oportunidades': 6 factores detectados (O1, O2, O3, O4, O5, O6).
[OK] Cuadrante 'Amenazas': 6 factores detectados (A1, A2, A3, A4, A5, A6).

------------------------------------------------------------
ESTADO: EXITOSO. La matriz cumple con todos los estándares canónicos.
============================================================
```

---

## 5. Especificación de Artefactos de Entrada y Salida (I/O)

### Entradas (Inputs)
- **Informe Forense de Auditoría ([`processAuditor`](file:///c:/Users/Diego/.gemini/config/skills/processAuditor/SKILL.md)):** Matriz RCM, conflictos de segregación de funciones (SoD), inventario de formularios en papel y mapa de silos TI.
- **Matriz de Partes Interesadas ([`stakeholderMatrix`](file:///c:/Users/Diego/.gemini/config/skills/stakeholderMatrix/SKILL.md)):** Resultados tangibles, expectativas cualitativas y obstáculos de los actores.
- **Minutas y Entrevistas Operativas:** Registros de relevamiento con identificadores `SRC-XX`.
- **Análisis de Entorno y Sector:** Tendencias de Lógica Dominante del Servicio (SDL), benchmarking tecnológico y marco regulatorio aplicable.

### Salidas (Outputs)
- **Archivo Canónico Obligatorio:** `foda.md` (guardado deterministamente en la raíz del espacio de trabajo).
- **Contenido Estructurado:**
  1. Metadatos del proceso y fuentes primarias auditadas.
  2. Resumen ejecutivo de balance situacional AS-IS.
  3. Matriz panorámica 2x2 sintética.
  4. Tablas detalladas por cuadrante con código unívoco (`F1`..`F6`, `D1`..`D6`, `O1`..`O6`, `A1`..`A6`), los 3 Ejes de Cátedra (Estrategia, Stakeholders, Resultados/Evidencia) y delimitación de gobernanza.
  5. Checklist de calidad metodológica y gobernanza.
  6. Puente hacia la formulación estratégica CAME ([`cameStrategizer`](file:///c:/Users/Diego/.gemini/config/skills/cameStrategizer/SKILL.md)).

---

## 6. Prevención de Anti-Patrones Metodológicos

| Anti-Patrón Común | Descripción del Error | Corrección Exigida por `fodaProcess` |
| :--- | :--- | :--- |
| **Confundir Oportunidad con Acción Interna** | Redactar *"Oportunidad: Desarrollar una app móvil o implementar un ERP"*. El desarrollo o compra es una decisión de gestión interna, no una condición del entorno. | Redactar el factor habilitador externo: *"Oportunidad: Oferta madura de plataformas SaaS logísticas con APIs abiertas y costos marginales reducidos"*. |
| **Confundir Amenaza con Debilidad Interna** | Redactar *"Amenaza: Los operarios cargan con demora los remitos"*. Es un fallo del proceso interno. | Redactar como Debilidad Interna ($D_x$): *"D2: Registro manual diferido de remitos que genera desincronización de 24h en el ERP"*. |
| **Debilidad sin Evidencia Fáctica** | Redactar afirmaciones ambiguas como *"El sistema es malo y hay mala comunicación"*. | Anclar a hallazgo de auditoría: *"D3: Interfaz desarticulada entre sistema de pesaje y ERP que obliga a reescribir 150 tickets diarios (Evidencia: RCM-04 / SRC-02)"*. |
| **Desbalance de Cuadrantes** | Matrices con 8 fortalezas, 1 debilidad y 2 amenazas. | Exigir entre 4 y 6 factores por cuadrante ($4 \le N \le 6$), forzando un examen riguroso y balanceado del proceso. |
| **Falta de Persistencia Canónica** | Generar salidas dispersas en el chat o en archivos con nombres variables. | Guardar deterministamente el entregable en `foda.md`. |
