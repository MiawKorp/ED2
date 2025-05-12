from flask import request, render_template

def index():
    results = None
    set_a = set_b = set()

    if request.method == "POST":
        # Obtener los conjuntos desde el formulario
        raw_a = request.form.get("set_a", "")
        raw_b = request.form.get("set_b", "")

        # Convertir las entradas a conjuntos de enteros
        set_a = set(map(int, raw_a.split(","))) if raw_a else set()
        set_b = set(map(int, raw_b.split(","))) if raw_b else set()

        # Realizar las operaciones entre los conjuntos y ordenar los resultados
        results = {
            "union": sorted(set_a | set_b),
            "intersection": sorted(set_a & set_b),
            "diff_a_b": sorted(set_a - set_b),
            "diff_b_a": sorted(set_b - set_a),
            "sym_diff": sorted(set_a ^ set_b),
            "is_subset": "Verdadero" if set_a.issubset(set_b) else "Falso",
            "is_superset": "Verdadero" if set_a.issuperset(set_b) else "Falso",
        }

    return render_template("index.html", results=results)