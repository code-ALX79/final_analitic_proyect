#!/bin/bash

# Crea la estructura profesional de carpetas
mkdir -p data/raw data/processed notebooks scripts tests outputs docs

# Mueve los archivos según su tipo
mv *.csv data/raw/ 2>/dev/null
mv *.ipynb notebooks/ 2>/dev/null
mv *.py scripts/ 2>/dev/null

# Mensaje final
echo "✅ Estructura de carpetas creada y archivos reubicados correctamente."

