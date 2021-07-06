from pydub import AudioSegment
import argparse
import os
import sys
folder = './'
for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.tmp', '.m4a')
    output = os.rename(infilename, newname)


formats_to_convert = ['.m4a']

for (dirpath, dirnames, filenames) in os.walk("./"):
    for filename in filenames:
        if filename.endswith(tuple(formats_to_convert)):

            filepath = dirpath + '/' + filename
            (path, file_extension) = os.path.splitext(filepath)
            file_extension_final = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(filepath,
                                               file_extension_final)
                mp3_filename = filename.replace(file_extension_final, 'mp3')
                mp3_path = dirpath + '/' + mp3_filename
                print('CONVERTING: ' + str(filepath))
                file_handle = track.export(mp3_path, format='mp3')
                os.remove(filepath)
            except:
                print("ERROR CONVERTING " + str(filepath))
