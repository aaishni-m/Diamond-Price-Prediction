from flask import Flask, render_template, request
import model as m

app = Flask(__name__)

# Updated features to match the trained model
features = [
    'cut', 'color', 'clarity', 'carat_weight', 'cut_quality', 
    'lab', 'symmetry', 'polish', 'eye_clean', 'culet_size', 
    'depth_percent', 'table_percent', 'meas_length', 'meas_width', 
    'meas_depth'
]

@app.route("/", methods=['GET', 'POST'])
def home():
    sales_prediction = None
    error_message = None

    if request.method == 'POST':
        try:
            # Gather input values from form
            input_list = []
            for feature in features:
                value = request.form.get(feature, '')
                try:
                    input_list.append(float(value))  # Convert numeric inputs
                except ValueError:
                    input_list.append(value)  # Keep string inputs

            # Make prediction using model
            sales_prediction = m.predict_pipe(input_list)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html', sale=sales_prediction, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
