import numpy as np
class FeatureExtractorReg(object):
    def __init__(self):
        self.w=15
        self.noisy = 0
        self.list_molecule = ['A',
                              'B',
                              'Q',
                              'R'
                             ]
 
    def fit(self, X_df, y):
        pass
    
    def smooth(self,x,window_len=11,window='hanning'):
        s=np.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
 
        if window == 'flat': #moving average
            w=np.ones(window_len,'d')
        else:
            w=eval('np.'+window+'(window_len)')
        y=np.convolve(w/w.sum(),s,mode='valid')
        return y
            
    def transform(self, X_df):   
        if self.noisy:
            XX = np.array([np.array(dd) for dd in X_df['spectra']])                  
        else:
            XX = np.array([self.smooth(np.array(dd),self.w)[(self.w-1)//2:(1-self.w)//2] for dd in X_df['spectra']])                  
        XX -= np.median(XX, axis=1)[:, None]                                     
        XX /= np.sqrt(np.sum(XX ** 2, axis=1))[:, None]                          
    
        XX = np.hstack((XX,X_df[self.list_molecule].values))                
 
        return XX 