clear ; close all; clc

input_layer_size  = 64; 
hidden_layer_size1 = 25;   
hidden_layer_size2 = 10;
   

num_labels = 2;

X = csvread('C://Users/Mehul_Jain/Desktop/data_car/good.csv');
y= csvread('C://Users/Mehul_Jain/Desktop/data_car/ans.csv');

Theta11=randInitializeWeights(input_layer_size,hidden_layer_size1);
Theta22=randInitializeWeights(hidden_layer_size1,hidden_layer_size2);
Theta33=randInitializeWeights(hidden_layer_size2,num_labels);
%Theta4=randn(6,9);
lambda = 5;

options = optimset('MaxIter', 70);
initial_nn_params = [Theta11(:) ; Theta22(:) ;Theta33(:)];

costFunction = @(p) nnCostFunction(p, ...
                                   input_layer_size, ...
                                   hidden_layer_size1, ...
                                   hidden_layer_size2, ...
                                   num_labels, X, y, lambda);

% Now, costFunction is a function that takes in only one argument (the
% neural network parameters)
[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

% Obtain Theta1 and Theta2 back from nn_params
Theta1 = reshape(nn_params(1:hidden_layer_size1 * (input_layer_size + 1)), ...
                 hidden_layer_size1, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size1 * (input_layer_size + 1))):( (hidden_layer_size1 * (input_layer_size + 1)))+hidden_layer_size2 * (hidden_layer_size1 + 1)), ...
                 hidden_layer_size2, (hidden_layer_size1 + 1));
             

Theta3 = reshape(nn_params((1 + hidden_layer_size1 * (input_layer_size + 1))+hidden_layer_size2 * (hidden_layer_size1 + 1):end), ...
                 num_labels, (hidden_layer_size2 + 1));

pred = predict(Theta1, Theta2,Theta3, X,y);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);

m = size(X, 1);
num_labels = size(Theta3, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

h1 = sigmoid([ones(m, 1) X] * Theta1');
h2 = sigmoid([ones(m, 1) h1] * Theta2');
h3 = sigmoid([ones(m, 1) h2] * Theta3');



