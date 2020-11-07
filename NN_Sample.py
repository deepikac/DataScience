"""
https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
"""
import numpy as np


class NeuralNetwork():
     """Initialize the Neural network
     input vector will be 1 * 3
     weights1 will be 3 * 4
     weights2 vector will be 4*1
     """

     def __init__(self,x,y):
         self.input = x
         self.weights1= np.random.rand(self.input.shape[1],4)
         self.weights2= np.random.rand(4,1)
         self.y = y

     def sigmoid_fn(self, input):
         """
         Implement sigmoid Function :
         Read every element of Matrix after linear combination of Input vector and weights vector
         Implement Sigmoid function on Independent element and return a output array
         :param input:
         :return:
         """
         i_arr = np.array(input)
         output_post_sigmoid = []

         for j in range(np.shape(i_arr)[1]):
              sigmoid_val = 1 / (1 + np.exp(-(i_arr[0,j])))

              if sigmoid_val > 0.5:
                  output_post_sigmoid.append(0.01)
              else:
                  output_post_sigmoid.append(0)

         return np.array([output_post_sigmoid])

     def feed_forward(self):
         """
            Implement FeedForward function
            apply linear combination of Input and weight vector , apply sigmoid function and retur the the final output
            for all the layer of Neural network
         :return:
         """
         self.layer1 =  self.sigmoid_fn(np.dot(self.input,self.weights1))
         self.output = self.sigmoid_fn(np.dot(self.layer1,self.weights2))


def build_main():
    """
    main function
    :return:
    """

    x = np.array([[0.7,0.5,0.2]])
    y = 1

    print(x.shape)
    nn = NeuralNetwork(x,y)

    print(f"Neural network Input Vector is {nn.input} " )
    print(f"Neural network layer 1 weight Vector is {nn.weights1} ")
    print(f"Neural network layer 2 Weight Vector is {nn.weights2} ")

    nn.feed_forward()
    print(f"Neural network layer 1 output Vector is {nn.layer1} ")
    print(f"Neural network layer 1 output Vector is {nn.output} ")


if __name__ == "__main__":
    build_main()