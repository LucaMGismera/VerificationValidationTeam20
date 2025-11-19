# BooKit

Project created according to the requirements prepared by team 11.

## Instrucciones para generar reportes de coverage
0. Identificamos que estamos en la iteración X
1. Accedemos a src/tests
2. Ejecutamos coverage run test_cases_itX.py, donde X es el conjunto de test cases de la iteración X en la que estamos
3. (Podemos si queremos ver una preview del coverage con "coverage report").
4. Ejecutamos: "coverage html"
5. Se generará un archivo en la misma carpeta llamada htmlcov
6. Renombrar la carpeta a "report_tc_itX" donde X es el número de iteración en la que estamos
7. Analizamos la situación en la que estamos según las instrucciones del ejercicio

## Instalación (modo editable)

```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\\Scripts\\activate
pip install -e .
python -m pip install coverage
```

# CÓDIGO FINALIZADO
Se podrían incluir comentarios en el código, pero está todo finalizado correctamente.

Se obtiene el 100% de coverage en la segunda iteración.
