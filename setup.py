from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='gldm',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'torch',
        # 'torch-cluster==1.6.0',
        # 'torch-scatter==2.1.0',
        # 'torch-sparse==0.6.15',
        # 'torchvision==0.14.0',
        # 'torchaudio==0.13.0',
        # 'torchmetrics==0.11.0',
        'torch-geometric',
        'omegaconf',
        'pandas',
        'pytorch_lightning',
        'tqdm',
        'rdkit',
        'tensorflow',
        'tensorboard',
        'einops',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)