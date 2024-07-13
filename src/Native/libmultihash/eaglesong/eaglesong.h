#ifndef EAGLESONG_H
#define EAGLESONG_H

#ifdef __cplusplus
extern "C" {
#endif

#include <cstddef>
#include <cstdint>

void eaglesong_hash(const uint8_t *input, size_t input_size, uint8_t *output);

#endif // EAGLESONG_H