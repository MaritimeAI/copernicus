from setuptools import setup

setup(
    name='copernicus',
    version='0.1.0',
    packages=['copernicus'],
    url='https://github.com/MaritimeAI/copernicus',
    license='MIT',
    author='ValV',
    author_email='0x05a4@gmail.com',
    description='ESA Copernicus Open Access Hub module',
    install_requires=[
        'marshmallow',
        'shapely'
    ]
)
