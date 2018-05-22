<h1 align="left">  Autonomous Tour-Guide Robot  </h1>
<p align="left"> Senior practicum project - autonomous tour-guide robot - donkeycar platform </p>

<p align="center">
  <img width="500" height="300" src="https://github.com/weretew/Autonomous-Tour-Guide-Robot/blob/master/tour_guide_robot.gif?raw=true">
</p>


<h2 align="left"> Introduction </h2>
<p align="left"> Mechanical engineering senior project to build an autonoumous tour-guide robot that navigates an office building environment. Robot is tasked with providing tours to groups of people highlighting the various attractions of the building. </p>


<h2 align="left"> Deployment </h2>
<p align="left"> The base of the robot consists of a modified Traxxas Slash 4x4 utilizing a stock brushed motor and a nickel-metal hydride (NiMH) battery in order to reduce speed and better control the robot. The robot was built utilizing the
  
  [Donkeycar](https://github.com/wroscoe/donkey) platform. The robot consists of a Raspberry Pi, PiCam, PCA 9685 servo driver, Apple iPad (tour experience), as well as an RPLidar A2 360 laser scanner for safety measures.</p>

<h2 align="left"> Dataset and Analysis </h2>
<p align="left"> In order to prevent the neural network from learning ever-changing objects in the course environment, e.g. moved furniture, the robot's camera was oriented at approximately 53° from the horizontal towards the ceiling.  In doing so, the network learned the course's ceiling lights and tiles, which enabled the robot to consistently navigate the course environment without being affected by ambient light or temporarily moved objects.
</p>

<p align="left"> In attempting to find the best possible model, several different neural network architectures (e.g. linear and categorical convnets, as well as an RNN Long Short Term Memory (LSTM)) were analyzed. Figure 1 below demonstrates how the models performed with respect to the accuracy metric on the test set,
</p>

<p align="center">
  <img width="700" height="300" src="https://github.com/weretew/Autonomous-Tour-Guide-Robot/blob/master/model_accuracy_comparison.png?raw=true"
</p>
  
<h5 align="center"> Figure 1: Comparison of Model Test Accuracy </h5>
  
<p align="left"> Figure 1 clearly demonstrates that the LSTM model achieves an amazingly high level of accuracy. Compared with the other models the LSTM outperforms the Categorical and Linear Convnets by approximately 18% and 75% respectively. The success of the LSTM is most likely attributed to how the model processes sequences of images as opposed to making a decison based on one image every x amount of seconds. Information from past sequences of images can be used in a later time step when making a decision.    
<h2 align="left"> Results </h2>

<p align="left"> After determining the LSTM model to be the best performing model for the course, the robot was tested in a 'live' setting with dynamic human movement as well as relatively static objects in the course environment.  Figure 2 below presents a comparison of the actual versus predicted steering angles of the LSTM model,</p>
<p align="center">
  <img width ="700" height="300" src="https://github.com/weretew/Autonomous-Tour-Guide-Robot/blob/master/lstm_steering_plot.png?raw=true"
</p>
<h5 align="center"> Figure 2: LSTM Steering Angle Actual vs. Predicited </h5>

<p align="left"> Compared with the other models, the LSTM achieved the lowest loss of 0.0063 MSE, which was hands down the lowest loss of any other model.  Furthermore, what was most facinating about the differences between the models, was how they physically performed in the course environment. The LSTM had a noticeably more stable performance than any other model.  This resulted in significantly reducing the amount of sway from the top iPad head piece, thus relieving stress in the robot's bottom chassis and reducing any possible chances of tipping. The LSTM model also greatly smoothed and stablilized the robot's navigation path, creating a much more consistent and less erratic tour experience.  
</p>

<h2 align="left"> Credits </h2>
<p align="left"> This project was completed using open source components.</p>
<p align="left"> 
  
  [Donkeycar](https://github.com/wroscoe/donkey)
   : autonomous RC car racing platform.</p>
  
<p align="left">
  
  [Tawn Kramer](https://github.com/tawnkramer/donkey/blob/master/donkeycar/parts/keras.py)
   : RNN LSTM. </p>

