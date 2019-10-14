cmake_minimum_required(VERSION 2.8.3)
project(navigation_uao)

find_package(catkin REQUIRED COMPONENTS 
roscpp
rospy
message_generation
  pcl_ros
  pcl_conversions
  pcl_msgs
  std_msgs
  geometry_msgs
  sensor_msgs
  velodyne_msgs
  nav_msgs
  base_local_planner
  costmap_2d
  move_base
  move_base_msgs
  actionlib
  nav_core
  tf
  nav_msgs
  pluginlib
  cmake_modules
  roslaunch
	pointcloud_to_laserscan
	spatio_temporal_voxel_layer
	
)


find_package(PCL REQUIRED)

catkin_package()

roslaunch_add_file_check(launch/include/move_base.launch)
roslaunch_add_file_check(launch/include/move_base_spatio.launch)
roslaunch_add_file_check(launch/include/move_base_spatio_cam.launch)
roslaunch_add_file_check(launch/include/move_base_voxel.launch)
roslaunch_add_file_check(launch/odom_navigation_costmap.launch)
roslaunch_add_file_check(launch/odom_navigation_voxel.launch)
roslaunch_add_file_check(launch/odom_navigation_spatio.launch)
roslaunch_add_file_check(launch/odom_navigation_spatio_cam.launch)
roslaunch_add_file_check(launch/pointcloud_filter.launch)

install(
DIRECTORY launch params src
DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)



