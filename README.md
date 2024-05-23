# liftOverLoops

liftOverLoops is a Python 3 wrapper for the liftOver tool, allowing users to convert BEDPE files from one genome build to another.

## Prerequisites

To use liftOverLoops, you'll need the following:

- [liftOver](https://genome.sph.umich.edu/wiki/LiftOver)
- A liftOver chain file
- Python 3

## Installation

You can simply download the `liftOverBedpe.py` script from the repository and place it in your desired location. Make sure you have Python 3 installed on your system.

## Usage

liftOverBedpe.py --help

### Options:

- `--lift LIFT_OVER`: Path to the liftOver executable
- `--chain CHAIN_FILE`: Path to the liftOver chain file
- `--i INPUT_FILE`: Path to the input BEDPE file
- `--o OUTPUT_FILE`: Path to the output file
- `--v`: Enable verbose mode
- `--h`: Set if the input file has a header line

### Example:

liftOverBedpe.py --lift ./liftOver/liftOver --chain ./liftOver/mm9ToMm10.over.chain.gz --i example.mm9.bedpe --o output.mm10.bed --v

## Additional Resources

You can find the original `liftOverBedpe.py` script written by Doug Phanstiel on [GitHub](https://github.com/cauyrd/liftOverBedpe/blob/main/liftOverBedpe.py).

For more information about the liftOver tool and how to use it, refer to the [liftOver documentation](https://genome.sph.umich.edu/wiki/LiftOver).
