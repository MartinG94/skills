#!/usr/bin/env python3
"""
build_cv.py - Compilador automatizado y renderizador de previsualización para cvOptimizer.

Flujo:
1. Verifica prerequisitos de entorno (tectonic / pdflatex y pymupdf). Auto-instala pymupdf si falta.
2. Compila el documento LaTeX principal (main.tex).
3. Exporta el PDF compilado a la misma altura que la carpeta del proyecto con el nombre:
   <Apellido Nombre>CV_<Puesto>.pdf
4. Renderiza la primera página como preview.png en alta resolución (300 DPI) para visualización en chat.
"""

import sys
import os
import shutil
import subprocess
import argparse
from pathlib import Path

def ensure_dependencies():
    """Verifica y auto-instala dependencias de Python (pymupdf)."""
    try:
        import pymupdf
    except ImportError:
        try:
            import fitz
        except ImportError:
            print("[INFO] pymupdf no detectado. Instalando automáticamente mediante pip...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf", "--quiet"])
            print("[OK] pymupdf instalado correctamente.")

def detect_compiler(preferred_engine=None):
    """Detecta si tectonic o pdflatex están disponibles en el PATH o en rutas locales."""
    if preferred_engine:
        path = shutil.which(preferred_engine)
        if path:
            return preferred_engine, path

    # Priorizar tectonic por ser autocontenido y descargar paquetes al vuelo
    tectonic_path = shutil.which("tectonic")
    if tectonic_path:
        return "tectonic", tectonic_path

    pdflatex_path = shutil.which("pdflatex")
    if pdflatex_path:
        return "pdflatex", pdflatex_path

    # Búsqueda en rutas conocidas de Windows
    local_bin = Path(os.path.expanduser("~")) / ".local" / "bin"
    if (local_bin / "tectonic.exe").exists():
        return "tectonic", str(local_bin / "tectonic.exe")
    if (local_bin / "pdflatex.cmd").exists():
        return "pdflatex", str(local_bin / "pdflatex.cmd")

    return None, None

def render_preview(pdf_path: Path, output_image_path: Path, dpi: int = 200):
    """Renderiza la primera página del PDF como PNG en alta fidelidad."""
    try:
        import pymupdf
        doc = pymupdf.open(pdf_path)
    except Exception:
        import fitz
        doc = fitz.open(pdf_path)

    if len(doc) < 1:
        print("[WARN] El PDF generado no contiene páginas para previsualizar.")
        return False

    page = doc[0]
    zoom = dpi / 72.0
    mat = page.get_display_matrix() if hasattr(page, "get_display_matrix") else None
    # Matriz de escalado para alta resolución
    import fitz as fz
    matrix = fz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix, alpha=False)
    pix.save(str(output_image_path))
    doc.close()
    return True

def compile_latex(project_dir: Path, engine: str, compiler_path: str):
    """Compila main.tex dentro de project_dir usando el motor seleccionado."""
    main_tex = project_dir / "main.tex"
    if not main_tex.exists():
        raise FileNotFoundError(f"No se encontró main.tex en {project_dir}")

    print(f"[INFO] Compilando con {engine} ({compiler_path})...")

    if engine == "tectonic":
        cmd = [compiler_path, str(main_tex)]
        res = subprocess.run(cmd, cwd=str(project_dir), capture_output=True, text=True)
        if res.returncode != 0:
            print("[ERROR] Falló la compilación con Tectonic:")
            print(res.stderr or res.stdout)
            return False
    elif engine == "pdflatex":
        # Ejecutar pdflatex dos veces para resolver hipervínculos y referencias cruzadas
        for i in range(2):
            cmd = [compiler_path, "-interaction=nonstopmode", "main.tex"]
            res = subprocess.run(cmd, cwd=str(project_dir), capture_output=True, text=True)
            if res.returncode != 0:
                print(f"[ERROR] Falló la pasada {i+1} de pdflatex:")
                print(res.stdout[-1500:])
                return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Compilador y exportador de CV para cvOptimizer")
    parser.add_argument("--project-dir", required=True, help="Ruta a la carpeta del proyecto LaTeX")
    parser.add_argument("--candidate-name", default="Diego Sanchez", help="Nombre del postulante (ej. Diego Sanchez)")
    parser.add_argument("--target-role", default="CV", help="Puesto postulado (ej. Analista_IT)")
    parser.add_argument("--company", default="", help="Empresa o institución postulada (opcional)")
    parser.add_argument("--engine", default=None, choices=["tectonic", "pdflatex"], help="Motor de compilación preferido")
    parser.add_argument("--dpi", type=int, default=200, help="DPI para previsualización PNG")

    args = parser.parse_args()
    project_dir = Path(args.project_dir).resolve()

    if not project_dir.exists():
        print(f"[ERROR] La carpeta de proyecto {project_dir} no existe.")
        sys.exit(1)

    ensure_dependencies()

    engine, compiler_path = detect_compiler(args.engine)
    if not engine:
        print("[ERROR] No se encontró ningún compilador TeX (tectonic o pdflatex) en el sistema.")
        print("[TIP] Puedes instalar Tectonic con: winget install Tectonic.Tectonic o cargo install tectonic")
        sys.exit(1)

    success = compile_latex(project_dir, engine, compiler_path)
    if not success:
        sys.exit(1)

    # Identificar el PDF generado en el directorio del proyecto
    compiled_pdf = project_dir / "main.pdf"
    if not compiled_pdf.exists():
        print(f"[ERROR] No se encontró main.pdf generado en {project_dir}")
        sys.exit(1)

    # Construir nombre estandarizado: <Apellido Nombre>CV_<Puesto>.pdf
    # Sanitizar nombres para archivos válidos
    clean_name = args.candidate_name.strip().replace(" ", "_")
    clean_role = args.target_role.strip().replace(" ", "_").replace("/", "_")
    if args.company:
        clean_company = args.company.strip().replace(" ", "_")
        pdf_filename = f"{clean_name}_CV_{clean_role}_{clean_company}.pdf"
    else:
        pdf_filename = f"{clean_name}_CV_{clean_role}.pdf"

    # Destino a la misma altura que la carpeta del proyecto (directorio padre)
    parent_dir = project_dir.parent
    final_pdf_path = parent_dir / pdf_filename

    shutil.copy2(compiled_pdf, final_pdf_path)
    print(f"[EXITO] PDF exportado a: {final_pdf_path}")

    # Renderizar previsualización PNG
    preview_img_project = project_dir / "preview.png"
    render_preview(final_pdf_path, preview_img_project, dpi=args.dpi)
    print(f"[EXITO] Previsualización renderizada en: {preview_img_project}")

if __name__ == "__main__":
    main()
