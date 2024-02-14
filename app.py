from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    ip = request.form['ip']
    scan_type = request.form['scan_type']
    try:
        if scan_type == 'nmap':
            output_bytes = subprocess.check_output(['nmap', ip])  # Example command, replace with actual command
        elif scan_type == 'nikto':
            output_bytes = subprocess.check_output(['nikto', '-h', ip])  # Example command, replace with actual command
        else:
            output_bytes = b"Invalid scan type selected"

        output = output_bytes.decode('utf-8').replace('\n', '<br>')
        return render_template('scan.html', output=output)
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
