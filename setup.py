import setuptools

# readme fetch
with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='pytom-template-matching-gpu',
    packages=['pytom_tm'],
    package_dir={'': 'src'},
    version='0.1',
    description='GPU template matching from PyTOM as a lightweight pip package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPLv3',
    author='McHaillet (Marten Chaillet)',
    url='https://github.com/McHaillet/pytom-template-matching-gpu',
    platforms=['any'],
    python_requires='>=3.9',
    install_requires=[
        'numpy',
        'voltools',
        'tqdm',
        'mrcfile',
        'starfile',
        'importlib_resources',
    ],
    package_data={
        'pytom_tm.angle_lists': ['*.txt'],
    },
    # include_package_data=True,
    test_suite='tests',
    scripts=[
        'src/bin/create_mask.py',
        'src/bin/create_template.py',
        'src/bin/match_template.py',
        'src/bin/extract_candidates.py'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GPLv3 License',
        'Programming Language :: Python :: 3 :: Only',
    ]
)