#!/bin/bash
# Test 1: Respuesta básica
curl -s http://localhost:5000 | grep "hello" || exit 1

# Test 2: Respuesta 404
curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/ruta-inexistente | grep 404 || exit 1
