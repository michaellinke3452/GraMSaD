

def read_segmentation_dataset(filename, train=False, test=False): 
    # Replace "PATH/TO/" with the path to the h5 files:
    # training data:
    # x_train, y_train = read_segmentation_dataset("PATH/TO/S1_train.h5", train=True)
    # testing data:
    # x_test, y_test = read_segmentation_dataset("PATH/TO/S1_test.h5", test=True)
    # Returns: (64x64) numpy arrays of the terrain (x_train, x_test) and the corresponding
    # label matrices (y_train, y_test).      
    import numpy as np
    import h5py 
    
    with h5py.File(filename, "r") as seg_file:  
        if train == True and test == False:
            x_train = seg_file.get("x_train")
            x_train = np.array(x_train)
            y_train = seg_file.get("y_train")
            y_train = np.array(y_train)
            return x_train, y_train
        elif test == True and train == False:
            x_test = seg_file.get("x_test") 
            x_test = np.array(x_test)
            y_test = seg_file.get("y_test") 
            y_test = np.array(y_test)
            return x_test, y_test
        else: 
            # only for files that include both train and test data!
            x_train = seg_file.get("x_train")
            x_train = np.array(x_train)
            y_train = seg_file.get("y_train")
            y_train = np.array(y_train)
            x_test = seg_file.get("x_test") 
            x_test = np.array(x_test)
            y_test = seg_file.get("y_test") 
            y_test = np.array(y_test)
            return x_train, y_train, x_test, y_test
    




def read_detection_dataset(filename, train=False, test=False): 
    # Replace "PATH/TO/" with the path to the h5 files:
    # training data:
    # x_train, y_train_class, y_train_reg = read_detection_dataset("PATH/TO/D1_train.h5", train=True)    
    # testing data:
    # x_test, y_test_class, y_test_reg = read_detection_dataset("PATH/TO/D1_test.h5", test=True)
    # Returns: (64x64) numpy arrays of the terrain (x_train, x_test), the corresponding
    # label matrices for center point segmentation (y_train_class, y_test_class), and radius length
    # regression (y_train_reg, y_test_reg).        
    import numpy as np
    import h5py 

    with h5py.File(filename, "r") as seg_file:  
        if train == True and test == False:
            x_train = seg_file.get("x_train")
            x_train = np.array(x_train)
            y_train_class = seg_file.get("y_train_class")
            y_train_class = np.array(y_train_class)
            y_train_reg = seg_file.get("y_train_reg")
            y_train_reg = np.array(y_train_reg)
            return x_train, y_train_class, y_train_reg

        elif test == True and train == False:
            x_test = seg_file.get("x_test") 
            x_test = np.array(x_test)
            y_test_class = seg_file.get("y_test_class") 
            y_test_class = np.array(y_test_class)
            y_test_reg = seg_file.get("y_test_reg") 
            y_test_reg = np.array(y_test_reg)
            return x_test, y_test_class, y_test_reg 

        else:
            # only for files that include both train and test data!
            x_train = seg_file.get("x_train")
            x_train = np.array(x_train)
            y_train_class = seg_file.get("y_train_class")
            y_train_class = np.array(y_train_class)
            y_train_reg = seg_file.get("y_train_reg")
            y_train_reg = np.array(y_train_reg)
            x_test = seg_file.get("x_test") 
            x_test = np.array(x_test)
            y_test_class = seg_file.get("y_test_class") 
            y_test_class = np.array(y_test_class)
            y_test_reg = seg_file.get("y_test_reg") 
            y_test_reg = np.array(y_test_reg)
            return x_train, y_train_class, y_train_reg, x_test, y_test_class, y_test_reg 