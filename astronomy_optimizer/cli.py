import argparse

def create_parser():
    """Create the CLI parser."""
    parser = argparse.ArgumentParser(description='Astronomy Parameter Optimizer')
    parser.add_argument('--strategy', type=str, default='grid',
                        help='search strategy: grid, random, annealing (default: grid)')
    parser.add_argument('--num_samples', type=int, default=100,
                        help='number of samples for the search space (default: 100)')
    parser.add_argument('--max_iter', type=int, default=10,
                        help='maximum number of iterations (default: 10)')
    return parser

def parse_args():
    """Parse the CLI arguments."""
    parser = create_parser()
    args = parser.parse_args()
    return vars(args)

if __name__ == '__main__':
    print(parse_args())
