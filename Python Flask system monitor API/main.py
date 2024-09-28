from flask import Flask, jsonify
import psutil
from flasgger import Swagger

try:
    import GPUtil
    gpu_available = True
except ImportError:
    gpu_available = False

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/system/cpu', methods=['GET'])
def cpu_usage():
    """
    Returns CPU usage
    ---
    responses:
      200:
        description: Current CPU usage percentage
        schema:
          type: object
          properties:
            cpu_percent:
              type: number
              description: CPU usage percentage
              example: 12.5
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    return jsonify({'cpu_percent': cpu_percent})


@app.route('/api/system/ram', methods=['GET'])
def ram_usage():
    """
    Returns RAM usage
    ---
    responses:
      200:
        description: RAM usage statistics
        schema:
          type: object
          properties:
            total:
              type: number
            available:
              type: number
            percent:
              type: number
    """
    memory = psutil.virtual_memory()
    ram_data = {
        'total': memory.total,
        'available': memory.available,
        'percent': memory.percent
    }
    return jsonify(ram_data)


@app.route('/api/system/disk', methods=['GET'])
def disk_usage():
    """
    Returns Disk usage
    ---
    responses:
      200:
        description: Disk usage statistics
        schema:
          type: object
          properties:
            total:
              type: number
            used:
              type: number
            free:
              type: number
            percent:
              type: number
    """
    disk = psutil.disk_usage('/')
    disk_data = {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }
    return jsonify(disk_data)


@app.route('/api/system/gpu', methods=['GET'])
def gpu_usage():
    """
    Returns GPU usage (if available)
    ---
    responses:
      200:
        description: GPU usage statistics
        schema:
          type: object
          properties:
            name:
              type: string
            load:
              type: number
            memoryTotal:
              type: number
            memoryUsed:
              type: number
            memoryFree:
              type: number
            temperature:
              type: number
      404:
        description: GPU not available
    """
    if gpu_available:
        gpus = GPUtil.getGPUs()
        gpu_data = []
        for gpu in gpus:
            gpu_data.append({
                'name': gpu.name,
                'load': gpu.load * 100,
                'memoryTotal': gpu.memoryTotal,
                'memoryUsed': gpu.memoryUsed,
                'memoryFree': gpu.memoryFree,
                'temperature': gpu.temperature,
            })
        return jsonify(gpu_data)
    else:
        return jsonify({'error': 'GPU not available'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
