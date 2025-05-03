Proyecto de Prueba: FastAPI con GitHub Actions

Este proyecto es una demostración sencilla de cómo integrar una aplicación FastAPI con un pipeline de CI/CD utilizando GitHub Actions. La aplicación expone un endpoint que devuelve un código de estado HTTP aleatorio, y el pipeline automatiza la ejecución de pruebas para verificar su correcto funcionamiento.

Características del Proyecto
FastAPI: Framework moderno y de alto rendimiento para construir APIs con Python.

Pytest: Framework de pruebas utilizado para validar el comportamiento del endpoint.

GitHub Actions: Automatización de pruebas en cada push al repositorio.

Pipeline Condicional: El pipeline muestra un mensaje de éxito si las pruebas pasan y un mensaje de error si fallan.

Pruebas Automatizadas

Se ha implementado una prueba que verifica que el endpoint / devuelve un código de estado 200. Dado que la respuesta es aleatoria, esta prueba puede fallar intencionalmente, lo que permite observar el comportamiento del pipeline en ambos escenarios.
