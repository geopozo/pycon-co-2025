from threading import Thread

i = 0
MAX = 100_000_000
def hilo_fn():
    global i
    for _ in range(MAX):
        i+=1

def main():

    t = Thread(target=hilo_fn)

    t.start()

    hilo_fn()

    t.join()
    print(i)


if __name__ == "__main__":
    main()
