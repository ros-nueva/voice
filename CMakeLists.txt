cmake_minimum_required(VERSION 2.8.3)
project(voice)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED)
## Generate actions in the 'action' folder

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_srvs
  std_msgs
  actionlib
  actionlib_msgs
  message_generation
)

add_action_files(
  FILES
  Text.action
)

generate_messages(
  DEPENDENCIES
  std_srvs
  std_msgs
  actionlib
  actionlib_msgs
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES package_test
  CATKIN_DEPENDS rospy message_generation
#  DEPENDS system_lib
)

# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
