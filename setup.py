from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='mir_eval',
    version='0.7',
    description='Common metrics for common audio/music processing tasks.',
    author='Colin Raffel',
    author_email='craffel@gmail.com',
    url='https://github.com/craffel/mir_eval',
    packages=['mir_eval'],
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Programming Language :: Python :: 3",
    ],
    keywords='audio music mir dsp',
    license='MIT',
    install_requires=[
        'numpy >= 1.7.0',
        'scipy >= 1.0.0',
    ],
    extras_require={
        'display': ['matplotlib>=1.5.0'],
        'testing': ['matplotlib>=2.1.0',
                    'decorator',
                    'pytest',
                    'pytest-cov',
                    'pytest-mpl',
                    'nose']
    },
    python_requires='>=3',
)
