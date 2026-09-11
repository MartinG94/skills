#!/usr/bin/env python3
"""Pruebas unitarias para el validador y generador de matriz SIPOC (validate_sipoc.py)."""

import json
import sys
import unittest
from pathlib import Path

# Asegurar importación determinista independiente del cwd
sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_sipoc import (
    SipocModel,
    generate_mermaid_diagram,
    parse_json_sipoc,
    parse_markdown_sipoc,
    validate_file,
    validate_sipoc_data,
)


class TestSipocValidator(unittest.TestCase):
    """Batería de pruebas metodológicas y técnicas para la matriz SIPOC."""

    def setUp(self) -> None:
        self.valid_model = SipocModel()
        self.valid_model.process_name = "Despacho de Pedidos Refrigerados"
        self.valid_model.process_owner = "Gerencia de Logística"
        self.valid_model.start_boundary = "Recepción de orden autorizada"
        self.valid_model.end_boundary = "Entrega con remito firmado"
        self.valid_model.suppliers = [{"id": "S1", "name": "Proveedor A"}]
        self.valid_model.inputs = [
            {"id": "I1", "name": "Materia Prima", "supplier": "Proveedor A", "requirement": "Certificado ISO, temp 2-8C"}
        ]
        self.valid_model.process_steps = [
            {"id": "P1", "name": "Recepcionar insumos"},
            {"id": "P2", "name": "Almacenar en cámara"},
            {"id": "P3", "name": "Preparar pedido"},
            {"id": "P4", "name": "Empacar y rotular"},
            {"id": "P5", "name": "Despachar a transporte"},
        ]
        self.valid_model.outputs = [
            {"id": "O1", "name": "Pedido Conforme", "customer": "Cliente B", "requirement": "Entrega en 24h sin rotura"}
        ]
        self.valid_model.customers = [{"id": "C1", "name": "Cliente B"}]

    def test_valid_model_passes(self) -> None:
        """Verifica que un modelo con datos completos y 5 pasos sea 100% válido."""
        errors = validate_sipoc_data(self.valid_model)
        self.assertEqual(len(errors), 0, f"No se esperaban errores: {errors}")

    def test_process_steps_below_minimum(self) -> None:
        """Falla si el macroproceso tiene menos de 4 pasos (sub-delimitación)."""
        self.valid_model.process_steps = [
            {"id": "P1", "name": "Paso 1"},
            {"id": "P2", "name": "Paso 2"},
            {"id": "P3", "name": "Paso 3"},
        ]
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("3 etapas" in e and "menos de 4" in e for e in errors))

    def test_process_steps_above_maximum(self) -> None:
        """Falla si el macroproceso supera 7 pasos (sobre-especificación de tareas)."""
        self.valid_model.process_steps = [
            {"id": f"P{i}", "name": f"Paso {i}"} for i in range(1, 9)
        ]
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("8 etapas" in e and "más de 7" in e for e in errors))

    def test_process_steps_exact_boundaries(self) -> None:
        """Comprueba que exactamente 4 pasos y exactamente 7 pasos sean válidos."""
        self.valid_model.process_steps = [
            {"id": f"P{i}", "name": f"Paso {i}"} for i in range(1, 5)
        ]
        self.assertEqual(len(validate_sipoc_data(self.valid_model)), 0)

        self.valid_model.process_steps = [
            {"id": f"P{i}", "name": f"Paso {i}"} for i in range(1, 8)
        ]
        self.assertEqual(len(validate_sipoc_data(self.valid_model)), 0)

    def test_missing_input_technical_requirement(self) -> None:
        """Falla si una entrada no declara requisitos técnicos o especificación."""
        self.valid_model.inputs[0]["requirement"] = ""
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("Requisito técnico o especificación de calidad faltante" in e for e in errors))

        self.valid_model.inputs[0]["requirement"] = "[TBD]"
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("Requisito técnico o especificación de calidad faltante" in e for e in errors))

    def test_missing_output_technical_requirement(self) -> None:
        """Falla si una salida no declara especificaciones de calidad o SLA."""
        self.valid_model.outputs[0]["requirement"] = ""
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("Especificación de calidad o SLA faltante" in e for e in errors))

        self.valid_model.outputs[0]["requirement"] = "N/A"
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("Especificación de calidad o SLA faltante" in e for e in errors))

    def test_missing_boundary_definitions(self) -> None:
        """Falla si no se definen las fronteras de inicio o de fin."""
        self.valid_model.start_boundary = ""
        self.valid_model.end_boundary = ""
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("frontera de inicio" in e for e in errors))
        self.assertTrue(any("frontera de fin" in e for e in errors))

    def test_missing_core_dimensions(self) -> None:
        """Falla si falta alguna de las 5 dimensiones fundamentales."""
        self.valid_model.suppliers = []
        self.valid_model.customers = []
        errors = validate_sipoc_data(self.valid_model)
        self.assertTrue(any("Dimensión Proveedores (S) vacía" in e for e in errors))
        self.assertTrue(any("Dimensión Clientes (C) vacía" in e for e in errors))

    def test_mermaid_diagram_generation(self) -> None:
        """Genera diagrama Mermaid compatible con preset diagramStudio."""
        diagram = generate_mermaid_diagram(self.valid_model)
        self.assertIn("```mermaid", diagram)
        self.assertIn("flowchart LR", diagram)
        self.assertIn('subgraph S ["1. PROVEEDORES (Suppliers)"]', diagram)
        self.assertIn('subgraph I ["2. ENTRADAS (Inputs)"]', diagram)
        self.assertIn('subgraph P ["3. PROCESO (Process - 5 Macroetapas)"]', diagram)
        self.assertIn('subgraph O ["4. SALIDAS (Outputs)"]', diagram)
        self.assertIn('subgraph C ["5. CLIENTES (Customers)"]', diagram)
        self.assertIn("P1 --> P2 --> P3 --> P4 --> P5", diagram)
        self.assertIn("S ==> I", diagram)
        self.assertIn("I ==> P", diagram)
        self.assertIn("P ==> O", diagram)
        self.assertIn("O ==> C", diagram)
        self.assertIn("classDef sStyle", diagram)

    def test_parse_json_example(self) -> None:
        """Prueba la lectura y validación del archivo sipoc_example.json."""
        example_path = Path(__file__).resolve().parent.parent / "templates" / "sipoc_example.json"
        if example_path.exists():
            success, errors, model = validate_file(example_path)
            self.assertTrue(success, f"Errores en sipoc_example.json: {errors}")
            self.assertEqual(len(model.process_steps), 5)
            self.assertEqual(len(model.suppliers), 4)
            self.assertEqual(len(model.inputs), 4)
            self.assertEqual(len(model.outputs), 3)
            self.assertEqual(len(model.customers), 3)

    def test_parse_markdown_document(self) -> None:
        """Prueba el parser sobre un documento Markdown formal."""
        md_text = """# Matriz SIPOC: Elaboración y Despacho de Pedidos
- **Proceso u Operación:** Elaboración y Despacho de Pedidos
- **Dueño / Responsable:** Gerente de Operaciones
- **Disparador / Límite de Inicio:** Ingreso de orden de compra
- **Evento Terminal / Límite de Fin:** Confirmación de remito en cliente

## 2. Matriz SIPOC Principal
| Proveedores (S) | Entradas / Insumos (I) | Macroproceso (P - 4 a 7 Pasos) | Salidas / Entregables (O) | Clientes / Destinatarios (C) |
|---|---|---|---|---|
| S1: Depósito Central<br>S2: Clientes | I1: Pedido confirmado<br>I2: Mercadería | P1: Verificar disponibilidad<br>P2: Preparar bulto<br>P3: Empacar caja<br>P4: Generar remito<br>P5: Cargar camión | O1: Bulto despachado<br>O2: Remito firmado | C1: Cliente Final<br>C2: Transportista |

## 3. Especificaciones Técnicas y Requisitos de Calidad de Entradas
| ID | Entrada / Insumo | Proveedor (S) | Requisito Técnico / Criterio de Aceptación | Formato |
|---|---|---|---|---|
| I1 | Pedido confirmado | S2: Clientes | Orden válida con pago acreditado y SKU verificado | Digital |
| I2 | Mercadería | S1: Depósito | Lote conforme con vencimiento > 12 meses | Físico |

## 4. Especificaciones Técnicas y Requisitos de Calidad de Salidas
| ID | Salida / Entregable | Cliente Destinatario (C) | Especificación de Calidad / SLA | Criterio |
|---|---|---|---|---|
| O1 | Bulto despachado | C1: Cliente Final | Embalaje inviolable con cinta de seguridad | Conforme |
| O2 | Remito firmado | C2: Transportista | Documento impreso por triplicado con código de barras legible | Checksum |
"""
        model = parse_markdown_sipoc(md_text)
        errors = validate_sipoc_data(model)
        self.assertEqual(len(errors), 0, f"Errores al parsear Markdown: {errors}")
        self.assertEqual(len(model.process_steps), 5)
        self.assertEqual(model.inputs[0]["requirement"], "Orden válida con pago acreditado y SKU verificado")
        self.assertEqual(model.outputs[0]["requirement"], "Embalaje inviolable con cinta de seguridad")

    def test_parse_sipoc_template_file(self) -> None:
        """Prueba la validación directa del archivo templates/sipoc_template.md."""
        template_path = Path(__file__).resolve().parent.parent / "templates" / "sipoc_template.md"
        self.assertTrue(template_path.exists(), "sipoc_template.md debe existir")
        success, errors, model = validate_file(template_path)
        self.assertTrue(success, f"Errores en sipoc_template.md: {errors}")
        self.assertEqual(len(model.process_steps), 5)
        self.assertEqual(len(model.suppliers), 3)
        self.assertEqual(len(model.inputs), 3)
        self.assertEqual(len(model.outputs), 3)
        self.assertEqual(len(model.customers), 3)
        self.assertIn("Beneficiario principal directo", model.client_principal)
        self.assertIn("Propósito central", model.process_objective)
        self.assertIn("Leyes nacionales", model.regulatory_framework.get("external", ""))
        self.assertIn("Estatuto institucional", model.regulatory_framework.get("internal", ""))
        self.assertIn("corazón", model.value_created.lower())

    def test_catedra_fields_in_json_example(self) -> None:
        """Verifica que sipoc_example.json contenga y valide los campos de cátedra GMP."""
        example_path = Path(__file__).resolve().parent.parent / "templates" / "sipoc_example.json"
        success, errors, model = validate_file(example_path)
        self.assertTrue(success)
        self.assertEqual(model.client_principal, "Farmacias Hospitalarias y Centros de Salud")
        self.assertIn("ANMAT", model.regulatory_framework.get("external", ""))
        self.assertIn("estabilidad farmacológica", model.value_created.lower())


if __name__ == "__main__":
    unittest.main()
