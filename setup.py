# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'pylama',
    'pytest',
]
unit_test_requirements = [
    'pytest',
]
integration_test_requirements = [
    'pytest',
]
run_requirements = [
    'fastapi',
    'uvicorn',
    'python-jose[cryptography]',
    'passlib[bcrypt]',
    'python-multipart'
]

with io.open('./oauth_template/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="oauth-template",
    version=version,
    author="Yassunaga",
    author_email="gabriel_yassunaga@hotmail.com",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    # url="https://gitlab.com/projetos-automatizai/conass/login-conass",
    license="COPYRIGHT",
    description="Login do CONASS",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
        'dev': dev_requirements,
        'unit': unit_test_requirements,
        'integration': integration_test_requirements,
    },
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'oauth_template = oauth_template.__main__:start'
        ],
    },
)
