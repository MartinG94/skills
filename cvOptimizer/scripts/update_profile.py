#!/usr/bin/env python3
"""
update_profile.py - Gestor de actualización incremental e iterativa de profile_data.json para cvOptimizer.

Permite fusionar nuevos datos descubiertos durante entrevistas o postulaciones
sin perder información preexistente en la base de datos de perfil del usuario.
"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

def load_profile(profile_path: Path) -> dict:
    if profile_path.exists():
        with open(profile_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_profile(profile_path: Path, data: dict):
    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[OK] profile_data.json actualizado con éxito en: {profile_path}")

def merge_skills(existing_skills: dict, new_skills: dict) -> dict:
    result = dict(existing_skills)
    for category in ["hard", "soft", "tools"]:
        cur_list = result.get(category, [])
        new_list = new_skills.get(category, [])
        combined = list(dict.fromkeys(cur_list + new_list))
        result[category] = combined

    # Para idiomas, comparar por el nombre del idioma
    cur_langs = {item["language"].lower(): item for item in result.get("languages", [])}
    for new_l in new_skills.get("languages", []):
        cur_langs[new_l["language"].lower()] = new_l
    result["languages"] = list(cur_langs.values())
    return result

def merge_list_by_key(existing_list: list, new_list: list, key: str) -> list:
    """Fusiona listas de diccionarios usando una clave primaria o compuesta."""
    lookup = {str(item.get(key, "")).lower(): item for item in existing_list}
    for item in new_list:
        lookup[str(item.get(key, "")).lower()] = item
    return list(lookup.values())

def incremental_update(profile_path: Path, update_payload: dict):
    profile = load_profile(profile_path)
    if not profile:
        # Cargar template inicial si el archivo no existía
        template_path = Path(__file__).resolve().parent.parent / "templates" / "profile_data_template.json"
        if template_path.exists():
            with open(template_path, "r", encoding="utf-8") as f:
                profile = json.load(f)
        else:
            profile = {
                "personal": {},
                "summary": "",
                "experience": [],
                "education": [],
                "skills": {"hard": [], "soft": [], "tools": [], "languages": []},
                "certifications": [],
                "activities": [],
                "projects": [],
                "metadata": {"interviewCount": 0, "targetRoles": []}
            }

    # 1. Actualizar datos personales si se proporcionan
    if "personal" in update_payload:
        profile.setdefault("personal", {}).update(update_payload["personal"])

    # 2. Resumen profesional
    if "summary" in update_payload and update_payload["summary"]:
        profile["summary"] = update_payload["summary"]

    # 3. Habilidades (fusión deduplicada)
    if "skills" in update_payload:
        profile["skills"] = merge_skills(profile.get("skills", {}), update_payload["skills"])

    # 4. Experiencia (fusión por empresa + rol)
    if "experience" in update_payload:
        cur_exp = profile.get("experience", [])
        for new_item in update_payload["experience"]:
            match_idx = next((i for i, x in enumerate(cur_exp) if x.get("company", "").lower() == new_item.get("company", "").lower() and x.get("role", "").lower() == new_item.get("role", "").lower()), None)
            if match_idx is not None:
                # Combinar highlights y métricas
                existing_highlights = cur_exp[match_idx].get("highlights", [])
                combined_hl = list(dict.fromkeys(existing_highlights + new_item.get("highlights", [])))
                cur_exp[match_idx]["highlights"] = combined_hl
                cur_metrics = cur_exp[match_idx].get("metrics", {})
                cur_metrics.update(new_item.get("metrics", {}))
                cur_exp[match_idx]["metrics"] = cur_metrics
            else:
                cur_exp.append(new_item)
        profile["experience"] = cur_exp

    # 5. Educación (fusión por degree)
    if "education" in update_payload:
        profile["education"] = merge_list_by_key(profile.get("education", []), update_payload["education"], "degree")

    # 6. Certificaciones (fusión por name)
    if "certifications" in update_payload:
        profile["certifications"] = merge_list_by_key(profile.get("certifications", []), update_payload["certifications"], "name")

    # 7. Actividades (fusión por role + organization)
    if "activities" in update_payload:
        profile["activities"] = merge_list_by_key(profile.get("activities", []), update_payload["activities"], "organization")

    # 8. Proyectos (fusión por name)
    if "projects" in update_payload:
        profile["projects"] = merge_list_by_key(profile.get("projects", []), update_payload["projects"], "name")

    # Metadatos de gobernanza
    meta = profile.setdefault("metadata", {})
    meta["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")
    meta["interviewCount"] = meta.get("interviewCount", 0) + 1

    if "targetRole" in update_payload:
        target_role = update_payload["targetRole"]
        roles = meta.get("targetRoles", [])
        if target_role not in roles:
            roles.append(target_role)
        meta["targetRoles"] = roles

    save_profile(profile_path, profile)

def main():
    parser = argparse.ArgumentParser(description="Actualizador incremental para profile_data.json")
    parser.add_argument("--profile", required=True, help="Ruta al archivo profile_data.json")
    parser.add_argument("--update-json", help="Cadena JSON o ruta a un archivo JSON con los datos a fusionar")
    parser.add_argument("--add-skill-hard", nargs="+", help="Agregar una o más hard skills")
    parser.add_argument("--add-skill-soft", nargs="+", help="Agregar una o más soft skills")
    parser.add_argument("--add-tool", nargs="+", help="Agregar una o más herramientas")
    parser.add_argument("--target-role", help="Puesto objetivo de la entrevista actual")

    args = parser.parse_args()
    profile_path = Path(args.profile).resolve()

    payload = {}
    if args.update_json:
        p = Path(args.update_json)
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                payload = json.load(f)
        else:
            payload = json.loads(args.update_json)

    if args.add_skill_hard or args.add_skill_soft or args.add_tool:
        skills = payload.setdefault("skills", {})
        if args.add_skill_hard:
            skills.setdefault("hard", []).extend(args.add_skill_hard)
        if args.add_skill_soft:
            skills.setdefault("soft", []).extend(args.add_skill_soft)
        if args.add_tool:
            skills.setdefault("tools", []).extend(args.add_tool)

    if args.target_role:
        payload["targetRole"] = args.target_role

    incremental_update(profile_path, payload)

if __name__ == "__main__":
    main()
