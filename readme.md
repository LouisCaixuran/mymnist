readme.md

Predict a integer image

Test data is stored in testdata directory

Dataset is the mnist standard train and test set



### Step1
Use train.py to train and store the two layer net model in two_layer_net.pkl
	
	$python3 train.py
	train acc, test acc | 0.10441666666666667, 0.1028
	train acc, test acc | 0.8023833333333333, 0.8073
	train acc, test acc | 0.8756666666666667, 0.8785
	train acc, test acc | 0.8978666666666667, 0.8999
	train acc, test acc | 0.9068666666666667, 0.9102
	train acc, test acc | 0.9144333333333333, 0.9148
	train acc, test acc | 0.9203166666666667, 0.9218
	train acc, test acc | 0.9235666666666666, 0.9244
	train acc, test acc | 0.92845, 0.9296
	train acc, test acc | 0.9311166666666667, 0.9317
	train acc, test acc | 0.9345833333333333, 0.9351
	train acc, test acc | 0.93695, 0.9374
	train acc, test acc | 0.94025, 0.9396
	train acc, test acc | 0.9419333333333333, 0.9396
	train acc, test acc | 0.9441833333333334, 0.9425
	train acc, test acc | 0.9457833333333333, 0.9445
	train acc, test acc | 0.9484833333333333, 0.9477

### Step2
Use two_layer_test.py to test the accuracy of the model

	$python3 two_layer_test.py
	Accuracy:0.9466

