#!/usr/bin/env python3
"""Short Bloom filter demo illustrating core characteristics.

Run:
    python3 demo_bloom.py
"""

from __future__ import annotations

import hashlib
import math
import random
import string


class BloomFilter:
    def __init__(self, bit_count: int, hash_count: int) -> None:
        self.m = bit_count
        self.k = hash_count
        self.bits = [0] * self.m

    def _hashes(self, item: str):
        # Double hashing trick: derive k hashes from two base hashes.
        h1 = int(hashlib.sha256(item.encode()).hexdigest(), 16)
        h2 = int(hashlib.md5(item.encode()).hexdigest(), 16)
        for i in range(self.k):
            yield (h1 + i * h2) % self.m

    def add(self, item: str) -> None:
        for idx in self._hashes(item):
            self.bits[idx] = 1

    def might_contain(self, item: str) -> bool:
        return all(self.bits[idx] for idx in self._hashes(item))

    def bit_occupancy(self) -> float:
        return sum(self.bits) / self.m


def random_token(length: int = 10) -> str:
    alphabet = string.ascii_lowercase + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def theoretical_false_positive_rate(m: int, k: int, n: int) -> float:
    # p ≈ (1 - e^(-kn/m))^k
    return (1 - math.e ** (-(k * n) / m)) ** k


def run_demo() -> None:
    random.seed(7)

    item_count = 300
    test_count = 3000
    bit_count = 3000
    hash_count = 7

    bloom = BloomFilter(bit_count, hash_count)

    inserted = {random_token() for _ in range(item_count)}
    while len(inserted) < item_count:
        inserted.add(random_token())

    for token in inserted:
        bloom.add(token)

    # Build test set disjoint from inserted set.
    queries = []
    while len(queries) < test_count:
        token = random_token()
        if token not in inserted:
            queries.append(token)

    false_positives = sum(1 for token in queries if bloom.might_contain(token))

    # Demonstrate no false negatives.
    false_negatives = sum(1 for token in inserted if not bloom.might_contain(token))

    measured_fp_rate = false_positives / test_count
    expected_fp_rate = theoretical_false_positive_rate(bit_count, hash_count, item_count)

    print("=== Bloom Filter Demo ===")
    print(f"Inserted items (n): {item_count}")
    print(f"Bit array size (m):  {bit_count}")
    print(f"Hash functions (k):  {hash_count}")
    print()

    print("Characteristics shown:")
    print(f"1) No false negatives: {false_negatives} missed inserted items")
    print(
        f"2) False positives exist: {false_positives}/{test_count} "
        f"({measured_fp_rate:.2%})"
    )
    print(f"3) Bit occupancy: {bloom.bit_occupancy():.2%}")
    print(f"4) Theoretical FP rate (approx): {expected_fp_rate:.2%}")


if __name__ == "__main__":
    run_demo()
