import matplotlib.pyplot as plt
import pydicom
import pydicom.data
  
# Full path of the DICOM file is passed in base
base = r"D:\Programming\Python\Learning Python\DCM"
pass_dicom = "sample.dcm"  # file name is 1-12.dcm
  
# enter DICOM image name for pattern
# result is a list of 1 element
filename = pydicom.data.data_manager.get_files(base, pass_dicom)[0]
  
ds = pydicom.dcmread(filename)

# file1 = open("MyFile.txt","a")

# file1.write(ds.decode)
# file1.close() 
print(ds)

