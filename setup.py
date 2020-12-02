from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='genesyscloudcli',
    version='0.4',
    py_modules=['genesyscloudcli'],
    license='MIT',
    description = "CLI to interact with Genesys Cloud",
    keywords = ['purecloud', 'genesys', 'genesys cloud'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    install_requires=[
        'Click',
        'pyyaml',
        'websockets',
        'requests', 
        'aioconsole',
        'tabulate'
    ],
    entry_points='''
        [console_scripts]
        # each line identifies one console script. 
        # The first part before the equals sign (=) is the name of the script that should be generated,
        # the second part is the import path followed by a colon (:) with the Click command.
        gc=genesyscloudcli.clidriver:cli
        gcli=genesyscloudcli.clidriver:cli
    ''',
)