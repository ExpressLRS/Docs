import shutil, os, glob

langs = {'en'}

assetDir = 'docs/assets/images'

# for filename in glob.iglob('assetsFolder', recursive=True):


for subdir, dirs, files in os.walk(assetDir):
    for file in files:
        infilename = os.path.join(subdir, file)
        if not os.path.isfile(infilename): continue
        print(infilename)
        for lang in langs:
            newname = infilename.replace('.', '.'+lang+'.')
            shutil.copy(infilename, newname)