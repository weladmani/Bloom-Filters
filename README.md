# Bloom Filters Interactive Demo

An interactive web-based demonstration of Bloom filters, a probabilistic data structure for space-efficient membership testing.

## What is a Bloom Filter?

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. It can tell you with certainty that an item is **not** in the set, but it might give false positives (indicating an item is in the set when it's actually not).

### Key Characteristics:
- **No false negatives**: If the filter says an item is not present, it's definitely not present
- **Possible false positives**: The filter might incorrectly report that an item is present
- **Space efficient**: Uses significantly less memory than storing the actual set
- **Fast operations**: Constant time for insertions and lookups

## How It Works

Bloom filters use:
- A bit array of size `m`
- `k` different hash functions
- Each element is hashed `k` times, setting the corresponding bits to 1
- For membership testing, an element is hashed and checked if all corresponding bits are 1

## Running the Demo

1. Open `index.html` in any modern web browser
2. No installation or server required - it's a standalone HTML file

## Demo Features

### Filter Designer
- Adjust expected number of elements (`n`)
- Set target false positive rate (`p`)
- See the calculated optimal bit array size (`m`) and number of hash functions (`k`)
- Apply your design to the interactive demo

### Interactive Controls
- **Insert**: Add words to the Bloom filter
- **Check**: Test if a word is in the filter
- **Auto Demo**: Run an automated demonstration
- **Reset**: Clear the filter and start over

### Visualizations
- **Bit Array Grid**: Visual representation of the bit array with real-time updates
- **Hash Trace**: Shows the hash positions for each operation
- **Statistics**: Displays current item count, bit occupancy, and measured false positive rate
- **Operation Log**: History of all operations performed

### Educational Elements
- Real-time calculation of theoretical vs. measured false positive rates
- Animated bit flips and result feedback
- Formula display showing how `m` and `k` are calculated

## Mathematical Background

The optimal parameters are calculated using:

```
m = ⌈ -n × ln(p) / (ln 2)² ⌉
k = ⌈ (m / n) × ln 2 ⌉
```

Where:
- `n` = expected number of elements
- `p` = target false positive probability
- `m` = size of bit array
- `k` = number of hash functions

## Browser Compatibility

Works in any modern browser with JavaScript enabled. No external dependencies.

## License

This demo is provided as-is for educational purposes.
