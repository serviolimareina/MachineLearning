#!/usr/bin/env python
# encoding: utf-8
'''
Machine Learning Algorithm Name: Principal component analysis (PCA)

This is a sample program to demonstrate the implementation of PCA

@author: Cheng-Lin Li a.k.a. Clark

@copyright:  2017 Cheng-Lin Li@University of Southern California. All rights reserved.

@license:    Licensed under the GNU v3.0. https://www.gnu.org/licenses/gpl.html

@contact:    clark.cl.li@gmail.com
@version:    1.0

@create:    October, 7, 2016
@updated: February, 15, 2017

    A PCA class is implemented and provide a lot of value sets for reference.
        self.x = Data set
        self.k = Target dimension we want to reduce to.
        self.covar = Covariance matrix
        self.nm_x = mean_normalization data set.
        self.eigenvalue = eigenvalue of the covariance.
        self.eigenvector = eigenvector of the covariance. Transformation may required to match with data set presentation. 
        self.sorted_eigenvalue = Decreasing sorted eigenvalue.
        self.sorted_eigenvector = Decreasing sorted eigenvector. Transformation may required to match with data set presentation. 
        self.sorted_k_eigenvector = First k decreasing sorted eigenvector. Transformation may required to match with data set presentation. 
        self.z_k_T = The result data set of k dimensions. It transforms the format to data points matrix
        
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class PCA ():
    '''
    classdocs
    
    function lists:
    1. mean_normalization(x): Return self.mn_x
        Return mean normalization data set
    2. convariance_matrix(x): Return self.covar
        Calculate covariance matrix of data set.
    3. get_sorted_eigenvector_nk (covarience, k): Return self.sorted_k_eigenvector
        Get sorted eigenvalue by decreasing then return first k eigenvector.
    4. k_dimension_projection(v, x): Return np.array, _z_k for project results to k dimensions.
        K dimension projection.
    5. execute(datapoints, dimensions): Return self.z_k_T,  The transform format as data points matrix
        Execute the PCA algorithm
    6. plot():
        Plot data into 3D for comparison.
    '''
        
    def __init__(self, datapoints=None, dimensions=0):   
        self.x = np.array(datapoints)
        self.k = dimensions
        self.covar = np.array
        self.mn_x = np.array  # mean normalization data set
        self.eigenvalue = np.array
        self.eigenvector = np.array
        self.sorted_eigenvalue = np.array
        self.sorted_eigenvector = np.array
        self.sorted_k_eigenvector = np.array
        self.z_k_T = np.array
        
    def mean_normalization(self, x):

        _mean = np.mean(x, axis=0)  # Calculate mean for each point
        self.mn_x = np.array(x - _mean)

        return self.mn_x
    
    def covariance_matrix(self, x):
        _covar = np.array
        _x = np.array(x)

        _covar = np.cov(_x.T)  # Actually np.cov() will perform mean_normalizaation automatically.
        self.covar = _covar

        return self.covar
    
    def get_sorted_eigenvector_nk (self, covarience, k):
        # Get sorted eigenvalue by decreasing then return first k eigenvector. 
        _eigenvalue = np.array
        _eigenvector = np.array  
        _v = np.array     
        _sorted_value_idx = np.array

        _eigenvector, _eigenvalue, _v = np.linalg.svd(covarience)

        self.eigenvalue = _eigenvalue
        self.eigenvector = _eigenvector
        
        _sorted_value_idx = np.argsort(-_eigenvalue)  # Decreasing sort

        _eigenvector = _eigenvector[:, _sorted_value_idx]  # Get decreasing sort eigenvector
        self.sorted_eigenvector = _eigenvector
        
        _eigenvalue = _eigenvalue[_sorted_value_idx]  # Get sorted eigenvalue
        self.sorted_eigenvalue = _eigenvalue
        
        self.sorted_k_eigenvector = self.sorted_eigenvector[:, :k]  # Get first K values from sorted eigenvalue
        
        return self.sorted_k_eigenvector
    
    def k_dimension_projection(self, v, x):
        
        _z_k = np.array
        
        _z_k = v.T.dot(x.T)  # input data format should be transform for calculation.
        
        return _z_k
    
    def execute(self, datapoints, dimensions):
        '''
        Execute the PCA algorithm
        '''
        _covar = self.covar
        _z_k = np.array
        _nx = np.array  # new data set after mean normalization
        self.x = datapoints
        self.k = dimensions
        _v_k = np.array  # k eigenvector by decreasing sorted eigenvalue
        
        if(datapoints is None):
            return None
        else :        
            _nx = self.mean_normalization(self.x)
            _covar = self.covariance_matrix(_nx)
            _v_k = self.get_sorted_eigenvector_nk(_covar, self.k)               
            _z_k = self.k_dimension_projection(_v_k, _nx)
            self.z_k_T = _z_k.T
            return self.z_k_T  # Transform the format to data points matrix

    def plot(self):
        '''
        Plot data into 3D for comparison.
        '''
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        _data_set = self.z_k_T      
        for i in range(len(_data_set)):
            _x = _data_set[i][0]
            _y = _data_set[i][1]
            _z = 0
            _c_p = ax.scatter(_x, _y, _z, c='c', marker='^') 
                         
        _data_set = self.x
        for i in range(len(_data_set)):
            _x = _data_set[i][0]
            _y = _data_set[i][1]
            _z = _data_set[i][2]
            _r_p = ax.scatter(_x, _y, _z, c='r', marker='o') 
        
        ax.legend ([_c_p, _r_p], ['Projected data','Original data'])        
        plt.show()
            
    
def getInputData(filename):
    # Get data from data file
    _data = np.genfromtxt(filename, delimiter='\t')
    return _data    


if __name__ == '__main__':
    
    '''
        Main program for the PCA class execution.
        Due to the definition of data set is different between input data and matrix of numpy library. 
        Some array/matrix transformation is required.
    
    '''
        
    dimension = 2
    datapoints = getInputData('pca-data.txt')   
    pca = PCA()
    z_k = pca.execute(datapoints, dimension)
    # print ('pca.covar=', pca.covar)
    # print('pca.eigenvalue.T=', pca.eigenvalue.T)
    print('pca.sorted k eigenvector=', pca.sorted_k_eigenvector.T) #Transform the format to original format

    print('Dimensions reduce to (', dimension, '), and results as below:\n', z_k) 
    pca.plot()
    
    
