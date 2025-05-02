Bilingüe

Más que Javascript: Cosas Nuevas con async/await en Python 3.10, 3.11, 3.12

asyncio/trio

1. Qué es el estado de async/await in python?
  -- paquetes de terceros esenciales (aiohttp, aiofile)
2. Cómo se compara con los sistemas en javascript
  - Los dos de un hilo? Es un poco más avanzado
  - Un poco más raro (generadores, los problemas con typing)
  - Arquitecturas distintas:
    - Basado en events, el web que ya sabemos, pero en python...
4. El paralellismo de muchas tareas, y la creación de paquetes nuevos:
  - Errors se levantan y se bajan y atracan de todos lados
  - Try/Await (performance bottle neck)
  - Cancelaciones, y Errores Nuevos
4. Las reglas especificas, para cuidar con python async/await:
  - Corutinas, Futuros, Tareas
  - Dificultad con async+sync
  - El GIL, que es, y como nos bloquea?
5. TaskGroups, Gather, or writing your own (complicated!)
  6. Los beneficios y malo de TaskGroups
5. Y que va a pasar con los hilos de python?- freethreaded va a cambiar todo


(Use jax examples as a bonus)
(Inject choreographer examples as a bonus)
