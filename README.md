# rawberth Oh-nope IRC Services

> :warning: This project has not released its first major version.

Ridiculous, waste of time, implementation of IRC services using Python.

"Oh that is nifty, I guess." Should you use these services? "Oh, nope."

<a href="https://rawberth.github.io/ohnope/validate/flake8.txt"><img src="https://rawberth.github.io/ohnope/badges/flake8.png"></a><br>
<a href="https://rawberth.github.io/ohnope/validate/pylint.txt"><img src="https://rawberth.github.io/ohnope/badges/pylint.png"></a><br>
<a href="https://rawberth.github.io/ohnope/validate/ruff.txt"><img src="https://rawberth.github.io/ohnope/badges/ruff.png"></a><br>
<a href="https://rawberth.github.io/ohnope/validate/mypy.txt"><img src="https://rawberth.github.io/ohnope/badges/mypy.png"></a><br>
<a href="https://rawberth.github.io/ohnope/validate/yamllint.txt"><img src="https://rawberth.github.io/ohnope/badges/yamllint.png"></a><br>
<a href="https://rawberth.github.io/ohnope/validate/pytest.txt"><img src="https://rawberth.github.io/ohnope/badges/pytest.png"></a><br>
<a href="https://rawberth.github.io/ohnope/validate/coverage.txt"><img src="https://rawberth.github.io/ohnope/badges/coverage.png"></a><br>
<a href="https://rawberth.github.io/ohnope/validate/sphinx.txt"><img src="https://rawberth.github.io/ohnope/badges/sphinx.png"></a><br>

## Documentation
Read [project documentation](https://rawberth.github.io/ohnope/sphinx)
built using the [Sphinx](https://www.sphinx-doc.org/) project.
Should you venture into the sections below you will be able to use the
`sphinx` recipe to build documention in the `sphinx/html` directory.

## Installing the package
Installing latest from GitHub repository
```
pip install git+https://github.com/rawberth/ohnope
```

## Quick start for local development
Start by cloning the repository to your local machine.
```
git clone https://github.com/rawberth/ohnope.git
```
Set up the Python virtual environments expected by the Makefile.
```
make -s venv-create
```

### Execute the linters and tests
The comprehensive approach is to use the `check` recipe. This will stop on
any failure that is encountered.
```
make -s check
```
However you can run the linters in a non-blocking mode.
```
make -s linters-pass
```
And finally run the various tests to validate the code and produce coverage
information found in the `htmlcov` folder in the root of the project.
```
make -s pytest
```

## Running the service
There are several command line arguments, see them all here.
```
python -m enrobie.execution.service --help
```
Here is an example of running the service from inside the project folder
within the [Workspace](https://github.com/enasisnetwork/workspace) project.
```
python -m ohnope.execution.service \
  --config ../../Persistent/ohnope-devel.yml \
  --console \
  --debug \
  --print_command
```
Replace `../../Persistent/ohnope-devel.yml` with your configuration file.

## Version management
> :warning: Ensure that no changes are pending.

1. Rebuild the environment.
   ```
   make -s check-revenv
   ```

1. Update the [version.txt](ohnope/version.txt) file.

1. Push to the `main` branch.

1. Create [repository](https://github.com/rawberth/ohnope) release.
