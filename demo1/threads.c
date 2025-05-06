#!/usr/bin/tcc -run
#include <inttypes.h>
#include <pthread.h>
#include <stdio.h>

const uint64_t MAX = 100000000;// (uint64_t)0-1;
// 1e10, != euler, es (2^10)
uint64_t i = 0;

void* hilo_fn(void* arg) {
    uint64_t j = 0;
    while (j++ < MAX) {
      i++;
    }
    return NULL;
}

int main() {
    printf("MAX: %llu\n", MAX);

    pthread_t thread1; // Declara objeto de configuración
    pthread_create(&thread1, NULL, hilo_fn, NULL); // El constructor

    hilo_fn(NULL);

    pthread_join(thread1, NULL);

    printf("i: %llu\n", i);
    return 0;
}
