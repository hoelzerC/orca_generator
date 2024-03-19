# ORCA Generator
[![Python](https://img.shields.io/badge/python-3.11.4-blue.svg)](https://www.python.org)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



The ORCA Generator is a tool designed for simplifying the submission of computational chemistry jobs, using [ORCA software](https://www.orcasoftware.de/), on various cluster setups. Due to the individual nature of cluster configurations across institutions, this tool requires users to provide a custom implementation of a jobscript class tailored to their specific cluster environment.

<div align="left">
<img src="./logo.png" alt="ORCA Generator" width="100" height="100">
</div>


## Configuration

You are required to write your own implementation of a jobscript class to match your institutional setup. To assist you in this task, examples for PBS and SLURM clusters are provided with the classes `PBS_Jobscript` and `SLURM_Jobscript`. 

To further configure the ORCA Generator for your needs:

- Change `ORCA_Generator.cmd` to fit your specific requirements.
- Look for `TODO` comments throughout the codebase to find places where your input is required.


## Running the ORCA Generator

To run the ORCA Generator, use the following command from your terminal:

```bash
python -m orca_generator
```


## Contributing and License

If you have suggestions for improving this tool or have developed jobscript implementations that could benefit others in the community, please feel free to contribute to this project by submitting a pull request.

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
