import os
import daphne.server

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
    
    # Configura i percorsi per i certificati
    certfile = "server.crt"
    keyfile = "server.key"

    # Esegui Daphne con HTTPS
    daphne.server.Service(
        application='BarAccademia.asgi:application',
        ssl_certfile=certfile,
        ssl_keyfile=keyfile,
        bind_address='0.0.0.0',
        port=443,
        root_path=""
    ).run()
