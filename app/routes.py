import os
import subprocess

from flask import Blueprint, request, jsonify

code_processor = Blueprint('compiler', __name__)

SOURCE_FILE = 'main.cpp'
EXECUTABLE = 'main'

CC = 'g++'
DIALECT = '-std=c++11'

@code_processor.route('/compile-code', methods=['POST'])
def compile_code():
    source_code = request.json.get('sourceCode')    

    for file in (SOURCE_FILE, EXECUTABLE):
        if os.path.exists(file):
            os.remove(file)
    
    with open(SOURCE_FILE, 'w') as file:
        file.write(source_code)

    compilation_result = subprocess.run([CC, DIALECT, '-ggdb', '-O0', '-fno-omit-frame-pointer', '-o', EXECUTABLE, 'main.cpp'], capture_output=True, text=True)


    if compilation_result.returncode == 0:
        execution_result = subprocess.run([f'./{EXECUTABLE}'], capture_output=True, text=True)
        return jsonify({'output': execution_result.stdout, 'return_code': compilation_result.returncode})

    return jsonify({'error': compilation_result.stderr, 'return_code': compilation_result.returncode})