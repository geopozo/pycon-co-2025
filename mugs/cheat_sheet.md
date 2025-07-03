## Coroutines

```py
## Coroutines
import asyncio # 👈 this library is already native since 3.13.5

# 👇"async" always at the beginning
async def get_carrot():
    return "🥕"

async def main():
    # --- 👇 "await" your result from the function
    print(await get_carrot()) # You got a 🥕!
# 👇 Required to start the coroutineV
asyncio.run(main())
```

## Task
```py
import asyncio

async def make_hole():
    return "Hole made"

async def main():
    # ------------ 👇 Use it to start a task
    task = asyncio.create_task(make_hole())
    await task # Task done

asyncio.run(main())
```



# Corutinas

```python
async def hola():
  return "Hello World"

foo() # devuelve un objeto: una corutina
await foo() # devuelve "Hello World"
```

- No se puede esperar mas de una vez
- Tienes que esperar para empezar la ejucucion

# Tareas

```python
await asyncio.create_task(foo()) # el argumento es una corutina
```

- Empieza a ejecutar cuando se crea, no se espera
- Puedes esperar > 1 vez

# Futuros

```python
f = asyncio.get_running_loop().create_future()
```

- De bajo nivel
- Tienes que f.set_result(...) f.set_exception(...)

# Gather

await asyncio.gather(tarea1, tarea2, ..., return_exceptions=True)

# TaskGroup

(python 3.11)

with asyncio.TaskGroup() as tg:
  tg.create_task()

Se cancela todo juntos
