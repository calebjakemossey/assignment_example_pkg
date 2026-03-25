from setuptools import setup

package_name = 'example_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        # Only for ROS support: register package with ament index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Only for ROS support: include package.xml
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'pyfiglet>=0.8.post1',
    ],
    zip_safe=True,
    author='Some Name',
    author_email='example @example.com',
    description='ROS-independent example package with pyfiglet dependency',
    # license='TODO',
    entry_points={
        'console_scripts': [
            'example_runner = example_package.example_runner:main',
        ],
    },
)
