from flask import Flask, request, jsonify

app = Flask(__name__)

# Volume Dictionary
VOLUME = {"ml": 1, "l": 1000, "tsp": 4.92892, "tbsp": 14.7868, "fl_oz": 29.5735, "cup": 236.588}


@app.route("/convert")
def convert():
    raw_value = request.args.get("value")
    from_unit = request.args.get("from_unit")
    to_unit = request.args.get("to_unit")
    
    if raw_value is None or from_unit is None or to_unit is None:
        return jsonify({
            "error": "Parameters 'value', 'from_unit', and 'to_unit' are required"
        }), 400
    
    try:
        value = float(raw_value)
    except ValueError:
        return jsonify({
            "error": "Parameter 'value' must be numeric"
        }), 400

    if from_unit == "F" and to_unit == "C":
        result = (value - 32) * 5 / 9
    elif from_unit == "C" and to_unit == "F":
        result = value * 9 / 5 + 32
    elif from_unit in VOLUME and to_unit in VOLUME:
        result = value * VOLUME[from_unit] / VOLUME[to_unit]
    else:
        return jsonify({"error": "Invalid unit conversion requested"}), 400

    return jsonify({
        "original_value": value,
        "original_unit": from_unit,
        "converted_value": round(result, 2),
        "converted_unit": to_unit,
    })


app.run(port=5001)
