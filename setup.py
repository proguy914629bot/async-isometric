import re
from setuptools import setup

with open('isometric_api/__init__.py') as f:
    try:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.M
        ).group(1)
    except AttributeError:
        raise RuntimeError('Could not identify version') from None

    # look at this boilerplate code
    try:
        author = re.search(
            r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.M
        ).group(1)
    except AttributeError:
        author = 'proguy914629'
   
readme = ''
with open('README.md', encoding='utf-8') as f:
    readme = f.read()
    
req = []
with open('requirements.txt', encoding='utf-8') as fp:
    req = fp.read().splitlines()

setup(
    name='isometric-api',
    author=author,
    url='https://github.com/proguy914629bot/isometric-api',
    version=version,
    project_urls={
        "Issue tracker": "https://github.com/proguy914629bot/isometric-api/issues",
    },
    packages=[
        'isometric-api'
    ],
    license='MIT',
    description='A async wrapper to the Isometric API (https://jeyy-api.herokuapp.com)',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=req,
    extras_require={
        'docs': [
            'sphinx>=4.0.2',
            'karma_sphinx_theme>=0.0.8',
            'sphinxcontrib-asyncio>=0.3.0',
            'sphinx-nervproject-theme>=2.0.4',
        ]
    },
    python_requires='>=3.7.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
