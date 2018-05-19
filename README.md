<h1 align="left">  Autonomous Tour-Guide Robot  </h1>
<p align="left"> Senior practicum project - autonomous tour-guide robot - donkeycar platform </p>

<p align="center">
  <img width="500" height="300" src="https://github.com/weretew/Autonomous-Tour-Guide-Robot/blob/master/tour_guide_robot.gif?raw=true">
</p>


<h2 align="left"> Introduction </h2>
<p align="left"> Mechanical engineering senior project to build an autonoumous tour-guide robot that navigates an office building environment. Robot is tasked with providing tours to groups of people highlighting the various attractions of the building. </p>


<h2 align="left"> Deployment </h2>
<p align="left"> The base of the robot consists of a modified Traxxas Slash 4x4 utilizing a stock brushed motor and a nickel-metal hydride (NiMH) battery in order to reduce speed and better control the robot. The robot was built utilizing the
  
  [Donkeycar](https://github.com/wroscoe/donkey) platform, consisting of a Raspberry Pi, PiCam, PCA 9685 servo driver, and an RPLidar A2 360 laser scanner.</p>

<h2 align="left"> Dataset and Analysis </h2>
<p align="left"> In order to prevent the neural network from learning ever-changing objects in the course environment, e.g. moved furniture, the robot's camera was oriented at approximately 53° from the horizontal towards the ceiling.  In doing so, the network learned the course's ceiling lights and tiles, which enabled the robot to consistently navigate the course environment without being affected by ambient light or temporarily moved objects.</p>

<p align="center">
  <img width="700" height="300" src="https://github.com/weretew/Autonomous-Tour-Guide-Robot/blob/master/model_accuracy_comparison.png?raw=true"
       </p>
  
<h2 align="left"> Results </h2>
<p align="center">
  <img width ="700" height="300" src="https://github.com/weretew/Autonomous-Tour-Guide-Robot/blob/master/lstm_steering_plot.png?raw=true"
</p>


