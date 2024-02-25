import matlab
import matlab.engine
engine = matlab.engine.start_matlab() # Start MATLAB process
engine = matlab.engine.start_matlab("-desktop") # Start MATLAB process with graphic UI
print(engine.sqrt(2.))
