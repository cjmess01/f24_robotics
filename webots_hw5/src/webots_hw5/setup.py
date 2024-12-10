from setuptools import find_packages, setup

package_name = 'webots_hw5'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/webots_hw5.launch.py']))


data_files.append(('share/' + package_name + '/webots_hw5', [
    'webots_hw5/webots_hw5.py', 
]))


data_files.append(('share/' + package_name + '/worlds', [
    'worlds/maze.wbt', 
]))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/maze1_smallest.wbt', 
]))


data_files.append(('share/' + package_name, ['package.xml']))

data_files.append(('share/' + package_name + '/resource', [
    'resource/turtlebot_webots.urdf',
    'resource/ros2control.yml',
]))

# data_files.append(('share/' + package_name + '/rviz', [
#     'rviz/turtlebot3_apriltags.rviz', 
# ]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Caleb messerly - UA',
    maintainer_email='cjmesserly@crimson.ua.edu',
    description='Webots HW5',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],    
        'console_scripts': ['webots_hw5_controller = webots_hw5.webots_hw5:main']
    },

)