from setuptools import setup, find_packages

setup(
    name="static-analysis-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "bandit==1.7.5",
        "pylint==3.0.3",
        "flake8==7.0.0",
        "radon==6.0.1",
        "click==8.1.7",
        "rich==13.7.0",
        "pyyaml==6.0.1",
    ],
    entry_points={
        'console_scripts': [
            'analyze=src.cli:main',
        ],
    },
    author="TiusLauren",
    description="AI-powered static code analysis agent",
    python_requires='>=3.8',
)
