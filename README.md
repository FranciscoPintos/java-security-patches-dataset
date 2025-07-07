# Java Security Patches Dataset

Este repositorio contiene un dataset curado de vulnerabilidades en proyectos Java y los commits que las corrigen, con el objetivo de servir como base para un sistema de sugerencia automática de parches de seguridad.

## Estructura del repositorio

- `data/`  
  Carpeta donde se irán almacenando los CSV o JSON generados.
- `scripts/`  
  Scripts en Python para extracción y limpieza de datos.
- `notebooks/`  
  Jupyter notebooks de exploración y validación preliminar.
- `LICENSE`  
  Licencia del repositorio.
- `README.md`  
  Documentación y guía de uso.

## Cómo empezar

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/FranciscoPintos/java-security-patches-dataset.git
   cd java-security-patches-dataset



4. Probar localmente
Activar tu entorno virtual y instala dependencias:
```bash
  source venv/bin/activate
  pip install -r requirements.txt 
```
Ejecuta el script:
```bash
python scripts/extract_commits.py
Verifica que se genere data/dataset_inicial.csv y que contenga entradas de commits.

