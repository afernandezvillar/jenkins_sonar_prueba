import subprocess

# Ejecutar pytest con cobertura
subprocess.call(['coverage', 'run', '-m', 'pytest'])
subprocess.call(['coverage', 'xml', '-i'])
comando = f"pytest --cov={'./'} --cov-report xml:test-coverage.xml"
subprocess.run(comando, shell=True)