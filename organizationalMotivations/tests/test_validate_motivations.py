#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para validate_motivations.py (organizationalMotivations skill).
"""

import os
import sys
import tempfile
import unittest

# Añadir directorio de scripts al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))
from validate_motivations import validate_motivations_file

EXAMPLE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "examples", "motivaciones_ejemplo.md"))

class TestValidateMotivations(unittest.TestCase):

    def test_canonical_example_is_valid(self):
        """Verifica que el ejemplo canónico de cátedra supere todas las validaciones."""
        self.assertTrue(os.path.exists(EXAMPLE_PATH), f"No se encontró el ejemplo en {EXAMPLE_PATH}")
        res = validate_motivations_file(EXAMPLE_PATH)
        self.assertTrue(res["valid"], f"El ejemplo falló la validación: {res['errors']}")
        self.assertEqual(res["stats"]["sections_found"], 5)
        self.assertGreaterEqual(res["stats"]["trends_count"], 3)
        self.assertGreaterEqual(res["stats"]["customer_needs_count"], 2)
        self.assertGreaterEqual(res["stats"]["drivers_count"], 2)
        self.assertTrue(res["stats"]["sdl_alignment_found"])

    def test_nonexistent_file(self):
        """Verifica el manejo adecuado de archivos no existentes."""
        res = validate_motivations_file("ruta/inexistente/motivaciones.md")
        self.assertFalse(res["valid"])
        self.assertTrue(any("no existe" in err for err in res["errors"]))

    def test_missing_sections(self):
        """Verifica que un archivo incompleto reporte errores de secciones faltantes."""
        incomplete_content = """# Matriz de Motivaciones
## 1. Identificación Institucional
Misión y Visión de la empresa.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(incomplete_content)
            temp_path = f.name

        try:
            res = validate_motivations_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertLess(res["stats"]["sections_found"], 5)
            self.assertTrue(any("Sección obligatoria" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_missing_sdl_perspective(self):
        """Verifica error si falta la perspectiva SDL / co-creación de valor."""
        content_without_sdl = """# Matriz de Motivaciones
## 1. Identificación Institucional
Misión y Visión. SMART. Cliente y propuesta de valor.
## 2. Matriz de Tendencias del Entorno SDLI
| ID | Macro-Sector | Sub-Tendencia | Dimensión | Manifestación | Impacto |
|---|---|---|---|---|---|
| `TND-01` | Digitalización | Automatización | Tecnología | Uso de computadoras | Alto |
| `TND-02` | Cultura de la Inmediatez | 24/7 | Sociedad | Atención rápida | Alto |
| `TND-03` | Conciencia Medio Ambiental | Eco | Economía | Menor consumo | Medio |
## 3. Matriz de Tendencias del Cliente
| ID | Tendencia | Expectativa | Fricción | Oportunidad |
|---|---|---|---|---|
| `CLI-01` | Rapidez | Atención | Espera | Mejorar |
| `CLI-02` | Online | Web | Papel | Digital |
## 4. Impulsores y Demandas de Mejora
| ID | Impulsor | Justificación | Procesos Afectados | Trazabilidad |
|---|---|---|---|---|
| `DRV-01` | Eficiencia | Bajar costos | Todos | Etapa 2 |
| `DRV-02` | Digitalización | Modernizar | Operaciones | Etapa 3 |
## 5. Síntesis y Conclusiones de Encuadre
Conclusiones generales.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(content_without_sdl)
            temp_path = f.name

        try:
            res = validate_motivations_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("Lógica Dominante del Servicio" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_insufficient_sdli_macro_sectors(self):
        """Verifica error si se analizan menos de 3 macro-sectores del Mapa SDLI."""
        content_few_sectors = """# Matriz de Motivaciones
## 1. Identificación Institucional
Misión y Visión. SMART. Cliente y propuesta de valor.
## 2. Matriz de Tendencias del Entorno SDLI
Enfoque de co-creación de valor y Lógica Dominante del Servicio (SDL).
| ID | Macro-Sector | Sub-Tendencia | Dimensión | Manifestación | Perspectiva SDL | Impacto |
|---|---|---|---|---|---|---|
| `TND-01` | Digitalización | Automatización | Tecnología | Automatizar | Co-creación | Alto |
| `TND-02` | Digitalización | Soluciones abiertas | Tecnología | APIs abiertas | Co-creación | Alto |
| `TND-03` | Digitalización | Transformación | Tecnología | Digital | Co-creación | Alto |
## 3. Matriz de Tendencias del Cliente
| ID | Tendencia | Expectativa | Fricción | Oportunidad |
|---|---|---|---|---|
| `CLI-01` | Rapidez | Atención | Espera | Co-creación |
| `CLI-02` | Online | Web | Papel | Co-creación |
## 4. Impulsores y Demandas de Mejora
| ID | Impulsor | Justificación | Procesos Afectados | Trazabilidad |
|---|---|---|---|---|
| `DRV-01` | Eficiencia | Bajar costos | Todos | Etapa 2 |
| `DRV-02` | Digitalización | Modernizar | Operaciones | Etapa 3 |
## 5. Síntesis y Conclusiones de Encuadre
Conclusiones generales.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(content_few_sectors)
            temp_path = f.name

        try:
            res = validate_motivations_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("al menos 3 macro-sectores" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == "__main__":
    unittest.main()
