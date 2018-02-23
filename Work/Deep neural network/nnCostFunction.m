function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size1, ...
                                   hidden_layer_size2, ...    
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size1 * (input_layer_size + 1)), ...
                 hidden_layer_size1, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size1 * (input_layer_size + 1))):( (hidden_layer_size1 * (input_layer_size + 1)))+hidden_layer_size2 * (hidden_layer_size1 + 1)), ...
                 hidden_layer_size2, (hidden_layer_size1 + 1));
             

Theta3 = reshape(nn_params((1 + hidden_layer_size1 * (input_layer_size + 1))+hidden_layer_size2 * (hidden_layer_size1 + 1):end), ...
                 num_labels, (hidden_layer_size2 + 1));

% Setup some useful variables
m = size(X, 1);
a1=X;
         
% You need to return the following variables correctly 
J = 0;

Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));
Theta3_grad = zeros(size(Theta3));

X = [ones(m, 1) X];
% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%         
        

        arr=X*Theta1';
        z2=arr;
        arr=sigmoid(arr);
        a2=arr;
        
        r = size(arr, 1);
        arr=[ones(r,1) arr];
        arr=arr*Theta2';
        z3=arr;
        arr=sigmoid(arr);
        a3=arr;
        
        r = size(arr, 1);
        arr=[ones(r,1) arr];
        arr=arr*Theta3';
        z4=arr;
        arr=sigmoid(arr);
        a4=arr;
        
        arrt= 1-arr;
        arrl=log(arr);
        arrtl=log(arrt);
        [s,q]=size(arr);
        yp=zeros(m,q);
        yn=zeros(m,q);
       
for i=1:m,
  yp(i,y(i))=1; 
end; 

yn=1-yp;
temp=yp.*arrl+yn.*arrtl;
J=-1/m*sum(temp(:));

t1=Theta1.*Theta1;
t2=Theta2.*Theta2;
t3=Theta3.*Theta3;

s1=sum(t1(:));
s2=sum(t2(:));
s3=sum(t3(:));

t1=Theta1(:,1).*Theta1(:,1);
s1=s1-sum(t1(:));

t2=Theta2(:,1).*Theta2(:,1);
s2=s2-sum(t2(:));

t3=Theta3(:,1).*Theta3(:,1);
s3=s3-sum(t3(:));

J=J+lambda/2/m*(s1+s2+s3);

% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.


%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%


del4=a4-yp;

del3=(del4*Theta3);
del3=del3(:,2:end).*[sigmoidGradient(z3)];

del2=(del3*Theta2);
del2=del2(:,2:end).*[sigmoidGradient(z2)];

[c1,c2]=size(a1);
[c3,c4]=size(a2);
[c5,c6]=size(a3);

Delta3=del4'*[ones(c5,1) a3];
Delta2=del3'*[ones(c3,1) a2];
Delta1=del2'*[ones(c1,1) a1];

[c1,c2]=size(Theta1);
[c3,c4]=size(Theta2);
[c5,c6]=size(Theta3);

bf1=[zeros(c1,1) ones(c1,c2-1)];
bf2=[zeros(c3,1) ones(c3,c4-1)];
bf3=[zeros(c5,1) ones(c5,c6-1)];

Theta1_grad=1/m.* Delta1 + lambda/m*(Theta1.*bf1);
Theta2_grad=1/m.* Delta2 + lambda/m*(Theta2.*bf2);
Theta3_grad=1/m.* Delta3 + lambda/m*(Theta3.*bf3);



%fprintf('\n sizes of c1 c2 c3 c4 %f %f %f %f\n', c1,c2,c3,c4);













% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:) ;Theta3_grad(:) ];


end
