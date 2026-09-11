#!/usr/bin/env python3
"""Validador y Generador de Matriz SIPOC (Suppliers, Inputs, Process, Outputs, Customers).

Verifica la gobernanza y rigor metodológico de la matriz SIPOC según los estándares
de Gestión y Mejora de Procesos (GMP / Ciclo PDCA - Cátedra TPI Etapa 2 Matriz 1):
1. Existencia y completitud de las 5 dimensiones fundamentales (S, I, P, O, C).
2. Regla canónica de 4 a 7 macroetapas en la dimensión Proceso (4 <= P <= 7).
3. Requisitos técnicos y criterios de calidad obligatorios para cada Entrada y Salida.
4. Delimitación explícita de fronteras (Límite de Inicio / Disparador y Límite de Fin / Evento Terminal).
5. Ausencia de orfandad y trazabilidad bidireccional (S -> I y O -> C).
6. Exportación y validación visual para diagramStudio (Mermaid flowchart LR y Draw.io XML).
"""

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

MIN_PROCESS_STEPS = 4
MAX_PROCESS_STEPS = 7

COLOR_STYLES = """    %% Estilos de Columnas SIPOC (diagramStudio preset)
    classDef sStyle fill:#ede7f6,stroke:#5e35b1,stroke-width:1.5px,color:#311b92;
    classDef iStyle fill:#e3f2fd,stroke:#1e88e5,stroke-width:1.5px,color:#0d47a1;
    classDef pStyle fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#1b5e20,font-weight:bold;
    classDef oStyle fill:#fff8e1,stroke:#fbc02d,stroke-width:1.5px,color:#f57f17;
    classDef cStyle fill:#fce4ec,stroke:#d81b60,stroke-width:1.5px,color:#880e4f;"""


class SipocModel:
    """Modelo estructurado de datos SIPOC con campos de cátedra GMP Etapa 2 Matriz 1."""

    def __init__(self) -> None:
        self.process_name: str = ""
        self.process_owner: str = ""
        self.client_principal: str = ""
        self.process_objective: str = ""
        self.process_scope: str = ""
        self.start_boundary: str = ""
        self.end_boundary: str = ""
        self.regulatory_framework: Dict[str, str] = {}
        self.value_created: str = ""
        self.suppliers: List[Dict[str, str]] = []  # [{"id": "S1", "name": "...", "type": "externo/proceso_mapa"}]
        self.inputs: List[Dict[str, str]] = []     # [{"id": "I1", "name": "...", "supplier": "...", "requirement": "...", "format": "..."}]
        self.process_steps: List[Dict[str, str]] = []  # [{"id": "P1", "name": "..."}]
        self.outputs: List[Dict[str, str]] = []    # [{"id": "O1", "name": "...", "customer": "...", "requirement": "...", "criteria": "..."}]
        self.customers: List[Dict[str, str]] = []  # [{"id": "C1", "name": "...", "type": "principal/proceso/mercado"}]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "process_name": self.process_name,
            "process_owner": self.process_owner,
            "client_principal": self.client_principal,
            "process_objective": self.process_objective,
            "process_scope": self.process_scope,
            "start_boundary": self.start_boundary,
            "end_boundary": self.end_boundary,
            "regulatory_framework": self.regulatory_framework,
            "value_created": self.value_created,
            "suppliers": self.suppliers,
            "inputs": self.inputs,
            "process_steps": self.process_steps,
            "outputs": self.outputs,
            "customers": self.customers,
        }


