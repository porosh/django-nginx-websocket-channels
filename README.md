# to run directly

gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# to run using docker

docker compose up

# test directly , open browser

http://127.0.0.1:8000/test_websocket/

# test using nginx, open browser

http://127.0.0.1/test_websocket/
