import argparse

def create_parser():
    """
    Create the CLI parser.

    Returns:
        ArgumentParser: The created CLI parser.
    """
    parser = argparse.ArgumentParser(description='Astronomy Parameter Optimizer')
    parser.add_argument('--strategy', type=str, default='grid',
                        help='Search strategy (default: grid)')
    parser.add_argument('--num_samples', type=int, default=100,
                        help='Number of samples for the search space (default: 100)')
    parser.add_argument('--max_iter', type=int, default=10,
                        help='Maximum number of iterations (default: 10)')
    return parser

def parse_args():
    """
    Parse the CLI arguments.

    Returns:
        dict: The parsed CLI arguments as a dictionary.
    """
    parser = create_parser()
    args = parser.parse_args()
    
    # Validate and handle edge cases
    if not isinstance(args.strategy, str):
        raise ValueError("Strategy must be a string")
    elif args.strategy.lower() not in ['grid', 'random']:
        print(f"Warning: Unknown strategy '{args.strategy}'. Defaulting to grid.")
        args.strategy = 'grid'
        
    if not (isinstance(args.num_samples, int) and args.num_samples > 0):
        raise ValueError("Number of samples must be a positive integer")
    elif args.num_samples < 10:
        print(f"Warning: Number of samples ({args.num_samples}) is less than the recommended minimum of 10.")
        
    if not (isinstance(args.max_iter, int) and args.max_iter >= 0):
        raise ValueError("Maximum iterations must be a non-negative integer")
    elif args.max_iter < 1:
        print(f"Warning: Maximum iterations ({args.max_iter}) is less than the recommended minimum of 1.")
        
    return vars(args)

if __name__ == '__main__':
    import pprint
    print(pprint.pformat(parse_args()))