def validate_sipoc_data(data: SipocModel) -> List[str]:
    """Ejecuta todas las reglas de validación sobre el modelo SIPOC."""
    errors: List[str] = []

    # 1. Validación de Fronteras
    invalid_boundary_values = ["[tbd]", "tbd", "[definir]", "definir", "[definir frontera]", "n/a", "na", "-"]
    if not data.start_boundary or data.start_boundary.strip().lower() in invalid_boundary_values:
        errors.append("Falta definir la frontera de inicio (Disparador / Límite de Inicio).")
    if not data.end_boundary or data.end_boundary.strip().lower() in invalid_boundary_values:
        errors.append("Falta definir la frontera de fin (Evento Terminal / Límite de Fin).")

    # 2. Validación de las 5 dimensiones fundamentales existentes
    if not data.suppliers:
        errors.append("Dimensión Proveedores (S) vacía. Debe declararse al menos 1 proveedor.")
    if not data.inputs:
        errors.append("Dimensión Entradas (I) vacía. Debe declararse al menos 1 entrada/insumo.")
    if not data.outputs:
        errors.append("Dimensión Salidas (O) vacía. Debe declararse al menos 1 salida/resultado.")
    if not data.customers:
        errors.append("Dimensión Clientes (C) vacía. Debe declararse al menos 1 cliente/destinatario.")

    # 3. Regla Canónica de Macroetapas de Proceso (4 a 7)
    step_count = len(data.process_steps)
    if step_count < MIN_PROCESS_STEPS:
        errors.append(
            f"El macroproceso tiene {step_count} etapas. Debe contener entre {MIN_PROCESS_STEPS} y {MAX_PROCESS_STEPS} "
            f"macroetapas (sub-delimitación: menos de {MIN_PROCESS_STEPS} no define un proceso completo)."
        )
    elif step_count > MAX_PROCESS_STEPS:
        errors.append(
            f"El macroproceso tiene {step_count} etapas. Debe contener entre {MIN_PROCESS_STEPS} y {MAX_PROCESS_STEPS} "
            f"macroetapas (sobre-especificación: más de {MAX_PROCESS_STEPS} degenera en nivel de tarea u operativo)."
        )

    # 4. Inferencia inteligente de proveedores/clientes únicos si no fueron mapeados
    if len(data.suppliers) == 1:
        default_supp = data.suppliers[0].get("name", "Proveedor Principal")
        for inp in data.inputs:
            if not inp.get("supplier"):
                inp["supplier"] = default_supp

    if len(data.customers) == 1:
        default_cust = data.customers[0].get("name", "Cliente Principal")
        for out in data.outputs:
            if not out.get("customer"):
                out["customer"] = default_cust

    # 5. Validación de Requisitos Técnicos Obligatorios en Entradas
    invalid_req_values = [
        "", "[tbd]", "tbd", "[definir requisito]", "[definir]", "definir",
        "n/a", "na", "-", "none", "ninguno", "pendiente", "[pendiente]"
    ]
    for idx, inp in enumerate(data.inputs, start=1):
        inp_id = inp.get("id", f"I{idx}")
        inp_name = inp.get("name", "").strip()
        req = inp.get("requirement", "").strip()
        supp = inp.get("supplier", "").strip()

        if not inp_name:
            errors.append(f"Entrada [{inp_id}]: Nombre o descripción del insumo vacío.")
        if not req or req.lower() in invalid_req_values:
            errors.append(
                f"Entrada [{inp_id} - '{inp_name}']: Requisito técnico o especificación de calidad faltante o vacío. "
                "Toda entrada debe declarar criterios de aceptación técnicos (formato, tolerancia, frescura, completitud)."
            )
        if not supp or supp.lower() in ["[tbd]", "tbd", "[definir]", "[definir proveedor]"]:
            errors.append(
                f"Entrada [{inp_id} - '{inp_name}']: Proveedor de origen no identificado (orfandad de entrada). "
                "Toda entrada debe provenir de al menos un proveedor externo o proceso del mapa identificado."
            )

    # 6. Validación de Requisitos Técnicos Obligatorios en Salidas
    for idx, out in enumerate(data.outputs, start=1):
        out_id = out.get("id", f"O{idx}")
        out_name = out.get("name", "").strip()
        req = out.get("requirement", "").strip()
        cust = out.get("customer", "").strip()

        if not out_name:
            errors.append(f"Salida [{out_id}]: Nombre o descripción de salida vacía.")
        if not req or req.lower() in invalid_req_values:
            errors.append(
                f"Salida [{out_id} - '{out_name}']: Especificación de calidad o SLA faltante o vacío. "
                "Toda salida debe declarar estándares de calidad verificables (SLA, umbral de tolerancia, formato de entrega)."
            )
        if not cust or cust.lower() in ["[tbd]", "tbd", "[definir]", "[definir cliente]"]:
            errors.append(
                f"Salida [{out_id} - '{out_name}']: Cliente o destinatario no identificado (orfandad de salida). "
                "Toda salida debe tener al menos un cliente principal, proceso interno o destinatario externo."
            )

    return errors


def is_subheading_item(val: str) -> bool:
    """Detecta si una línea en la celda es un subtítulo o categoría en lugar de un ítem de negocio."""
    v = val.strip()
    if not v:
        return True

    # Si contiene un ID formal de ítem de SIPOC (ej. S1:, I1:, P1:, O1:, C1:), NUNCA es un subtítulo
    if re.search(r"\b[siopc]\d+[:\.\s-]", v, re.IGNORECASE):
        return False

    # Si la línea está envuelta en negrita como subtítulo: **Proveedores Externos:** o **Clientes Internos:**
    if re.match(r"^[-*•\s]*\*\*[^*]+:\*\*\s*$", v):
        return True
    if re.match(r"^[-*•\s]*\*\*(?:proveedores?|clientes?|procesos?|entradas?|salidas?|insumos?|sociedad)[^*]*\*\*\s*:?$", v, re.IGNORECASE):
        return True

    # Texto limpio de markdown, paréntesis y puntuación
    cleaned = re.sub(r"[*_:`~#]", "", v).strip().lower()
    cleaned = re.sub(r"\(.*?\)", "", cleaned).strip()
    known_category_headers = {
        "proveedores externos", "proveedor externo", "proveedores internos",
        "procesos del mapa", "proceso del mapa", "procesos clave", "procesos de soporte",
        "procesos estrategicos", "procesos estratégicos",
        "cliente principal", "clientes principales", "clientes internos", "cliente interno",
        "cliente externo", "clientes externos", "cliente externo / sociedad", "sociedad",
        "sociedad y mercado", "mercado y sociedad", "regulador", "entes reguladores",
        "macroproceso", "macroetapas", "entradas e insumos", "entradas / insumos",
        "salidas y entregables", "salidas / entregables",
        "insumos", "entradas", "salidas", "entregables", "proveedores", "clientes"
    }
    if cleaned in known_category_headers:
        return True

    # Solo si termina en ':' y parece un encabezado de categoría
    if v.rstrip("*_ \t").endswith(":"):
        if any(cat in cleaned for cat in ["proveedor", "cliente", "mapa", "macroproceso", "etapa"]):
            return True

    return False


def _clean_str(text: str) -> str:
    """Limpia formato markdown de una celda o texto (backticks, comillas, espacios)."""
    return text.strip("`'\" \t\r\n")


