from pathlib import Path

from tqdm import tqdm

from .command import Command, Default_Command
from .jobscript import Jobscript


class ORCA_Generator:
    chrg_file = ".CHRG"
    """File containing total charge of molecule."""
    uhf_file = ".UHF"
    """File containing number of unpaired electrons."""

    def __init__(
        self,
        folder: Path,
        jobscript: Jobscript,
        fname: str = "sample.xyz",
        cmd: Command = Default_Command(),
    ):
        """
        Generator to create ORCA input for given samples.

        Parameters
        ----------
        folder : Path
            The root directory path that contains each sample in its own subdirectory.
        jobscript : Jobscript
            A callable script that handles the submission of jobs to your computing cluster.
        fname : str, optional
            The name of the XYZ file(s) to be used for simulations, by default "sample.xyz".
        cmd : Command, optional
            A callable that generates the ORCA command to be written to the "orca.inp" file, by default Default_Command.
        """
        self.folder = folder
        self.jobscript = jobscript
        self.fname = fname
        self.cmd = cmd

    def __call__(self):
        """Set up ORCA inputs for all samples contained in `self.folder`."""
        for file in tqdm(self.folder.rglob(self.fname), desc="Setting up"):
            self.generate_orca_input(file.parent)

    def inp(self, charge: int, multiplicity: int, *args, **kwargs) -> str:
        """Content of `orca.inp`."""
        return f"""\
{self.cmd(*args, **kwargs)}
* XYZfile {charge} {multiplicity} ./{self.fname}"""

    def generate_orca_input(self, folder: Path):
        """Generate ORCA input files for the specified folder."""

        # read molecular charge
        with (folder / self.chrg_file).open("r") as f:
            chrg = int(f.read())

        # read multiplicity (2S+1)
        with (folder / self.uhf_file).open("r") as f:
            multi = int(f.read()) + 1

        # write orca input
        with open(folder / "orca.inp", "w") as outfile:
            outfile.write(self.inp(chrg, multi))

        # write job script
        with open(folder / "orca_job", "w") as outfile:
            # TODO: add your logic here ...
            outfile.write(self.jobscript("Ndummy", "Pdummy", "Adummy"))

    def cleanup(self, rm_files: list[str] = ["orca.inp", "orca_job"]):
        """Remove all ORCA related input files and reset the root folder to its initial state."""
        for file in tqdm(self.folder.rglob(self.fname), desc="Deleting"):
            for name in rm_files:
                fp = file.parent / name
                if fp.exists():
                    fp.unlink()
