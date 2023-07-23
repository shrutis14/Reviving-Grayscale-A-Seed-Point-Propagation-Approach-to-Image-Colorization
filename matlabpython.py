import matlab.engine
eng = matlab.engine.start_matlab()
s=eng.genpath('Daisy')
eng.addpath(s,nargout=0)
eng.testing('hi',nargout=0)
eng.quit()
