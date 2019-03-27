from setuptools import find_packages, setup

setup(
        name='lab',
        version='1.0.0',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'flask',
            'flask_assets',
            'jsmin',
            'cssmin',
            'requests',
            'wtforms',
            'flask-wtf'
        ],
)