def _detect_column_mapping(headers: List[str], table_type: str) -> Dict[str, int]:
    """Determina los índices de columnas según los encabezados de tabla de requisitos."""
    mapping: Dict[str, int] = {}
    for idx, h in enumerate(headers):
        hl = h.strip().lower()
        if re.search(r"\b(?:id|c[oó]digo)\b", hl) and "id" not in mapping:
            mapping["id"] = idx
        elif any(k in hl for k in ["entrada", "insumo", "input"]) and "name" not in mapping and table_type == "inputs":
            mapping["name"] = idx
        elif any(k in hl for k in ["salida", "entregable", "output", "producto", "resultado"]) and "name" not in mapping and table_type == "outputs":
            mapping["name"] = idx
        elif any(k in hl for k in ["proveedor", "supplier", "origen"]) and "actor" not in mapping:
            mapping["actor"] = idx
        elif any(k in hl for k in ["cliente", "destinatario", "customer"]) and "actor" not in mapping:
            mapping["actor"] = idx
        elif any(k in hl for k in ["requisito", "especificaci", "sla", "calidad", "tolerancia"]) and "req" not in mapping:
            mapping["req"] = idx
        elif any(k in hl for k in ["criterio", "conformidad", "aceptaci[oó]n", "formato", "medio", "captura", "soporte"]) and "extra" not in mapping:
            mapping["extra"] = idx

    # Valores por defecto si no se detectaron encabezados explícitos
    if "name" not in mapping:
        mapping["name"] = 1 if ("id" in mapping and mapping["id"] == 0) else 0
    if "actor" not in mapping and len(headers) >= 3:
        mapping["actor"] = 2 if "id" in mapping else 1
    if "req" not in mapping:
        for i in range(len(headers)):
            if i not in mapping.values():
                mapping["req"] = i
                break
    return mapping


