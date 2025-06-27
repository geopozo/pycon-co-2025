import asyncio

class DelayedValue:
    def __init__(self, value, delay=1):
        self.value = value
        self.delay = delay

    def __call__(self):
        print(f"Called with value={self.value}, delay={self.delay}")
        return self

    def __await__(self):
        async def inner():
            await asyncio.sleep(self.delay)
            return self.value
        return inner().__await__()  # Returns an awaitable object

# Usage
async def main():
    obj = DelayedValue("Hello!", delay=2)

    # Call it like a function
    obj()

    # Await it like a coroutine
    result = await obj
    print("Result:", result)

