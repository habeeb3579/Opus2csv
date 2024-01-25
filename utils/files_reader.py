import opusFC
import os
def opusFilesReader(files):
    wavenumbers = []
    absorbance = []
    params = []
    file_names = []
    if files:
        for f in files:
            datablocks = opusFC.listContents(f)
            #logging.debug(datablocks)
            ab_count = [datablock for datablock in datablocks if datablock[0]=='AB']
            if ab_count:
                data = opusFC.getOpusData(f, datablocks[0])
                wavenumbers.append(data.x)
                absorbance.append(data.y)
                params.append(data.parameters)
                file_names.append(os.path.basename(f))
                #valuesos.append((np.append(dataos.x, 'File Name'), np.append(dataos.y,os.path.basename(f))))

    return (wavenumbers, absorbance, params, file_names)