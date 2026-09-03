#!/usr/bin/env python3
"""
Script utilitario de extracción de tokens para DESIGN.md.
Escanea un directorio de código fuente buscando configuraciones de Tailwind,
variables CSS y definiciones de color para sintetizar un borrador de DESIGN.md.
"""

import sys
import os
import re
import json

def find_colors_in_file(filepath):
    colors = set()
    hex_pattern = re.compile(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})')
    var_pattern = re.compile(r'--([a-zA-Z0-9_-]+):\s*(#[A-Fa-f0-9]{3,6}|rgba?\([^)]+\)|oklch\([^)]+\))')
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for match in hex_pattern.findall(content):
                colors.add(f"#{match}".upper())
    except Exception:
        pass
    return colors

def scan_project(root_dir):
    print(f"Escaneando proyecto en: {root_dir}...")
    found_colors = set()
    found_fonts = set()
    
    extensions = {'.js', '.jsx', '.ts', '.tsx', '.css', '.scss', '.json'}
    ignore_dirs = {'node_modules', '.git', 'dist', 'build', '.next'}
    
    tailwind_config = None
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for f in filenames:
            ext = os.path.splitext(f)[1]
            if f.startswith('tailwind.config'):
                tailwind_config = os.path.join(dirpath, f)
            if ext in extensions:
                p = os.path.join(dirpath, f)
                found_colors.update(find_colors_in_file(p))

    print(f"Se identificaron {len(found_colors)} valores de color únicos en el código.")
    if tailwind_config:
        print(f"Configuración de Tailwind detectada en: {tailwind_config}")
        
    return found_colors

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    scan_project(target)
