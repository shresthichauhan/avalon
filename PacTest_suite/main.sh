#!/bin/bash
location=/Jenkins_Publish/SDPTool/PacTest_suite/Tests
cd $location
echo '============================================'
echo 'Pre-PacTest suite cleanup'
echo 'START'
echo '--------------------------------------------'
$location/epoch.sh
echo '--------------------------------------------'
echo 'Pre-PacTest suite cleanup'
echo 'END'
echo '============================================'
$location/Testcase1.sh
$location/Testcase2.sh
$location/Testcase3.sh
$location/Testcase4.sh
$location/Testcase5.sh
$location/Testcase6.sh
$location/Testcase7.sh
$location/Testcase8.sh
$location/Testcase9.sh
$location/Testcase10.sh
$location/Testcase11.sh
$location/Testcase12.sh
$location/Testcase13.sh
$location/Testcase14.sh
$location/Testcase15.sh
$location/Testcase16.sh
$location/Testcase17.sh
$location/Testcase18.sh
$location/Testcase19.sh
$location/Testcase20.sh
$location/Testcase21.sh
