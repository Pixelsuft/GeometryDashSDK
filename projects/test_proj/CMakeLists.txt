cmake_minimum_required(VERSION 3.0.0)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(test_proj CXX)

add_library(cocos2d INTERFACE)
add_library(test_proj SHARED src/main.cpp)


# really make sure its c++
set_target_properties(cocos2d PROPERTIES
  LANGUAGE CXX
  LINKER_LANGUAGE CXX
)

add_subdirectory(minhook)
add_subdirectory(gd.h)

target_include_directories(cocos2d INTERFACE 
  cocos2dx
  cocos2dx/include
  cocos2dx/kazmath/include
  cocos2dx/platform/win32
  cocos2dx/platform/third_party/win32
  cocos2dx/platform/third_party/win32/OGLES
  extensions
)

target_link_libraries(cocos2d INTERFACE
  ${CMAKE_CURRENT_LIST_DIR}/cocos2dx/libcocos2d.lib
  ${CMAKE_CURRENT_LIST_DIR}/extensions/libExtensions.lib
  minhook
)

target_include_directories(test_proj INTERFACE 
  cocos2dx
  cocos2dx/include
  cocos2dx/kazmath/include
  cocos2dx/platform/win32
  cocos2dx/platform/third_party/win32
  cocos2dx/platform/third_party/win32/OGLES
  extensions
  minhook/include
)

target_link_libraries(test_proj 
  ${CMAKE_SOURCE_DIR}/cocos2dx/libcocos2d.lib
  minhook
  cocos2d
  gd.h
)
