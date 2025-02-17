from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Data of 100 imaginary students
students = [
    {"name": "vZf8IgLu", "marks": 61}, {"name": "v7", "marks": 66}, {"name": "Py6bLR", "marks": 7},
    {"name": "n", "marks": 75}, {"name": "Wan", "marks": 19}, {"name": "1h", "marks": 58},
    {"name": "FjM5ICQ", "marks": 46}, {"name": "yWL1", "marks": 8}, {"name": "Y", "marks": 25},
    {"name": "E", "marks": 64}, {"name": "MZ", "marks": 36}, {"name": "LtrB9z", "marks": 69},
    {"name": "Zj", "marks": 2}, {"name": "TS60SCBJ", "marks": 91}, {"name": "bhizIcO", "marks": 35},
    {"name": "04xoJ7Rm", "marks": 42}, {"name": "7J48V", "marks": 20}, {"name": "6Iy", "marks": 79},
    {"name": "P", "marks": 57}, {"name": "d1YoJ1NJ", "marks": 39}, {"name": "EbJK", "marks": 57},
    {"name": "XVGb", "marks": 64}, {"name": "cAw", "marks": 38}, {"name": "8Y5", "marks": 35},
    {"name": "1xn6EfS0IY", "marks": 7}, {"name": "Xjwo3w81H", "marks": 72}, {"name": "HfAUVMgR6", "marks": 60},
    {"name": "gfHkAY", "marks": 39}, {"name": "piJd8", "marks": 69}, {"name": "MT", "marks": 36},
    {"name": "gvKQ", "marks": 0}, {"name": "UPTHZ3P2Ri", "marks": 64}, {"name": "Fw7cn6", "marks": 7},
    {"name": "4HSUM5LWf", "marks": 42}, {"name": "d7", "marks": 46}, {"name": "yRGt2bn", "marks": 26},
    {"name": "GypfKkT7YB", "marks": 17}, {"name": "YUDZ", "marks": 8}, {"name": "v3bF3POd", "marks": 71},
    {"name": "39cD", "marks": 39}, {"name": "Ev5CcPwGNV", "marks": 51}, {"name": "MBcH", "marks": 53},
    {"name": "aoMPvaGHT", "marks": 86}, {"name": "eOIo2fF1p", "marks": 84}, {"name": "IxCGt8eDPx", "marks": 48},
    {"name": "WU3QTiXx", "marks": 13}, {"name": "2arVRD", "marks": 92}, {"name": "sMb", "marks": 23},
    {"name": "TW8UmDOba7", "marks": 58}, {"name": "Z38TFUrqSX", "marks": 18}, {"name": "qLeN8bk", "marks": 13},
    {"name": "Vq", "marks": 36}, {"name": "dhYxvS8Ibo", "marks": 84}, {"name": "YTx", "marks": 49},
    {"name": "mpO6gVI3k9", "marks": 51}, {"name": "vUfxIrM", "marks": 87}, {"name": "3QuwxxEdG", "marks": 0},
    {"name": "XPL8zBIXj", "marks": 88}, {"name": "EtkQxAKtb", "marks": 2}, {"name": "dsKlyO", "marks": 7},
    {"name": "lfa7toaeiI", "marks": 5}, {"name": "MYg", "marks": 51}, {"name": "uYeWzjHiMj", "marks": 3},
    {"name": "717PgGv", "marks": 8}, {"name": "K1", "marks": 64}, {"name": "8PxiiuHU6", "marks": 84},
    {"name": "5l7v5G1", "marks": 61}, {"name": "NqTvsuHl", "marks": 78}, {"name": "ox", "marks": 99},
    {"name": "EYOKcCjVN", "marks": 29}, {"name": "QG8CNZNREA", "marks": 16}, {"name": "piO9j46Ss", "marks": 22},
    {"name": "lX0ytIbq", "marks": 66}, {"name": "ZoRSy", "marks": 54}, {"name": "ueoYeLgb", "marks": 34},
    {"name": "ciee9ln", "marks": 28}, {"name": "sT7t80d", "marks": 70}, {"name": "zvdwYK1", "marks": 2},
    {"name": "VBjoOXd7", "marks": 14}, {"name": "YU", "marks": 50}, {"name": "dCLB2Zo", "marks": 85},
    {"name": "qQqppP2", "marks": 82}, {"name": "b4OD", "marks": 9}, {"name": "ExY", "marks": 12},
    {"name": "BEM", "marks": 66}, {"name": "c8W", "marks": 57}, {"name": "jL1Jhw", "marks": 94},
    {"name": "GMZiXt", "marks": 69}, {"name": "BaM", "marks": 77}, {"name": "dwf9", "marks": 92},
    {"name": "SH", "marks": 98}, {"name": "55Dg1", "marks": 33}, {"name": "g0f", "marks": 35},
    {"name": "Ki2RO59", "marks": 33}, {"name": "5Tih", "marks": 20}, {"name": "hbWc1", "marks": 98},
    {"name": "azO6", "marks": 64}, {"name": "ef", "marks": 33}, {"name": "ZmK5a", "marks": 14},
    {"name": "g5LQ8", "marks": 44}
]

# API endpoint
@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get the 'name' query parameters
    marks = [next((student['marks'] for student in students if student['name'] == name), None) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
