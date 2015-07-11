import numpy as np
import matplotlib.pyplot as plt
import os


def plot_drives(path_to_data= '../../data/drivers',driverId=1, outliers=False):
    '''
    :param path_to_data: Path to the dataset
    :param driverId: The driver whose drives we
    :param outliers: Int IDs of outliers, if given, mark them in the plot
    :return:
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    r = lambda : np.random.randint(0, 255)
    path_to_driver = path_to_data + '/' + str(driverId)
    drives = os.listdir(path_to_driver)
    for drive in drives:
        print 'plotting ', str(drive)

        curr_drive = np.genfromtxt(path_to_driver+'/'+str(drive), delimiter=',',skiprows=1, dtype='float')
        #outliers given
        if outliers:
            driveID = int(drive.split('.')[0])
            if driveID in outliers:
                curr_plot_handle = ax.plot(curr_drive[:,0], curr_drive[:,1], c='r')
            else:
                rand_col = '#%02X%02X%02X' % (0,r(),r())
                curr_plot_handle = ax.plot(curr_drive[:,0], curr_drive[:,1], c=rand_col, linestyle='--')
        else:
            rand_col = '#%02X%02X%02X' % (0,r(),r())
            curr_plot_handle = ax.plot(curr_drive[:,0], curr_drive[:,1], c=rand_col, linestyle='--', label='Outlier')

        print curr_drive.shape
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

# plott all drives of driver 1, labeling 1, 69 and 183 as outliers
plot_drives(outliers=[1,69,183])