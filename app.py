from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def two_number_sum(array, target_sum):
    nums = {}
    steps = []

    for num in array:
        steps.append(f"Checking {num}")
        potential_match = target_sum - num
        if potential_match in nums:
            steps.append(f"Found a match: {potential_match} and {num}")
            return {"result": [potential_match, num], "steps": steps}
        else:
            steps.append(f"Adding {num} to the checked numbers")
            nums[num] = True

    return {"result": "No pair found", "steps": steps}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    array = list(map(int, data['array'].split(',')))
    target_sum = int(data['target_sum'])
    output = two_number_sum(array, target_sum)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
