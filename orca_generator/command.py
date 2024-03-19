from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract class for ORCA command."""

    @abstractmethod
    def __call__(self, *args, **kwargs) -> str:
        """Return the ORCA input file command."""
        pass


class Default_Command(Command):
    def __call__(self, *args, **kwargs) -> str:
        """Default ORCA command written to `orca.inp` file."""
        return f"""\
! wB97M-V def2-TZVPD DEFGRID2 TightSCF PAL4
%scf
MaxIter 2000
end
%geom
MaxIter 500
end"""


# TODO: add your command specifications
