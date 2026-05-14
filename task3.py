from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Violation weights
VIOLATION_WEIGHTS = {
    "phone": 1.5,
    "tab_switch": 1.0,
    "multiple_faces": 2.0
}


# Risk score calculation
def calculate_risk_score(violations):

    # No violations
    if not violations:
        return 0, "safe"

    weighted_sum = 0
    total_weight = 0

    for violation in violations:

        v_type = violation["type"]
        severity = violation["severity"]

        # Get weight
        weight = VIOLATION_WEIGHTS.get(v_type, 1.0)

        weighted_sum += severity * weight
        total_weight += weight

    risk_score = weighted_sum / total_weight

    # Status logic
    if risk_score == 0:
        status = "safe"
    elif risk_score <= 0.5:
        status = "warning"
    else:
        status = "flagged"

    return round(risk_score, 2), status


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# API endpoint
@app.route('/calculate_risk', methods=['POST'])
def calculate_risk():

    data = request.get_json()

    violations = data.get("violations", [])

    risk_score, status = calculate_risk_score(violations)

    return jsonify({
        "risk_score": risk_score,
        "status": status
    })


if __name__ == '__main__':
    app.run(debug=True)