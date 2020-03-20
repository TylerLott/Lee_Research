# Lee_Research
This repo uses composite data based on four variables (fiber type, fiber weight, dispersing agent, and micing agent). The failure load and the max deflection were determined experimentally. This reasearch is being conducted by undergraduate Tyler Lott under advisement of Dr. Juhyeong Lee and Dr. Som Dutta.

## Approach
A neural network is used to predict the failure load of a given combination of the four variables. A Sequantial model is used with a total of five layers. The activation functions at the layers are rectified linear as well as hyperbolic tangent. The optimizer used in Root Mean Square Propagation with a learning rate of .001. The original data is split into training and testing catagories with a split of 90% training and 10% test. The training dataset is then split into two catagories, training and validation. The split is 90% training and 10% validation. 
