function p = predict(Theta1, Theta2,Theta3, X,y)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta3, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

h1 = sigmoid([ones(m, 1) X] * Theta1');
h2 = sigmoid([ones(m, 1) h1] * Theta2');
h3 = sigmoid([ones(m, 1) h2] * Theta3');

TP=0;
TN=0;
FP=0;
FN=0;

for i=1:m,
  if h3(i,1)>h3(i,2) && y(i)==1
      TP=TP+1;
  end;
  if h3(i,1)<h3(i,2) && y(i)==1
      TN=TN+1;
  end;
  if h3(i,1)<h3(i,2) && y(i)==2
      FP=FP+1;
  end;
  if h3(i,1)>h3(i,2) && y(i)==2
      FN=FN+1;
  end;
  
end; 

fprintf('%f ', m);
fprintf('%f ', TP);
fprintf('%f ', TN);
fprintf('%f ', FP);
fprintf('%f ', FN);


[dummy, p] = max(h3, [], 2);

% =========================================================================


end
