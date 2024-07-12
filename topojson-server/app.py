from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

@app.route('/topojson/<filename>')
def get_topojson(filename):
    try:
        topojson_dir = os.path.join(app.root_path, 'static')
        app.logger.info(f'Requested file: {filename}')
        app.logger.info(f'Serving from directory: {topojson_dir}')
        return send_from_directory(topojson_dir, filename)

    except Exception as e:
        app.logger.error(f'Error serving file: {e}')
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context=context, debug=True)