def parse_markdown_sipoc(content: str) -> SipocModel:
    """Parsea un archivo Markdown sipoc.md extrayendo las dimensiones y requisitos técnicos."""
    model = SipocModel()

    # 1. Extraer Nombre del Proceso
    match_proc = re.search(
        r"\*\*.*?(?:Nombre\s+del\s+)?Proceso(?:\s+u\s+Operación|\s+Analizado)?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_proc:
        model.process_name = _clean_str(match_proc.group(1))
    else:
        # Fallback a encabezado principal H1
        match_h1 = re.search(r"^#\s+(?:Matriz\s+SIPOC:\s*)(.+)$", content, re.MULTILINE | re.IGNORECASE)
        if match_h1:
            raw_title = match_h1.group(1).strip()
            clean_title = re.sub(r"\(.*?\)", "", raw_title).strip()
            model.process_name = _clean_str(clean_title)

    # 2. Dueño / Responsable
    match_owner = re.search(
        r"\*\*.*?(?:Dueño|Responsable|L[íi]der|Propietario).*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_owner:
        model.process_owner = _clean_str(match_owner.group(1))

    # 3. Cliente Principal
    match_client = re.search(
        r"\*\*.*?(?:Cliente\s+Principal|Beneficiario\s+Principal).*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_client:
        model.client_principal = _clean_str(match_client.group(1))

    # 4. Objetivo del Proceso
    match_obj = re.search(
        r"\*\*.*?(?:Objetivo(?:\s+del\s+Proceso)?|Prop[oó]sito).*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_obj:
        model.process_objective = _clean_str(match_obj.group(1))

    # 5. Alcance Operativo
    match_scope = re.search(
        r"\*\*.*?(?:Alcance(?:\s+Operativo)?).*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_scope:
        model.process_scope = _clean_str(match_scope.group(1))

    # 6. Fronteras de Inicio y Fin
    match_start = re.search(
        r"\*\*.*?(?:Disparador|L[íi]mite\s+de\s+Inicio|Frontera\s+de\s+Inicio|Hito\s+de\s+Inicio|Inicio|Desde).*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_start:
        model.start_boundary = _clean_str(match_start.group(1))

    match_end = re.search(
        r"\*\*.*?(?:Evento\s+Terminal|L[íi]mite\s+de\s+Fin|Frontera\s+de\s+Fin|Hito\s+de\s+Fin|Fin|Hasta|T[eé]rmino).*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_end:
        model.end_boundary = _clean_str(match_end.group(1))

    # 7. Valor Creado
    match_val = re.search(
        r"\*\*.*?(?:Valor\s+Creado|Propuesta\s+de\s+Valor|Valor\s+Agregado).*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_val:
        model.value_created = _clean_str(match_val.group(1))

    # 8. Marco Regulatorio
    match_reg_ext = re.search(
        r"\*\*.*?(?:Normativa|Normas?|Regulaci[oó]n|Marco\s+Regulatorio)\s+Extern[ao]s?.*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    match_reg_int = re.search(
        r"\*\*.*?(?:Reglas?(?:\s+de\s+Negocio)?|Normativa|Normas?|Pol[íi]ticas?)\s+Intern[ao]s?.*?:\*\*\s*`?([^`\r\n]+)`?",
        content,
        re.IGNORECASE,
    )
    if match_reg_ext or match_reg_int:
        model.regulatory_framework = {
            "external": _clean_str(match_reg_ext.group(1)) if match_reg_ext else "",
            "internal": _clean_str(match_reg_int.group(1)) if match_reg_int else "",
        }

    # 9. Parsing de Tablas Markdown con detección determinista de cabeceras
    in_table_req_inputs = False
    in_table_req_outputs = False
    in_table_sipoc_main = False

    inputs_col_map: Dict[str, int] = {}
    outputs_col_map: Dict[str, int] = {}

    lines = content.splitlines()
    for idx, line in enumerate(lines):
        stripped = line.strip()

        # Detección de encabezados de sección
        if re.search(r"##\s+.*(?:Requisitos|Especificaciones).*(?:Entrada|Insumo)", stripped, re.IGNORECASE):
            in_table_req_inputs = True
            in_table_req_outputs = False
            in_table_sipoc_main = False
            inputs_col_map = {}
            continue
        elif re.search(r"##\s+.*(?:Requisitos|Especificaciones).*(?:Salida|Entregable)", stripped, re.IGNORECASE):
            in_table_req_inputs = False
            in_table_req_outputs = True
            in_table_sipoc_main = False
            outputs_col_map = {}
            continue
        elif re.search(r"##\s+.*(?:Matriz\s+SIPOC|Tabla\s+SIPOC|SIPOC\s+Principal)", stripped, re.IGNORECASE):
            in_table_req_inputs = False
            in_table_req_outputs = False
            in_table_sipoc_main = True
            continue
        elif stripped.startswith("## "):
            in_table_req_inputs = False
            in_table_req_outputs = False
            in_table_sipoc_main = False

        if not stripped.startswith("|"):
            continue

        cols = [c.strip() for c in stripped.split("|")[1:-1]]
        if not cols:
            continue

        # Fila de separación de tabla (|---|---|...)
        if all(re.match(r"^:?-+:?$", c) for c in cols):
            continue

        # Comprobar si la siguiente línea es la fila de separación de la tabla (|---|...)
        next_is_separator = False
        if idx + 1 < len(lines):
            next_stripped = lines[idx + 1].strip()
            if next_stripped.startswith("|"):
                next_cols = [c.strip() for c in next_stripped.split("|")[1:-1]]
                if next_cols and all(re.match(r"^:?-+:?$", c) for c in next_cols):
                    next_is_separator = True

        if next_is_separator:
            # Esta fila es la cabecera de la tabla
            header_text = " ".join(cols).lower()
            if ("proveedor" in header_text or "supplier" in header_text) and \
               ("proceso" in header_text or "process" in header_text) and \
               (("entrada" in header_text or "insumo" in header_text or "input" in header_text) or
                ("salida" in header_text or "output" in header_text or "entregable" in header_text)):
                in_table_sipoc_main = True
                in_table_req_inputs = False
                in_table_req_outputs = False
            elif in_table_req_inputs or any(k in header_text for k in ["entrada", "insumo", "input"]):
                in_table_req_inputs = True
                in_table_req_outputs = False
                in_table_sipoc_main = False
                inputs_col_map = _detect_column_mapping(cols, "inputs")
            elif in_table_req_outputs or any(k in header_text for k in ["salida", "entregable", "output", "producto"]):
                in_table_req_inputs = False
                in_table_req_outputs = True
                in_table_sipoc_main = False
                outputs_col_map = _detect_column_mapping(cols, "outputs")
            continue

        # Si llegamos aquí, la fila es una fila de datos

        # Parsing de Tabla 3: Requisitos Técnicos de Entradas
        if in_table_req_inputs:
            if not inputs_col_map:
                inputs_col_map = _detect_column_mapping(cols, "inputs")

            id_idx = inputs_col_map.get("id")
            name_idx = inputs_col_map.get("name", 0)
            actor_idx = inputs_col_map.get("actor")
            req_idx = inputs_col_map.get("req", 2 if len(cols) > 2 else 1)
            extra_idx = inputs_col_map.get("extra")

            inp_id_raw = cols[id_idx] if (id_idx is not None and id_idx < len(cols)) else ""
            inp_id_match = re.match(r"^(I\d+)\b", inp_id_raw.strip(), re.IGNORECASE)
            inp_id = inp_id_match.group(1).upper() if inp_id_match else ""

            name = _clean_str(cols[name_idx]) if (name_idx < len(cols)) else ""
            supp = _clean_str(cols[actor_idx]) if (actor_idx is not None and actor_idx < len(cols)) else ""
            req = _clean_str(cols[req_idx]) if (req_idx < len(cols)) else ""
            fmt = _clean_str(cols[extra_idx]) if (extra_idx is not None and extra_idx < len(cols)) else ""

            if not name and not req and not inp_id:
                continue

            # Buscar si ya existe la entrada por ID o por coincidencia de nombre
            existing = None
            if inp_id:
                existing = next((x for x in model.inputs if x.get("id", "").upper() == inp_id), None)
            if not existing and name:
                norm_name = name.lower()
                existing = next(
                    (x for x in model.inputs if x.get("name", "").lower() == norm_name or
                     (norm_name in x.get("name", "").lower() and len(norm_name) > 3)),
                    None,
                )

            if existing:
                if req:
                    existing["requirement"] = req
                if supp and not existing.get("supplier"):
                    existing["supplier"] = supp
                if fmt and not existing.get("format"):
                    existing["format"] = fmt
                if name and (existing.get("name", "").startswith("[") or len(name) > len(existing.get("name", ""))):
                    existing["name"] = name
            else:
                assigned_id = inp_id or f"I{len(model.inputs) + 1}"
                model.inputs.append({
                    "id": assigned_id,
                    "name": name,
                    "supplier": supp,
                    "requirement": req,
                    "format": fmt,
                })

        # Parsing de Tabla 4: Requisitos Técnicos de Salidas
        elif in_table_req_outputs:
            if not outputs_col_map:
                outputs_col_map = _detect_column_mapping(cols, "outputs")

            id_idx = outputs_col_map.get("id")
            name_idx = outputs_col_map.get("name", 0)
            actor_idx = outputs_col_map.get("actor")
            req_idx = outputs_col_map.get("req", 2 if len(cols) > 2 else 1)
            extra_idx = outputs_col_map.get("extra")

            out_id_raw = cols[id_idx] if (id_idx is not None and id_idx < len(cols)) else ""
            out_id_match = re.match(r"^(O\d+)\b", out_id_raw.strip(), re.IGNORECASE)
            out_id = out_id_match.group(1).upper() if out_id_match else ""

            name = _clean_str(cols[name_idx]) if (name_idx < len(cols)) else ""
            cust = _clean_str(cols[actor_idx]) if (actor_idx is not None and actor_idx < len(cols)) else ""
            req = _clean_str(cols[req_idx]) if (req_idx < len(cols)) else ""
            crit = _clean_str(cols[extra_idx]) if (extra_idx is not None and extra_idx < len(cols)) else ""

            if not name and not req and not out_id:
                continue

            existing = None
            if out_id:
                existing = next((x for x in model.outputs if x.get("id", "").upper() == out_id), None)
            if not existing and name:
                norm_name = name.lower()
                existing = next(
                    (x for x in model.outputs if x.get("name", "").lower() == norm_name or
                     (norm_name in x.get("name", "").lower() and len(norm_name) > 3)),
                    None,
                )

            if existing:
                if req:
                    existing["requirement"] = req
                if cust and not existing.get("customer"):
                    existing["customer"] = cust
                if crit and not existing.get("criteria"):
                    existing["criteria"] = crit
                if name and (existing.get("name", "").startswith("[") or len(name) > len(existing.get("name", ""))):
                    existing["name"] = name
            else:
                assigned_id = out_id or f"O{len(model.outputs) + 1}"
                model.outputs.append({
                    "id": assigned_id,
                    "name": name,
                    "customer": cust,
                    "requirement": req,
                    "criteria": crit,
                })

        # Parsing de Tabla 2: Matriz SIPOC Principal (5 columnas)
        elif in_table_sipoc_main:
            if len(cols) >= 5:
                s_val, i_val, p_val, o_val, c_val = cols[0], cols[1], cols[2], cols[3], cols[4]

                # 1. Proveedores (S)
                if s_val:
                    for item in re.split(r"<br\s*/?>|\n|;\s*", s_val):
                        item_raw = item.strip()
                        if not item_raw or is_subheading_item(item_raw):
                            continue
                        clean_item = re.sub(r"^[-*•]\s+", "", item_raw).strip()
                        clean_item = _clean_str(clean_item)
                        match_id = re.match(r"^(S\d+)[:\.\s-]+(.+)$", clean_item, re.IGNORECASE)
                        s_id = match_id.group(1).upper() if match_id else f"S{len(model.suppliers) + 1}"
                        s_name = _clean_str(match_id.group(2)) if match_id else clean_item
                        if not any(s["name"] == s_name for s in model.suppliers):
                            model.suppliers.append({"id": s_id, "name": s_name})

                # 2. Entradas (I)
                if i_val:
                    for item in re.split(r"<br\s*/?>|\n|;\s*", i_val):
                        item_raw = item.strip()
                        if not item_raw or is_subheading_item(item_raw):
                            continue
                        clean_item = re.sub(r"^[-*•]\s+", "", item_raw).strip()
                        clean_item = _clean_str(clean_item)
                        match_id = re.match(r"^(I\d+)[:\.\s-]+(.+)$", clean_item, re.IGNORECASE)
                        i_id = match_id.group(1).upper() if match_id else f"I{len(model.inputs) + 1}"
                        i_name = _clean_str(match_id.group(2)) if match_id else clean_item
                        if not any(inp["name"] == i_name for inp in model.inputs):
                            model.inputs.append({"id": i_id, "name": i_name, "requirement": ""})

                # 3. Macroproceso (P)
                if p_val:
                    for item in re.split(r"<br\s*/?>|\n|;\s*", p_val):
                        item_raw = item.strip()
                        if not item_raw or is_subheading_item(item_raw):
                            continue
                        clean_item = re.sub(r"^[-*•]\s+", "", item_raw).strip()
                        clean_item = _clean_str(clean_item)
                        match_id = re.match(r"^(?:P?(\d+)|\bStep\s*(\d+))[:\.\)\s-]+(.+)$", clean_item, re.IGNORECASE)
                        if match_id:
                            step_num = match_id.group(1) or match_id.group(2)
                            p_id = f"P{step_num}"
                            p_name = _clean_str(match_id.group(3))
                        else:
                            p_id = f"P{len(model.process_steps) + 1}"
                            p_name = _clean_str(re.sub(r"^\d+[\.\)]\s*", "", clean_item))

                        if not any(p["id"].upper() == p_id.upper() for p in model.process_steps):
                            model.process_steps.append({"id": p_id, "name": p_name})

                # 4. Salidas (O)
                if o_val:
                    for item in re.split(r"<br\s*/?>|\n|;\s*", o_val):
                        item_raw = item.strip()
                        if not item_raw or is_subheading_item(item_raw):
                            continue
                        clean_item = re.sub(r"^[-*•]\s+", "", item_raw).strip()
                        clean_item = _clean_str(clean_item)
                        match_id = re.match(r"^(O\d+)[:\.\s-]+(.+)$", clean_item, re.IGNORECASE)
                        o_id = match_id.group(1).upper() if match_id else f"O{len(model.outputs) + 1}"
                        o_name = _clean_str(match_id.group(2)) if match_id else clean_item
                        if not any(out["name"] == o_name for out in model.outputs):
                            model.outputs.append({"id": o_id, "name": o_name, "requirement": ""})

                # 5. Clientes (C)
                if c_val:
                    for item in re.split(r"<br\s*/?>|\n|;\s*", c_val):
                        item_raw = item.strip()
                        if not item_raw or is_subheading_item(item_raw):
                            continue
                        clean_item = re.sub(r"^[-*•]\s+", "", item_raw).strip()
                        clean_item = _clean_str(clean_item)
                        match_id = re.match(r"^(C\d+)[:\.\s-]+(.+)$", clean_item, re.IGNORECASE)
                        c_id = match_id.group(1).upper() if match_id else f"C{len(model.customers) + 1}"
                        c_name = _clean_str(match_id.group(2)) if match_id else clean_item
                        if not any(c["name"] == c_name for c in model.customers):
                            model.customers.append({"id": c_id, "name": c_name})

    # Si los pasos del proceso se listaron fuera de la tabla en un bloque numerado o viñetas
    if not model.process_steps:
        p_matches = re.findall(r"(?:^|[\r\n])\s*(?:[-*•\d\.]+\s+)?(P\d+)[:\.\s-]+([^\r\n]+)", content, re.IGNORECASE)
        for p_id, p_name in p_matches:
            model.process_steps.append({"id": p_id.upper(), "name": _clean_str(p_name)})

    return model


def parse_json_sipoc(json_str: str) -> SipocModel:
    """Parsea un payload JSON estructurado a SipocModel con campos de cátedra GMP."""
    data = json.loads(json_str)
    model = SipocModel()
    model.process_name = data.get("process_name", "")
    model.process_owner = data.get("process_owner", "")
    model.client_principal = data.get("client_principal", "")
    model.process_objective = data.get("process_objective", "")
    model.process_scope = data.get("process_scope", "")
    model.start_boundary = data.get("start_boundary", "")
    model.end_boundary = data.get("end_boundary", "")
    model.regulatory_framework = data.get("regulatory_framework", {})
    model.value_created = data.get("value_created", "")
    model.suppliers = data.get("suppliers", [])
    model.inputs = data.get("inputs", [])
    model.process_steps = data.get("process_steps", [])
    model.outputs = data.get("outputs", [])
    model.customers = data.get("customers", [])
    return model


def _format_mermaid_node_label(item_id: str, raw_name: str) -> str:
    """Limpia el label de un nodo Mermaid evitando prefijos duplicados (ej. P1: P1:)."""
    name = _clean_str(raw_name)
    # Remover prefijo de ID si ya lo tiene (ej. 'P1:', 'P1 -', 'P1.')
    name = re.sub(rf"^{re.escape(item_id)}[:\.\s-]+", "", name, flags=re.IGNORECASE).strip()
    name_esc = name.replace('"', '\\"')
    return f'{item_id}: {name_esc}'


def _safe_mermaid_id(raw_id: str) -> str:
    """Convierte un identificador en un nombre seguro para Mermaid."""
    return re.sub(r"[^a-zA-Z0-9_]", "_", raw_id)


def generate_mermaid_diagram(data: SipocModel) -> str:
    """Genera el código Mermaid flowchart LR conforme al preset diagramStudio."""
    lines: List[str] = [
        "```mermaid",
        "flowchart LR",
        "    %% Columnas SIPOC",
    ]

    # Subgraph S (Proveedores)
    lines.append('    subgraph S ["1. PROVEEDORES (Suppliers)"]')
    lines.append("        direction TB")
    s_ids: List[str] = []
    for idx, supp in enumerate(data.suppliers, start=1):
        s_id = supp.get("id", f"S{idx}")
        safe_id = _safe_mermaid_id(s_id)
        s_ids.append(safe_id)
        label = _format_mermaid_node_label(s_id, supp.get("name", f"Proveedor {idx}"))
        lines.append(f'        {safe_id}["{label}"]')
    lines.append("    end")
    lines.append("")

    # Subgraph I (Entradas)
    lines.append('    subgraph I ["2. ENTRADAS (Inputs)"]')
    lines.append("        direction TB")
    i_ids: List[str] = []
    for idx, inp in enumerate(data.inputs, start=1):
        i_id = inp.get("id", f"I{idx}")
        safe_id = _safe_mermaid_id(i_id)
        i_ids.append(safe_id)
        label = _format_mermaid_node_label(i_id, inp.get("name", f"Entrada {idx}"))
        lines.append(f'        {safe_id}["{label}"]')
    lines.append("    end")
    lines.append("")

    # Subgraph P (Proceso - 4 a 7 Macroetapas)
    step_count = len(data.process_steps)
    lines.append(f'    subgraph P ["3. PROCESO (Process - {step_count} Macroetapas)"]')
    lines.append("        direction TB")
    p_ids: List[str] = []
    for idx, step in enumerate(data.process_steps, start=1):
        p_id = step.get("id", f"P{idx}")
        safe_id = _safe_mermaid_id(p_id)
        p_ids.append(safe_id)
        label = _format_mermaid_node_label(p_id, step.get("name", f"Paso {idx}"))
        lines.append(f'        {safe_id}["{label}"]')
    if len(p_ids) > 1:
        seq_flow = " --> ".join(p_ids)
        lines.append(f"        {seq_flow}")
    lines.append("    end")
    lines.append("")

    # Subgraph O (Salidas)
    lines.append('    subgraph O ["4. SALIDAS (Outputs)"]')
    lines.append("        direction TB")
    o_ids: List[str] = []
    for idx, out in enumerate(data.outputs, start=1):
        o_id = out.get("id", f"O{idx}")
        safe_id = _safe_mermaid_id(o_id)
        o_ids.append(safe_id)
        label = _format_mermaid_node_label(o_id, out.get("name", f"Salida {idx}"))
        lines.append(f'        {safe_id}["{label}"]')
    lines.append("    end")
    lines.append("")

    # Subgraph C (Clientes)
    lines.append('    subgraph C ["5. CLIENTES (Customers)"]')
    lines.append("        direction TB")
    c_ids: List[str] = []
    for idx, cust in enumerate(data.customers, start=1):
        c_id = cust.get("id", f"C{idx}")
        safe_id = _safe_mermaid_id(c_id)
        c_ids.append(safe_id)
        label = _format_mermaid_node_label(c_id, cust.get("name", f"Cliente {idx}"))
        lines.append(f'        {safe_id}["{label}"]')
    lines.append("    end")
    lines.append("")

    # Conectores principales entre columnas
    lines.append("    %% Relaciones de Flujo")
    lines.append("    S ==> I")
    lines.append("    I ==> P")
    lines.append("    P ==> O")
    lines.append("    O ==> C")
    lines.append("")

    # Estilos de clases canónicas
    lines.append(COLOR_STYLES)
    lines.append("")

    # Asignación de clases
    if s_ids:
        lines.append(f"    class {','.join(s_ids)} sStyle;")
    if i_ids:
        lines.append(f"    class {','.join(i_ids)} iStyle;")
    if p_ids:
        lines.append(f"    class {','.join(p_ids)} pStyle;")
    if o_ids:
        lines.append(f"    class {','.join(o_ids)} oStyle;")
    if c_ids:
        lines.append(f"    class {','.join(c_ids)} cStyle;")

    lines.append("```")
    return "\n".join(lines)


def generate_drawio_diagram(data: SipocModel) -> str:
    """Genera archivo XML Draw.io (.drawio) conforme al preset oficial diagramStudio.
    
    Implementa:
    - 5 columnas uniformes de 220px con cabeceras temáticas coloreadas.
    - Cajas de contenido delimitadas y tarjetas para cada ítem enumerado.
    - Flechas secuenciales entre las macroetapas del proceso.
    - Flechas de flujo macro S -> I -> P -> O -> C entre encabezados.
    """
    col_width = 220
    col_gap = 30
    header_height = 40
    lane_height = 560
    card_height = 55
    start_x = 40
    start_y = 50

    columns_config = [
        {"key": "S", "title": "1. PROVEEDORES (Suppliers)", "items": data.suppliers, "prefix": "S",
         "style_header": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ede7f6;strokeColor=#5e35b1;fontColor=#311b92;fontStyle=1;fontSize=12;",
         "style_card": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#5e35b1;fontColor=#311b92;fontSize=11;strokeWidth=1.5;"},
        {"key": "I", "title": "2. ENTRADAS (Inputs)", "items": data.inputs, "prefix": "I",
         "style_header": "rounded=1;whiteSpace=wrap;html=1;fillColor=#e3f2fd;strokeColor=#1e88e5;fontColor=#0d47a1;fontStyle=1;fontSize=12;",
         "style_card": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1e88e5;fontColor=#0d47a1;fontSize=11;strokeWidth=1.5;"},
        {"key": "P", "title": f"3. PROCESO ({len(data.process_steps)} Macroetapas)", "items": data.process_steps, "prefix": "P",
         "style_header": "rounded=1;whiteSpace=wrap;html=1;fillColor=#e8f5e9;strokeColor=#43a047;fontColor=#1b5e20;fontStyle=1;fontSize=12;",
         "style_card": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#43a047;fontColor=#1b5e20;fontSize=11;fontStyle=1;strokeWidth=2;"},
        {"key": "O", "title": "4. SALIDAS (Outputs)", "items": data.outputs, "prefix": "O",
         "style_header": "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff8e1;strokeColor=#fbc02d;fontColor=#f57f17;fontStyle=1;fontSize=12;",
         "style_card": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#fbc02d;fontColor=#f57f17;fontSize=11;strokeWidth=1.5;"},
        {"key": "C", "title": "5. CLIENTES (Customers)", "items": data.customers, "prefix": "C",
         "style_header": "rounded=1;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#d81b60;fontColor=#880e4f;fontStyle=1;fontSize=12;",
         "style_card": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d81b60;fontColor=#880e4f;fontSize=11;strokeWidth=1.5;"},
    ]

    total_width = start_x * 2 + 5 * col_width + 4 * col_gap

    lines: List[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<mxfile host="drawio" version="26.0.0">',
        f'  <diagram name="SIPOC: {html.escape(data.process_name or "Proceso")}" id="sipoc-diagram">',
        f'    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{total_width}" pageHeight="720" background="#ffffff">',
        '      <root>',
        '        <mxCell id="0" />',
        '        <mxCell id="1" parent="0" />',
    ]

    cell_id = 2
    header_cell_ids: List[int] = []
    process_card_ids: List[int] = []

    for col_idx, col in enumerate(columns_config):
        x = start_x + col_idx * (col_width + col_gap)

        # 1. Contenedor de columna de fondo (swimlane visual)
        bg_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#fafafa;strokeColor=#e0e0e0;strokeWidth=1;dashed=1;"
        lines.append(
            f'        <mxCell id="{cell_id}" value="" style="{bg_style}" vertex="1" parent="1">'
        )
        lines.append(
            f'          <mxGeometry x="{x}" y="{start_y}" width="{col_width}" height="{lane_height}" as="geometry" />'
        )
        lines.append('        </mxCell>')
        cell_id += 1

        # 2. Encabezado de Columna
        header_val = html.escape(col["title"])
        header_id = cell_id
        header_cell_ids.append(header_id)
        lines.append(
            f'        <mxCell id="{header_id}" value="{header_val}" style="{col["style_header"]}" vertex="1" parent="1">'
        )
        lines.append(
            f'          <mxGeometry x="{x}" y="{start_y}" width="{col_width}" height="{header_height}" as="geometry" />'
        )
        lines.append('        </mxCell>')
        cell_id += 1

        # 3. Tarjetas de Ítems
        card_y = start_y + header_height + 15
        items = col["items"]
        for idx, it in enumerate(items, start=1):
            it_id = it.get("id", f"{col['prefix']}{idx}")
            raw_name = it.get("name", f"Item {idx}")
            clean_name = _clean_str(raw_name)
            clean_name = re.sub(rf"^{re.escape(it_id)}[:\.\s-]+", "", clean_name, flags=re.IGNORECASE).strip()

            val_text = f"<b>{html.escape(it_id)}</b>: {html.escape(clean_name)}"
            current_card_id = cell_id
            if col["key"] == "P":
                process_card_ids.append(current_card_id)

            lines.append(
                f'        <mxCell id="{current_card_id}" value="{val_text}" style="{col["style_card"]}" vertex="1" parent="1">'
            )
            lines.append(
                f'          <mxGeometry x="{x + 10}" y="{card_y}" width="{col_width - 20}" height="{card_height}" as="geometry" />'
            )
            lines.append('        </mxCell>')
            cell_id += 1
            card_y += card_height + 12

    # 4. Flechas entre macroetapas del Proceso (P1 -> P2 -> ... -> Pn)
    for i in range(len(process_card_ids) - 1):
        source_id = process_card_ids[i]
        target_id = process_card_ids[i + 1]
        p_edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#43a047;strokeWidth=2;"
        lines.append(
            f'        <mxCell id="{cell_id}" value="" style="{p_edge_style}" edge="1" parent="1" source="{source_id}" target="{target_id}">'
        )
        lines.append('          <mxGeometry relative="1" as="geometry" />')
        lines.append('        </mxCell>')
        cell_id += 1

    # 5. Flechas macro de flujo entre columnas (S -> I -> P -> O -> C)
    for i in range(len(header_cell_ids) - 1):
        source_id = header_cell_ids[i]
        target_id = header_cell_ids[i + 1]
        macro_edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#757575;strokeWidth=3;"
        lines.append(
            f'        <mxCell id="{cell_id}" value="" style="{macro_edge_style}" edge="1" parent="1" source="{source_id}" target="{target_id}">'
        )
        lines.append('          <mxGeometry relative="1" as="geometry" />')
        lines.append('        </mxCell>')
        cell_id += 1

    lines.append('      </root>')
    lines.append('    </mxGraphModel>')
    lines.append('  </diagram>')
    lines.append('</mxfile>')

    return "\n".join(lines)


def validate_file(file_path: Path) -> Tuple[bool, List[str], SipocModel]:
    """Carga y valida un archivo Markdown o JSON."""
    if not file_path.exists():
        return False, [f"El archivo especificado no existe: {file_path}"], SipocModel()

    content = file_path.read_text(encoding="utf-8")
    if file_path.suffix.lower() == ".json":
        model = parse_json_sipoc(content)
    else:
        model = parse_markdown_sipoc(content)

    errors = validate_sipoc_data(model)
    return len(errors) == 0, errors, model


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validador y Generador de Matriz SIPOC con exportación a diagramStudio (Mermaid y Draw.io)."
    )
    parser.add_argument("file", nargs="?", help="Ruta al archivo Markdown (sipoc.md) o JSON a validar.")
    parser.add_argument("--test-steps", type=int, help="Prueba la regla de pasos de proceso directamente con un número.")
    parser.add_argument("--export-mermaid", action="store_true", help="Genera y muestra el bloque Mermaid de diagramStudio.")
    parser.add_argument("--export-drawio", nargs="?", const="", help="Exporta la matriz SIPOC a archivo XML Draw.io (.drawio).")
    parser.add_argument("--json", action="store_true", help="Vuelca el modelo extraído en formato JSON estructurado.")

    args = parser.parse_args()

    if args.test_steps is not None:
        steps = args.test_steps
        if MIN_PROCESS_STEPS <= steps <= MAX_PROCESS_STEPS:
            print(f"OK: {steps} macroetapas está dentro del rango canónico ({MIN_PROCESS_STEPS} a {MAX_PROCESS_STEPS}).")
            sys.exit(0)
        else:
            print(
                f"ERROR: {steps} macroetapas fuera de rango. Debe tener entre {MIN_PROCESS_STEPS} y {MAX_PROCESS_STEPS} "
                f"(actual: {steps})."
            )
            sys.exit(1)

    if not args.file:
        parser.print_help()
        sys.exit(1)

    path = Path(args.file)
    success, errors, model = validate_file(path)

    if args.json:
        print(json.dumps(model.to_dict(), indent=2, ensure_ascii=False))

    if args.export_mermaid:
        mermaid_code = generate_mermaid_diagram(model)
        print("\n--- Diagrama Mermaid para diagramStudio ---\n")
        print(mermaid_code)

    if args.export_drawio is not None:
        drawio_xml = generate_drawio_diagram(model)
        target_path = Path(args.export_drawio) if args.export_drawio else path.with_suffix(".drawio")
        target_path.write_text(drawio_xml, encoding="utf-8")
        print(f"Diagrama Draw.io exportado exitosamente en: {target_path}")

    if success:
        print(
            f"EXITO: Matriz SIPOC '{model.process_name or path.name}' validada con éxito.\n"
            f"- Proveedores (S): {len(model.suppliers)}\n"
            f"- Entradas (I): {len(model.inputs)} (todas con especificaciones técnicas)\n"
            f"- Macroproceso (P): {len(model.process_steps)} pasos (conforme al rango 4-7)\n"
            f"- Salidas (O): {len(model.outputs)} (todas con especificaciones de calidad)\n"
            f"- Clientes (C): {len(model.customers)}\n"
            f"- Fronteras delimitadas: Inicio = '{model.start_boundary}', Fin = '{model.end_boundary}'"
        )
        sys.exit(0)
    else:
        print(f"FALLO DE VALIDACION SIPOC ({len(errors)} error(es) detectado(s)):", file=sys.stderr)
        for err in errors:
            print(f"  [X] {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
