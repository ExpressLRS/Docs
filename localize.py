import shutil, os, glob

langs = {'en'}

assetDir = 'docs/assets/images'

# for filename in glob.iglob('assetsFolder', recursive=True):


for subdir, dirs, files in os.walk(assetDir):
    for file in files:
        infilename = os.path.join(subdir, file)
        if not os.path.isfile(infilename): continue
        for lang in langs:
            if '.' + lang + '.' not in infilename:
                newname = infilename.replace('.', '.'+lang+'.')
                shutil.copy(infilename, newname)