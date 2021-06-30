from setuptools import setup

package_name = 'wasp_mini_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wasp_mini',
    maintainer_email='wasp_mini@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["motor_FL=wasp_mini_controller.motor_FL:main",
        "motor_FR=wasp_mini_controller.motor_FR:main",
        "actuator_position=wasp_mini_controller.actuator_fb:main",
        "main_node=wasp_mini_controller.main:main"
        ],
    },
)
