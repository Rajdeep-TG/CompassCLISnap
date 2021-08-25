import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="PyCompass",
    version="1.1.0",
    author="TechGeeks",
    author_email="ZypeLang@tgeeks.cf",
    maintainer="Rajdeep Malakar",
    maintainer_email="Rajdeep@tgeeks.cf",
    description="Compass CLI for ZypeLang (Linux [AMD64] Snap)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zype-Z/Compass-Snap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'ZypeSDK',
        'rich'
    ],
    entry_points=dict(
        console_scripts=['pycompass=pycompass.compass:main']
    )
)
