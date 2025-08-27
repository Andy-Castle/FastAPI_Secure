# Comandos para crear el certificado de OpenSSL

openssl genrsa -out clave.key 2048
openssl req -new -x509 -key clave.key -out certificado.crt -days 365

# Para que arranque con https

uvicorn main:app --host 127.0.0.1 --port 8000 --ssl-keyfile="cert\clave.key" --ssl-certfile="cert\certificado.crt"

uvicorn main:app --reload --host 127.0.0.1 --port 8000 --ssl-keyfile="cert\clave.key" --ssl-certfile="cert\certificado.crt"
