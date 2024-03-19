import argparse
from pathlib import Path

from .generator import ORCA_Generator
from .jobscript import PBS_Jobscript, SLURM_Jobscript


class CLI:
    """Class to bundle command line interaction functionalities."""

    def get_args() -> argparse.Namespace:
        """Get parser arguments."""
        parser = argparse.ArgumentParser()
        parser.add_argument("data", type=Path, help="Directory containing raw data.")
        parser.add_argument(
            "--jobscript",
            "-js",
            type=str,
            default="SLURM",
            help="Identifier for job submission script.",
        )
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete all ORCA input files.",
        )
        return parser.parse_args()


# ENTRYPOINT
if __name__ == "__main__":
    args = CLI.get_args()

    # TODO: add your `Jobscript` and logic
    jobscript = SLURM_Jobscript() if args.jobscript == "SLURM" else PBS_Jobscript()

    if not args.data.is_dir():
        raise FileNotFoundError

    print(f"Setting up ORCA calulcations in {args.data}")
    og = ORCA_Generator(args.data, jobscript)
    if args.delete:
        og.cleanup()
    else:
        og()
