from setuptools import find_packages, setup

setup(
    name='dcsam',
    version='0.1dev',
    packages=find_packages(),
    license='',
    python_requires=">=3.8.*",
    install_requires=[
        'scipy>=1.4.1',
        'matplotlib>=3.2.1',
        'tqdm>=4.46.0',
        'numpy>=1.18.4',
        'opencv-python>=4.2.0.34',
        'pillow>=7.1.2',
        'tensorboard>=2.2.1',
        'torch>=1.6.0',
        'torchvision>=0.4.2',
    ],
    include_package_data=True,
    packages_data={'': ['*, yaml', '*.cu', '*.cpp', '*,h']},
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown'
)