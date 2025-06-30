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
# 👇 Required to start the coroutine
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
